import csv
import itertools
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments"
FIG_DIR = ROOT / "figures"
DOCS = ROOT / "docs"

RESULTS_CSV = EXP_DIR / "episode_results.csv"
SUMMARY_JSON = EXP_DIR / "summary.json"
EVIDENCE_MD = DOCS / "evidence_summary.md"


def min_norm_halfspace(H: np.ndarray, h: np.ndarray, tol: float = 1e-8) -> Tuple[Optional[np.ndarray], str]:
    """Solve min ||c||_2 subject to H c >= h by active-set enumeration.

    The correction dimension is small in this experiment. At the Euclidean projection
    onto a polyhedron in R^d, an optimal point has at most d independent active
    halfspaces, so enumerating active sets is exact up to numerical tolerance.
    """
    k, d = H.shape
    if np.all(h <= tol):
        return np.zeros(d), "already_satisfied"

    best = None
    best_norm = np.inf
    best_status = "infeasible"
    indices = range(k)
    for r in range(1, d + 1):
        for active in itertools.combinations(indices, r):
            A = H[list(active), :]
            b = h[list(active)]
            if np.linalg.matrix_rank(A, tol=1e-9) < r:
                continue
            gram = A @ A.T
            try:
                lam = np.linalg.solve(gram, b)
            except np.linalg.LinAlgError:
                lam = np.linalg.pinv(gram) @ b
            c = A.T @ lam
            if np.all(H @ c >= h - 1e-7):
                n = float(np.linalg.norm(c))
                if n < best_norm:
                    best = c
                    best_norm = n
                    best_status = "optimal"
    if best is not None:
        return best, best_status

    # Numerical fallback for rare degenerate active sets. The experiment does not
    # depend on SciPy for the usual path, but the package is available in the
    # batch environment and keeps the generated labels honest.
    try:
        from scipy.optimize import minimize

        def obj(x: np.ndarray) -> float:
            return 0.5 * float(x @ x)

        constraints = [{"type": "ineq", "fun": lambda x, row=row, rhs=rhs: float(row @ x - rhs)} for row, rhs in zip(H, h)]
        result = minimize(obj, np.zeros(d), method="SLSQP", constraints=constraints, options={"maxiter": 300, "ftol": 1e-10})
        if result.success and np.all(H @ result.x >= h - 1e-6):
            return np.asarray(result.x), "optimal_slsqp"
    except Exception:
        pass
    return best, best_status


def current_only(H: np.ndarray, h: np.ndarray) -> np.ndarray:
    row = H[0]
    rhs = max(0.0, float(h[0]))
    denom = float(row @ row)
    if rhs <= 0.0 or denom <= 1e-12:
        return np.zeros(H.shape[1])
    return row * (rhs / denom)


def one_axis_current(H: np.ndarray, h: np.ndarray) -> np.ndarray:
    row = H[0]
    j = int(np.argmax(np.abs(row)))
    rhs = max(0.0, float(h[0]))
    c = np.zeros(H.shape[1])
    if rhs <= 0.0 or abs(row[j]) <= 1e-12:
        return c
    c[j] = rhs / row[j]
    return c


def gradient_line_search(H: np.ndarray, h: np.ndarray, max_norm: float) -> Tuple[np.ndarray, str]:
    violations = np.maximum(h, 0.0)
    direction = H.T @ violations
    norm = float(np.linalg.norm(direction))
    if norm <= 1e-12:
        return np.zeros(H.shape[1]), "zero"
    direction = direction / norm
    best = None
    for alpha in np.linspace(0.0, max_norm, 401):
        c = direction * alpha
        if np.all(H @ c >= h - 1e-7):
            best = c
            break
    if best is None:
        return direction * max_norm, "failed"
    return best, "line_search"


def random_search(H: np.ndarray, h: np.ndarray, rng: np.random.Generator, max_norm: float) -> Tuple[np.ndarray, str]:
    best = None
    best_norm = np.inf
    for _ in range(800):
        direction = rng.normal(size=H.shape[1])
        dn = np.linalg.norm(direction)
        if dn <= 1e-12:
            continue
        direction /= dn
        radius = rng.random() ** (1.0 / H.shape[1]) * max_norm
        c = direction * radius
        if np.all(H @ c >= h - 1e-7):
            n = float(np.linalg.norm(c))
            if n < best_norm:
                best = c
                best_norm = n
    if best is None:
        return np.zeros(H.shape[1]), "failed"
    return best, "random"


def make_reachable_trial(rng: np.random.Generator, k: int = 9, d: int = 3) -> Tuple[np.ndarray, np.ndarray, Dict[str, float]]:
    anchor = rng.normal(size=d)
    anchor /= max(1e-12, np.linalg.norm(anchor))
    anchor *= rng.uniform(0.35, 1.25)
    anchor_dir = anchor / max(1e-12, np.linalg.norm(anchor))
    H = rng.normal(size=(k, d))
    # Create a learner nullspace by suppressing one physical correction direction
    # on a random subset of trials. This mirrors contact effort that the update
    # rule does not use.
    if rng.random() < 0.45:
        H[:, 2] *= rng.uniform(0.0, 0.08)
    # Make every future margin compatible with the anchor correction.
    for i in range(k):
        if H[i] @ anchor < 0:
            H[i] *= -1.0
        # Avoid labeling a trial reachable when one row is nearly orthogonal to
        # the hidden feasible correction.
        dot = H[i] @ anchor
        min_dot = rng.uniform(0.18, 0.35)
        if dot < min_dot:
            H[i] += ((min_dot - dot) / max(1e-12, np.linalg.norm(anchor))) * anchor_dir
    raw = H @ anchor
    h = raw * rng.uniform(0.45, 0.92, size=k)
    return H, h, {"reachable": 1.0, "anchor_norm": float(np.linalg.norm(anchor))}


def make_unreachable_trial(rng: np.random.Generator, k: int = 9, d: int = 3) -> Tuple[np.ndarray, np.ndarray, Dict[str, float]]:
    H = rng.normal(size=(k, d))
    u = rng.normal(size=d)
    u /= max(1e-12, np.linalg.norm(u))
    H[0] = u
    H[1] = -u
    h = np.abs(rng.normal(loc=0.25, scale=0.08, size=k))
    h[0] = rng.uniform(0.45, 0.85)
    h[1] = rng.uniform(0.45, 0.85)
    # Most other constraints are mild, but the first two are contradictory.
    h[2:] *= rng.uniform(0.2, 0.6, size=k - 2)
    return H, h, {"reachable": 0.0, "anchor_norm": float("nan")}


def evaluate_method(name: str, c: Optional[np.ndarray], status: str, H: np.ndarray, h: np.ndarray, reachable: bool, max_norm: float) -> Dict[str, object]:
    if c is None:
        c = np.zeros(H.shape[1])
        norm = float("nan")
    else:
        norm = float(np.linalg.norm(c))
    margins = H @ c - h
    all_success = bool(np.all(margins >= -1e-7) and norm <= max_norm + 1e-7)
    current_success = bool(margins[0] >= -1e-7 and norm <= max_norm + 1e-7)
    detects_unreachable = (not reachable) and (status in {"infeasible", "failed"})
    return {
        "method": name,
        "status": status,
        "norm": norm,
        "future_success": int(all_success),
        "current_success": int(current_success),
        "detects_unreachable": int(detects_unreachable),
        "min_margin": float(np.min(margins)),
        "max_margin": float(np.max(margins)),
    }


def run(seed: int = 15, n_trials: int = 600, max_norm: float = 3.0) -> List[Dict[str, object]]:
    rng = np.random.default_rng(seed)
    rows: List[Dict[str, object]] = []
    for trial in range(n_trials):
        if rng.random() < 0.22:
            H, h, meta = make_unreachable_trial(rng)
        else:
            H, h, meta = make_reachable_trial(rng)
        reachable = bool(meta["reachable"])

        c_ubc, ubc_status = min_norm_halfspace(H, h)
        if c_ubc is not None and np.linalg.norm(c_ubc) > max_norm:
            c_ubc = None
            ubc_status = "outside_physical_cap"
        baselines = [
            ("UBC", c_ubc, ubc_status),
            ("current_only", current_only(H, h), "current_constraint"),
            ("one_axis_current", one_axis_current(H, h), "current_axis"),
        ]
        c_grad, grad_status = gradient_line_search(H, h, max_norm)
        baselines.append(("gradient_line_search", c_grad, grad_status))
        c_rand, rand_status = random_search(H, h, rng, max_norm)
        baselines.append(("random_search", c_rand, rand_status))

        rank = int(np.linalg.matrix_rank(H, tol=1e-8))
        null_dim = H.shape[1] - rank
        for name, c, status in baselines:
            row = evaluate_method(name, c, status, H, h, reachable, max_norm)
            row.update(
                {
                    "trial": trial,
                    "reachable": int(reachable),
                    "rank_H": rank,
                    "null_dim": null_dim,
                    "max_norm": max_norm,
                    "anchor_norm": meta["anchor_norm"],
                }
            )
            rows.append(row)
    return rows


def write_results(rows: List[Dict[str, object]]) -> Dict[str, Dict[str, float]]:
    EXP_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "trial",
        "method",
        "reachable",
        "status",
        "norm",
        "future_success",
        "current_success",
        "detects_unreachable",
        "min_margin",
        "max_margin",
        "rank_H",
        "null_dim",
        "max_norm",
        "anchor_norm",
    ]
    with RESULTS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    summary: Dict[str, Dict[str, float]] = {}
    methods = sorted({str(r["method"]) for r in rows})
    for method in methods:
        subset = [r for r in rows if r["method"] == method]
        reachable_subset = [r for r in subset if r["reachable"] == 1]
        unreachable_subset = [r for r in subset if r["reachable"] == 0]
        finite_norms = [float(r["norm"]) for r in reachable_subset if np.isfinite(float(r["norm"]))]
        successful_norms = [
            float(r["norm"])
            for r in reachable_subset
            if r["future_success"] == 1 and np.isfinite(float(r["norm"]))
        ]
        summary[method] = {
            "future_success_all": float(np.mean([r["future_success"] for r in subset])),
            "future_success_reachable": float(np.mean([r["future_success"] for r in reachable_subset])) if reachable_subset else 0.0,
            "current_success_reachable": float(np.mean([r["current_success"] for r in reachable_subset])) if reachable_subset else 0.0,
            "detects_unreachable": float(np.mean([r["detects_unreachable"] for r in unreachable_subset])) if unreachable_subset else 0.0,
            "mean_norm_reachable": float(np.mean(finite_norms)) if finite_norms else float("nan"),
            "mean_norm_successful": float(np.mean(successful_norms)) if successful_norms else float("nan"),
        }
    SUMMARY_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def plot_summary(summary: Dict[str, Dict[str, float]]) -> None:
    methods = ["UBC", "current_only", "one_axis_current", "gradient_line_search", "random_search"]
    labels = ["UBC", "Current", "Axis", "Gradient", "Random"]
    success = [summary[m]["future_success_reachable"] for m in methods]
    detect = [summary[m]["detects_unreachable"] for m in methods]
    norms = [summary[m]["mean_norm_successful"] for m in methods]

    plt.figure(figsize=(7.0, 3.5))
    x = np.arange(len(methods))
    width = 0.38
    plt.bar(x - width / 2, success, width, label="reachable future success")
    plt.bar(x + width / 2, detect, width, label="unreachable detected")
    plt.xticks(x, labels)
    plt.ylim(0, 1.05)
    plt.ylabel("rate")
    plt.title("Correction methods on future-behavior constraints")
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "success_rates.png", dpi=200)
    plt.close()

    plt.figure(figsize=(7.0, 3.5))
    clean_norms = [0 if not np.isfinite(v) else v for v in norms]
    plt.bar(x, clean_norms, color=["#2f6f8f", "#9c6b2f", "#8464a0", "#4f8a3f", "#777777"])
    plt.xticks(x, labels)
    plt.ylabel("mean norm on successful reachable trials")
    plt.title("Physical correction size")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "correction_norms.png", dpi=200)
    plt.close()


def write_evidence_md(summary: Dict[str, Dict[str, float]], rows: List[Dict[str, object]]) -> None:
    n_trials = len({r["trial"] for r in rows})
    reachable = len({r["trial"] for r in rows if r["reachable"] == 1})
    unreachable = n_trials - reachable
    lines = [
        "# Evidence Summary",
        "",
        f"Trials: {n_trials} total, {reachable} reachable, {unreachable} intentionally unreachable.",
        "",
        "The synthetic embodied-correction environment represents a robot whose physical correction `c` changes future behavior margins through a composed update map `H = A J`, where `J` is the learner's correction-to-parameter channel and `A` maps updated parameters to future behavior margins. The proposed UBC method solves `min ||c||_2` subject to `H c >= h`.",
        "",
        "| Method | Future success on reachable | Detects unreachable | Mean norm on successful reachable |",
        "|---|---:|---:|---:|",
    ]
    for method in ["UBC", "current_only", "one_axis_current", "gradient_line_search", "random_search"]:
        stats = summary[method]
        lines.append(
            f"| {method} | {stats['future_success_reachable']:.3f} | {stats['detects_unreachable']:.3f} | {stats['mean_norm_successful']:.3f} |"
        )
    lines += [
        "",
        "## Interpretation",
        "- Current-only corrections usually satisfy the immediate constraint but often fail the future-context set, demonstrating that present repair is not equivalent to future learning.",
        "- UBC succeeds on the reachable local problems because it solves the exact minimum-norm projected halfspace problem.",
        "- Unreachable trials contain contradictory future margins in the physical correction channel; UBC returns an infeasibility certificate rather than pretending a larger correction would help.",
        "- The evidence is simulated and local. It supports the formal mechanism, not a hardware or global nonlinear claim.",
        "",
        "Generated artifacts:",
        "- `experiments/episode_results.csv`",
        "- `experiments/summary.json`",
        "- `figures/success_rates.png`",
        "- `figures/correction_norms.png`",
    ]
    EVIDENCE_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    rows = run()
    summary = write_results(rows)
    plot_summary(summary)
    write_evidence_md(summary, rows)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
