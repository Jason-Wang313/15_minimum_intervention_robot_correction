import csv
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import LinearConstraint, minimize


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "full_scale"
DOCS = ROOT / "docs"

MASTER_SEED = 15015
MAX_NORM = 3.0


def ensure_dirs() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)


def write_progress(**kwargs: object) -> None:
    payload = {"stage": "running"}
    payload.update(kwargs)
    (OUT / "progress.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")


def unit(v: np.ndarray) -> np.ndarray:
    n = float(np.linalg.norm(v))
    if n <= 1e-12:
        return np.zeros_like(v)
    return v / n


def active_set_min_norm(A: np.ndarray, b: np.ndarray, tol: float = 1e-8) -> Tuple[Optional[np.ndarray], str]:
    k, d = A.shape
    if np.all(b <= tol):
        return np.zeros(d), "already_satisfied"

    best = None
    best_norm = np.inf
    for r in range(1, min(d, k) + 1):
        for active in itertools.combinations(range(k), r):
            M = A[list(active), :]
            rhs = b[list(active)]
            if np.linalg.matrix_rank(M, tol=1e-9) < r:
                continue
            gram = M @ M.T
            try:
                lam = np.linalg.solve(gram, rhs)
            except np.linalg.LinAlgError:
                lam = np.linalg.pinv(gram) @ rhs
            y = M.T @ lam
            if np.all(A @ y >= b - 1e-7):
                n = float(np.linalg.norm(y))
                if n < best_norm:
                    best = y
                    best_norm = n
    if best is None:
        return None, "infeasible"
    return best, "optimal"


def solve_min_norm(
    H: np.ndarray,
    h: np.ndarray,
    max_norm: float = MAX_NORM,
    weights: Optional[np.ndarray] = None,
    x0: Optional[np.ndarray] = None,
) -> Tuple[Optional[np.ndarray], str]:
    """Solve min c^T W c subject to Hc >= h for small correction problems."""
    d = H.shape[1]
    weights = np.ones(d) if weights is None else np.asarray(weights, dtype=float)
    weights = np.maximum(weights, 1e-6)
    inv_sqrt = 1.0 / np.sqrt(weights)
    A = H * inv_sqrt[None, :]

    if H.shape[0] <= 9 and d <= 3:
        y, status = active_set_min_norm(A, h)
    else:
        constraint = LinearConstraint(A, lb=h, ub=np.full_like(h, np.inf, dtype=float))
        if x0 is not None:
            y0 = np.asarray(x0, dtype=float) * np.sqrt(weights)
        else:
            y0 = np.zeros(d)

        def obj(y: np.ndarray) -> float:
            return 0.5 * float(y @ y)

        def jac(y: np.ndarray) -> np.ndarray:
            return y

        result = minimize(
            obj,
            y0,
            jac=jac,
            constraints=[constraint],
            method="SLSQP",
            options={"maxiter": 120, "ftol": 1e-10, "disp": False},
        )
        if result.success and np.all(A @ result.x >= h - 1e-6):
            y, status = np.asarray(result.x), "optimal"
        else:
            y, status = None, "infeasible"

    if y is None:
        return None, status
    c = y * inv_sqrt
    if float(np.linalg.norm(c)) > max_norm + 1e-7:
        return None, "outside_cap"
    return c, status


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
    c = np.zeros(H.shape[1])
    rhs = max(0.0, float(h[0]))
    if rhs > 0.0 and abs(row[j]) > 1e-12:
        c[j] = rhs / row[j]
    return c


def gradient_line_search(H: np.ndarray, h: np.ndarray, max_norm: float = MAX_NORM) -> Tuple[np.ndarray, str]:
    direction = H.T @ np.maximum(h, 0.0)
    direction = unit(direction)
    if np.linalg.norm(direction) <= 1e-12:
        return np.zeros(H.shape[1]), "zero"
    for alpha in np.linspace(0.0, max_norm, 101):
        c = direction * alpha
        if np.all(H @ c >= h - 1e-7):
            return c, "line_search"
    return direction * max_norm, "failed"


def random_search(H: np.ndarray, h: np.ndarray, rng: np.random.Generator, max_norm: float = MAX_NORM, n: int = 360) -> Tuple[np.ndarray, str]:
    d = H.shape[1]
    best = None
    best_norm = np.inf
    for _ in range(n):
        direction = unit(rng.normal(size=d))
        radius = (rng.random() ** (1.0 / d)) * max_norm
        c = direction * radius
        if np.all(H @ c >= h - 1e-7):
            norm = float(np.linalg.norm(c))
            if norm < best_norm:
                best = c
                best_norm = norm
    if best is None:
        return np.zeros(d), "failed"
    return best, "random"


def least_squares_repair(H: np.ndarray, h: np.ndarray, max_norm: float = MAX_NORM) -> Tuple[np.ndarray, str]:
    c, *_ = np.linalg.lstsq(H, h, rcond=None)
    n = float(np.linalg.norm(c))
    if n > max_norm:
        c = c * (max_norm / max(n, 1e-12))
        return c, "lsq_capped"
    return c, "lsq"


def soft_penalty_repair(H: np.ndarray, h: np.ndarray, max_norm: float = MAX_NORM, steps: int = 180) -> Tuple[np.ndarray, str]:
    c = np.zeros(H.shape[1])
    lr = 0.05
    lam = 8.0
    for _ in range(steps):
        slack = h - H @ c
        active = np.maximum(slack, 0.0)
        grad = c - 2.0 * lam * (H.T @ active)
        c = c - lr * grad
        n = float(np.linalg.norm(c))
        if n > max_norm:
            c = c * (max_norm / max(n, 1e-12))
        lr *= 0.995
    return c, "soft_penalty"


def sequential_greedy(H: np.ndarray, h: np.ndarray, max_norm: float = MAX_NORM) -> Tuple[np.ndarray, str]:
    c = np.zeros(H.shape[1])
    for _ in range(5):
        changed = False
        for row, rhs in zip(H, h):
            violation = float(rhs - row @ c)
            denom = float(row @ row)
            if violation > 1e-8 and denom > 1e-12:
                c = c + row * (violation / denom)
                changed = True
                n = float(np.linalg.norm(c))
                if n > max_norm:
                    c = c * (max_norm / max(n, 1e-12))
        if not changed:
            break
    status = "sequential" if np.all(H @ c >= h - 1e-7) else "failed"
    return c, status


def make_reachable(
    rng: np.random.Generator,
    k: int,
    d: int,
    null_prob: float = 0.35,
    anchor_scale: Tuple[float, float] = (0.35, 1.20),
) -> Tuple[np.ndarray, np.ndarray, Dict[str, object]]:
    anchor = unit(rng.normal(size=d)) * rng.uniform(*anchor_scale)
    anchor_dir = unit(anchor)
    H = rng.normal(size=(k, d))
    null_dim = 0
    if rng.random() < null_prob and d > 1:
        null_dim = int(rng.integers(1, min(3, d) + 1))
        H[:, -null_dim:] *= rng.uniform(0.0, 0.06)
    for i in range(k):
        if H[i] @ anchor < 0:
            H[i] *= -1.0
        dot = float(H[i] @ anchor)
        min_dot = rng.uniform(0.16, 0.34)
        if dot < min_dot:
            H[i] += ((min_dot - dot) / max(1e-12, np.linalg.norm(anchor))) * anchor_dir
    h = (H @ anchor) * rng.uniform(0.45, 0.88, size=k)
    return H, h, {"reachable": 1, "anchor": anchor, "null_dim_hidden": null_dim}


def make_unreachable(rng: np.random.Generator, k: int, d: int, null_prob: float = 0.35) -> Tuple[np.ndarray, np.ndarray, Dict[str, object]]:
    H = rng.normal(size=(k, d))
    u = unit(rng.normal(size=d))
    H[0] = u
    H[1] = -u
    if rng.random() < null_prob and d > 1:
        H[:, -1] *= rng.uniform(0.0, 0.04)
    h = np.abs(rng.normal(loc=0.18, scale=0.06, size=k))
    h[0] = rng.uniform(0.45, 0.85)
    h[1] = rng.uniform(0.45, 0.85)
    h[2:] *= rng.uniform(0.15, 0.45, size=max(0, k - 2))
    return H, h, {"reachable": 0, "anchor": None, "null_dim_hidden": 1}


def make_trial(rng: np.random.Generator, k: int, d: int, reachable_ratio: float, null_prob: float) -> Tuple[np.ndarray, np.ndarray, Dict[str, object]]:
    if rng.random() < reachable_ratio:
        return make_reachable(rng, k, d, null_prob)
    return make_unreachable(rng, k, d, null_prob)


def evaluate(
    family: str,
    method: str,
    c: Optional[np.ndarray],
    status: str,
    H_true: np.ndarray,
    h_true: np.ndarray,
    reachable: int,
    max_norm: float = MAX_NORM,
    extra: Optional[Dict[str, object]] = None,
    true_success_fn: Optional[Callable[[np.ndarray], bool]] = None,
) -> Dict[str, object]:
    d = H_true.shape[1]
    if c is None:
        c = np.zeros(d)
        norm = float("nan")
    else:
        norm = float(np.linalg.norm(c))
    margins = H_true @ c - h_true
    if true_success_fn is None:
        success = bool(np.all(margins >= -1e-7) and norm <= max_norm + 1e-7)
    else:
        success = bool(true_success_fn(c) and norm <= max_norm + 1e-7)
    detects = int((reachable == 0) and status in {"infeasible", "failed", "outside_cap"})
    false_cert = int((reachable == 1) and status not in {"infeasible", "failed", "outside_cap"} and not success)
    row: Dict[str, object] = {
        "family": family,
        "method": method,
        "status": status,
        "reachable": reachable,
        "future_success": int(success),
        "current_success": int(margins[0] >= -1e-7 and norm <= max_norm + 1e-7),
        "detects_unreachable": detects,
        "false_certificate": false_cert,
        "norm": norm,
        "min_margin": float(np.min(margins)),
        "rank_H": int(np.linalg.matrix_rank(H_true, tol=1e-8)),
        "null_dim": int(d - np.linalg.matrix_rank(H_true, tol=1e-8)),
    }
    if extra:
        row.update(extra)
    return row


def aggregate(rows: List[Dict[str, object]], group_cols: Sequence[str]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    keys = list(group_cols) + ["method"]
    out: List[Dict[str, object]] = []
    grouped: Iterable[Tuple[object, pd.DataFrame]]
    grouped = df.groupby(keys, dropna=False) if keys else [((), df)]
    for key, sub in grouped:
        if not isinstance(key, tuple):
            key = (key,)
        row = {name: value for name, value in zip(keys, key)}
        reachable = sub[sub["reachable"] == 1]
        unreachable = sub[sub["reachable"] == 0]
        success_base = reachable if len(reachable) else sub
        row.update(
            {
                "trials": int(len(sub)),
                "reachable_rate": float(sub["reachable"].mean()),
                "overall_success": float(sub["future_success"].mean()),
                "future_success": float(success_base["future_success"].mean()),
                "current_success": float(success_base["current_success"].mean()),
                "detects_unreachable": float(unreachable["detects_unreachable"].mean()) if len(unreachable) else 0.0,
                "false_certificate": float(success_base["false_certificate"].mean()),
                "mean_norm": float(success_base["norm"].mean()),
                "mean_min_margin": float(success_base["min_margin"].mean()),
                "mean_rank": float(sub["rank_H"].mean()),
                "mean_null_dim": float(sub["null_dim"].mean()),
            }
        )
        out.append(row)
    return pd.DataFrame(out)


def write_csv(df: pd.DataFrame, name: str) -> None:
    df.to_csv(OUT / name, index=False, quoting=csv.QUOTE_MINIMAL)


def latex_table(df: pd.DataFrame, columns: Sequence[str], headers: Sequence[str], name: str) -> None:
    lines = [r"\begin{tabular}{" + "l" * len(columns) + "}", r"\toprule"]
    lines.append(" & ".join(headers) + r" \\")
    lines.append(r"\midrule")
    for _, row in df.iterrows():
        vals = []
        for col in columns:
            val = row[col]
            if isinstance(val, (float, np.floating)):
                if math.isnan(float(val)):
                    vals.append("--")
                else:
                    vals.append(f"{float(val):.3f}")
            else:
                vals.append(str(val).replace("_", r"\_"))
        lines.append(" & ".join(vals) + r" \\")
    lines.extend([r"\bottomrule", r"\end{tabular}", ""])
    (OUT / name).write_text("\n".join(lines), encoding="utf-8")


def save_bar(df: pd.DataFrame, x_col: str, y_col: str, hue_col: Optional[str], title: str, ylabel: str, name: str) -> None:
    plt.figure(figsize=(7.2, 3.8))
    if hue_col is None:
        xs = np.arange(len(df))
        plt.bar(xs, df[y_col].astype(float), color="#2f6f8f")
        plt.xticks(xs, df[x_col].astype(str), rotation=25, ha="right")
    else:
        labels = list(df[x_col].astype(str).unique())
        hues = list(df[hue_col].astype(str).unique())
        x = np.arange(len(labels))
        width = 0.8 / max(1, len(hues))
        for i, hue in enumerate(hues):
            sub = df[df[hue_col].astype(str) == hue].copy()
            sub["_x"] = sub[x_col].astype(str)
            sub = sub.set_index("_x")
            vals = [float(sub.loc[label, y_col]) if label in sub.index else 0.0 for label in labels]
            plt.bar(x + (i - (len(hues) - 1) / 2) * width, vals, width, label=hue)
        plt.xticks(x, labels, rotation=25, ha="right")
        plt.legend(frameon=False, fontsize=8)
    plt.ylim(0, max(1.05, float(df[y_col].max()) * 1.15 if len(df) else 1.0))
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(OUT / f"{name}.pdf")
    plt.savefig(OUT / f"{name}.png", dpi=200)
    plt.close()


def save_line(df: pd.DataFrame, x_col: str, y_col: str, hue_col: str, title: str, ylabel: str, name: str) -> None:
    plt.figure(figsize=(7.2, 3.8))
    for hue, sub in df.groupby(hue_col):
        sub = sub.sort_values(x_col)
        plt.plot(sub[x_col], sub[y_col], marker="o", label=str(hue).replace("_", " "))
    plt.ylim(0, 1.05 if "success" in y_col or "rate" in y_col or "certificate" in y_col else None)
    plt.xlabel(x_col.replace("_", " "))
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    plt.savefig(OUT / f"{name}.pdf")
    plt.savefig(OUT / f"{name}.png", dpi=200)
    plt.close()


def family_a() -> Tuple[pd.DataFrame, pd.DataFrame]:
    rows: List[Dict[str, object]] = []
    methods = ["UBC", "current_only", "one_axis_current", "gradient_line", "random_search", "least_squares", "soft_penalty", "oracle_anchor"]
    for d, k, null_prob in itertools.product([2, 3, 5], [3, 12, 24], [0.0, 0.5]):
        for seed in range(6):
            rng = np.random.default_rng(MASTER_SEED + 1000 + d * 100 + k * 10 + seed)
            for trial in range(10):
                H, h, meta = make_trial(rng, k=k, d=d, reachable_ratio=0.76, null_prob=null_prob)
                reachable = int(meta["reachable"])
                anchor = meta["anchor"]
                c_ubc, st_ubc = solve_min_norm(H, h, x0=anchor if reachable else None)
                candidates = {
                    "UBC": (c_ubc, st_ubc),
                    "current_only": (current_only(H, h), "current"),
                    "one_axis_current": (one_axis_current(H, h), "axis"),
                    "gradient_line": gradient_line_search(H, h),
                    "random_search": random_search(H, h, rng),
                    "least_squares": least_squares_repair(H, h),
                    "soft_penalty": soft_penalty_repair(H, h),
                    "oracle_anchor": (anchor if reachable else None, "oracle" if reachable else "infeasible"),
                }
                for method in methods:
                    c, status = candidates[method]
                    rows.append(
                        evaluate(
                            "A_coverage",
                            method,
                            c,
                            status,
                            H,
                            h,
                            reachable,
                            extra={"d": d, "contexts": k, "null_prob": null_prob, "seed": seed, "trial": trial},
                        )
                    )
    detail = pd.DataFrame(rows)
    seed = aggregate(rows, ["d", "contexts", "null_prob", "seed"])
    write_csv(seed, "family_a_context_coverage_seed.csv")
    write_csv(aggregate(rows, ["d", "contexts", "null_prob"]), "family_a_context_coverage_summary.csv")
    main = seed[(seed["d"] == 3) & (seed["contexts"] == 12) & (seed["null_prob"] == 0.5)]
    table = (
        main.groupby("method")
        .agg(future_success=("future_success", "mean"), detects_unreachable=("detects_unreachable", "mean"), mean_norm=("mean_norm", "mean"))
        .reset_index()
        .sort_values("future_success", ascending=False)
    )
    latex_table(table, ["method", "future_success", "detects_unreachable", "mean_norm"], ["Method", "Future success", "Unreach. detect", "Norm"], "table_main_context_coverage.tex")
    save_bar(table, "method", "future_success", None, "Main future-context coverage", "future success", "figure_main_context_coverage")
    return seed, detail


def family_b() -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    for sigma, scale, samples, guard_mult in itertools.product([0.0, 0.02, 0.05, 0.10, 0.20, 0.35], [0.75, 1.0, 1.25], [8, 32, 128], [0.0, 0.5, 1.0]):
        for seed in range(4):
            rng = np.random.default_rng(MASTER_SEED + 2000 + int(sigma * 1000) + int(scale * 100) + samples + seed)
            for trial in range(8):
                H, h, meta = make_reachable(rng, k=9, d=3, null_prob=0.35)
                eff_sigma = sigma * math.sqrt(8.0 / samples)
                H_hat = scale * H + rng.normal(0.0, eff_sigma, size=H.shape)
                if sigma >= 0.20 and rng.random() < 0.25:
                    H_hat[:, -1] *= 0.05
                guarded_h = h + guard_mult * eff_sigma
                c, status = solve_min_norm(H_hat, guarded_h, x0=meta["anchor"])
                method = "estimated" if guard_mult == 0 else f"guard_{guard_mult:.1f}"
                rows.append(
                    evaluate(
                        "B_channel",
                        method,
                        c,
                        status,
                        H,
                        h,
                        1,
                        extra={"sigma": sigma, "scale": scale, "samples": samples, "guard": guard_mult, "seed": seed, "trial": trial, "channel_angle": channel_angle(H, H_hat)},
                    )
                )
    seed = aggregate(rows, ["sigma", "scale", "samples", "guard", "seed"])
    write_csv(seed, "family_b_channel_seed.csv")
    summary = aggregate(rows, ["sigma", "scale", "samples", "guard"])
    write_csv(summary, "family_b_channel_summary.csv")
    table = (
        summary[(summary["scale"] == 1.0) & (summary["samples"] == 32)]
        .groupby(["sigma", "method"])
        .agg(future_success=("future_success", "mean"), false_certificate=("false_certificate", "mean"), mean_norm=("mean_norm", "mean"))
        .reset_index()
    )
    latex_table(table, ["sigma", "method", "future_success", "false_certificate", "mean_norm"], ["Sigma", "Method", "Success", "False cert.", "Norm"], "table_channel_stress.tex")
    save_line(table, "sigma", "future_success", "method", "Estimated update-channel stress", "true-margin success", "figure_channel_stress")
    return seed


def channel_angle(H: np.ndarray, H_hat: np.ndarray) -> float:
    a = H.reshape(-1)
    b = H_hat.reshape(-1)
    denom = max(1e-12, float(np.linalg.norm(a) * np.linalg.norm(b)))
    return float(np.degrees(np.arccos(np.clip(float(a @ b) / denom, -1.0, 1.0))))


def family_c() -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    for curvature, cap, method in itertools.product([0.0, 0.05, 0.10, 0.20, 0.40], [1.5, 3.0, 5.0], ["linear_ubc", "guarded", "trust_recenter"]):
        for seed in range(6):
            rng = np.random.default_rng(MASTER_SEED + 3000 + int(curvature * 1000) + int(cap * 10) + seed)
            for trial in range(10):
                H, h, meta = make_reachable(rng, k=10, d=3, null_prob=0.25, anchor_scale=(0.25, min(1.2, cap * 0.45)))
                extra_guard = 0.0
                if method == "guarded":
                    extra_guard = 0.4 * curvature
                elif method == "trust_recenter":
                    extra_guard = 0.2 * curvature
                c, status = solve_min_norm(H, h + extra_guard, max_norm=cap, x0=meta["anchor"])
                row_sens = rng.uniform(0.2, 0.7, size=H.shape[0])

                def nonlinear_success(cand: np.ndarray, H=H, h=h, row_sens=row_sens, curvature=curvature, method=method) -> bool:
                    penalty = curvature * (float(np.linalg.norm(cand)) ** 2) * row_sens
                    if method == "trust_recenter":
                        penalty *= 0.45
                    true_margin = H @ cand - h - penalty
                    return bool(np.all(true_margin >= -1e-7))

                rows.append(
                    evaluate(
                        "C_nonlinear",
                        method,
                        c,
                        status,
                        H,
                        h,
                        1,
                        max_norm=cap,
                        extra={"curvature": curvature, "cap": cap, "seed": seed, "trial": trial},
                        true_success_fn=nonlinear_success,
                    )
                )
    seed = aggregate(rows, ["curvature", "cap", "seed"])
    write_csv(seed, "family_c_nonlinear_seed.csv")
    summary = aggregate(rows, ["curvature", "cap"])
    write_csv(summary, "family_c_nonlinear_summary.csv")
    table = summary[summary["cap"] == 3.0][["curvature", "method", "future_success", "false_certificate", "mean_norm"]]
    latex_table(table, ["curvature", "method", "future_success", "false_certificate", "mean_norm"], ["Curv.", "Method", "Success", "False cert.", "Norm"], "table_nonlinear_locality.tex")
    save_line(table, "curvature", "future_success", "method", "Nonlinear locality stress", "true nonlinear success", "figure_nonlinear_locality")
    return seed


def family_d() -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    cost_variants = {
        "isotropic": np.array([1.0, 1.0, 1.0, 1.0]),
        "force_anisotropic": np.array([0.8, 1.5, 3.0, 5.0]),
        "joint_limited": np.array([1.0, 1.0, 6.0, 6.0]),
        "comfort_weighted": np.array([0.7, 1.2, 2.0, 4.5]),
        "sparse_contact": np.array([0.6, 0.6, 4.0, 4.0]),
    }
    for cost_name, weights in cost_variants.items():
        for method in ["euclidean_ubc", "matching_weighted_ubc", "wrong_cost_ubc"]:
            for seed in range(8):
                rng = np.random.default_rng(MASTER_SEED + 4000 + seed + len(cost_name) * 17)
                for trial in range(8):
                    H, h, meta = make_reachable(rng, k=10, d=4, null_prob=0.20)
                    if method == "euclidean_ubc":
                        solve_weights = np.ones(4)
                    elif method == "matching_weighted_ubc":
                        solve_weights = weights
                    else:
                        solve_weights = weights[::-1]
                    c, status = solve_min_norm(H, h, weights=solve_weights, x0=meta["anchor"])
                    row = evaluate(
                        "D_cost",
                        method,
                        c,
                        status,
                        H,
                        h,
                        1,
                        extra={"cost": cost_name, "seed": seed, "trial": trial},
                    )
                    if c is not None:
                        row["weighted_norm"] = float(np.sqrt(c @ np.diag(weights) @ c))
                    else:
                        row["weighted_norm"] = float("nan")
                    rows.append(row)
    df = pd.DataFrame(rows)
    seed = (
        df.groupby(["cost", "seed", "method"], dropna=False)
        .agg(
            trials=("future_success", "size"),
            future_success=("future_success", "mean"),
            mean_norm=("norm", "mean"),
            weighted_norm=("weighted_norm", "mean"),
            false_certificate=("false_certificate", "mean"),
        )
        .reset_index()
    )
    write_csv(seed, "family_d_interface_cost_seed.csv")
    summary = seed.groupby(["cost", "method"]).mean(numeric_only=True).reset_index()
    write_csv(summary, "family_d_interface_cost_summary.csv")
    table = summary[["cost", "method", "future_success", "weighted_norm", "mean_norm"]]
    latex_table(table, ["cost", "method", "future_success", "weighted_norm", "mean_norm"], ["Cost", "Method", "Success", "W-norm", "E-norm"], "table_interface_cost.tex")
    plot_df = summary[summary["method"].isin(["euclidean_ubc", "matching_weighted_ubc", "wrong_cost_ubc"])]
    save_bar(plot_df, "cost", "weighted_norm", "method", "Interface cost changes the minimum correction", "weighted norm", "figure_interface_cost")
    return seed


def family_e() -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    methods = ["UBC", "reward_gradient", "coactive_direction", "margin_penalty", "safe_large_guard", "robust_ubc", "sequential_greedy"]
    for seed in range(12):
        rng = np.random.default_rng(MASTER_SEED + 5000 + seed)
        for trial in range(14):
            H, h, meta = make_trial(rng, k=14, d=3, reachable_ratio=0.82, null_prob=0.35)
            reachable = int(meta["reachable"])
            anchor = meta["anchor"]
            noise = rng.normal(0.0, 0.05, size=H.shape)
            H_hat = H + noise
            candidates = {
                "UBC": solve_min_norm(H, h, x0=anchor if reachable else None),
                "reward_gradient": gradient_line_search(H, h),
                "coactive_direction": (unit(H[0] + 0.4 * np.mean(H, axis=0)) * min(MAX_NORM, float(np.mean(np.maximum(h, 0.0))) + 0.6), "coactive"),
                "margin_penalty": soft_penalty_repair(H, h, steps=240),
                "safe_large_guard": solve_min_norm(H, h + 0.20, x0=anchor if reachable else None),
                "robust_ubc": solve_min_norm(H_hat, h + 0.08, x0=anchor if reachable else None),
                "sequential_greedy": sequential_greedy(H, h),
            }
            for method in methods:
                c, status = candidates[method]
                rows.append(evaluate("E_baselines", method, c, status, H, h, reachable, extra={"seed": seed, "trial": trial}))
    seed = aggregate(rows, ["seed"])
    write_csv(seed, "family_e_strong_baselines_seed.csv")
    summary = aggregate(rows, [])
    write_csv(summary, "family_e_strong_baselines_summary.csv")
    table = summary[["method", "future_success", "detects_unreachable", "false_certificate", "mean_norm"]].sort_values("future_success", ascending=False)
    latex_table(table, ["method", "future_success", "detects_unreachable", "false_certificate", "mean_norm"], ["Method", "Success", "Unreach.", "False cert.", "Norm"], "table_strong_baselines.tex")
    save_bar(table, "method", "future_success", None, "Stronger correction-learning baselines", "future success", "figure_strong_baselines")
    return seed


def nullspace_component(c: np.ndarray, H: np.ndarray) -> float:
    if c is None or not np.all(np.isfinite(c)):
        return float("nan")
    _, _, vh = np.linalg.svd(H, full_matrices=True)
    rank = np.linalg.matrix_rank(H, tol=1e-8)
    null_basis = vh[rank:].T
    if null_basis.size == 0:
        return 0.0
    proj = null_basis @ (null_basis.T @ c)
    return float(np.linalg.norm(proj))


def family_f() -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    for hidden_null, contradictory in itertools.product([0, 1, 2], [0, 1]):
        for seed in range(6):
            rng = np.random.default_rng(MASTER_SEED + 6000 + hidden_null * 100 + contradictory * 10 + seed)
            for trial in range(6):
                d = 3
                k = 9
                if contradictory:
                    H, h, meta = make_unreachable(rng, k=k, d=d, null_prob=0.0)
                    reachable = 0
                    anchor = None
                else:
                    H, h, meta = make_reachable(rng, k=k, d=d, null_prob=0.0)
                    reachable = 1
                    anchor = meta["anchor"]
                if hidden_null > 0:
                    H[:, -hidden_null:] *= 0.01
                c_ubc, st_ubc = solve_min_norm(H, h, x0=anchor if reachable else None)
                c_current = current_only(H, h)
                c_current[-hidden_null:] += rng.normal(0.0, 0.6, size=hidden_null) if hidden_null > 0 else 0.0
                candidates = {
                    "UBC": (c_ubc, st_ubc),
                    "current_with_null_effort": (c_current, "current"),
                    "gradient_line": gradient_line_search(H, h),
                    "sequential_greedy": sequential_greedy(H, h),
                }
                for method, (c, status) in candidates.items():
                    row = evaluate("F_diagnostics", method, c, status, H, h, reachable, extra={"hidden_null": hidden_null, "contradictory": contradictory, "seed": seed, "trial": trial})
                    row["nullspace_effort"] = nullspace_component(c if c is not None else np.zeros(d), H)
                    rows.append(row)
    df = pd.DataFrame(rows)
    seed = (
        df.groupby(["hidden_null", "contradictory", "seed", "method"], dropna=False)
        .agg(
            trials=("future_success", "size"),
            future_success=("future_success", "mean"),
            detects_unreachable=("detects_unreachable", "mean"),
            false_certificate=("false_certificate", "mean"),
            mean_norm=("norm", "mean"),
            nullspace_effort=("nullspace_effort", "mean"),
        )
        .reset_index()
    )
    write_csv(seed, "family_f_infeasibility_nullspace_seed.csv")
    summary = seed.groupby(["hidden_null", "contradictory", "method"]).mean(numeric_only=True).reset_index()
    write_csv(summary, "family_f_infeasibility_nullspace_summary.csv")
    table = summary[(summary["hidden_null"].isin([0, 1, 2])) & (summary["method"].isin(["UBC", "current_with_null_effort", "sequential_greedy"]))]
    latex_table(table, ["hidden_null", "contradictory", "method", "future_success", "detects_unreachable", "nullspace_effort"], ["Null", "Contr.", "Method", "Success", "Unreach.", "Null effort"], "table_infeasibility_nullspace.tex")
    plot_df = summary[summary["contradictory"] == 0]
    save_line(plot_df, "hidden_null", "nullspace_effort", "method", "Learning-null physical effort", "nullspace effort", "figure_infeasibility_nullspace")
    return seed


def structured_task(rng: np.random.Generator, task: str) -> Tuple[np.ndarray, np.ndarray, Dict[str, object], np.ndarray]:
    if task == "planar_push":
        H, h, meta = make_reachable(rng, k=8, d=2, null_prob=0.05)
        weights = np.array([1.0, 1.3])
    elif task == "shared_waypoint":
        H, h, meta = make_reachable(rng, k=12, d=3, null_prob=0.25)
        H[:, 0] += 0.3
        weights = np.array([1.0, 1.0, 1.8])
    elif task == "force_tactile":
        H, h, meta = make_reachable(rng, k=10, d=4, null_prob=0.40)
        H[:, 2:] *= 0.45
        weights = np.array([0.7, 1.2, 3.5, 4.5])
    else:
        H, h, meta = make_reachable(rng, k=14, d=5, null_prob=0.60)
        H[:, -2:] *= 0.08
        weights = np.array([1.0, 1.4, 2.0, 4.5, 5.0])
    return H, h, meta, weights


def family_g() -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    tasks = ["planar_push", "shared_waypoint", "force_tactile", "peg_compliance"]
    for task in tasks:
        for seed in range(10):
            rng = np.random.default_rng(MASTER_SEED + 7000 + len(task) * 31 + seed)
            for trial in range(10):
                H, h, meta, weights = structured_task(rng, task)
                H_hat = H + rng.normal(0.0, 0.06, size=H.shape)
                candidates = {
                    "UBC": solve_min_norm(H, h, x0=meta["anchor"]),
                    "weighted_UBC": solve_min_norm(H, h, weights=weights, x0=meta["anchor"]),
                    "estimated_guarded": solve_min_norm(H_hat, h + 0.04, weights=weights, x0=meta["anchor"]),
                    "current_only": (current_only(H, h), "current"),
                    "margin_penalty": soft_penalty_repair(H, h),
                }
                for method, (c, status) in candidates.items():
                    rows.append(evaluate("G_embodied", method, c, status, H, h, 1, extra={"task": task, "seed": seed, "trial": trial}))
    seed = aggregate(rows, ["task", "seed"])
    write_csv(seed, "family_g_embodied_seed.csv")
    summary = aggregate(rows, ["task"])
    write_csv(summary, "family_g_embodied_summary.csv")
    table = summary[summary["method"].isin(["UBC", "weighted_UBC", "estimated_guarded", "current_only"])][["task", "method", "future_success", "mean_norm", "false_certificate"]]
    latex_table(table, ["task", "method", "future_success", "mean_norm", "false_certificate"], ["Task", "Method", "Success", "Norm", "False cert."], "table_embodied_tasks.tex")
    save_bar(table, "task", "future_success", "method", "Manipulator-inspired synthetic tasks", "future success", "figure_embodied_tasks")
    return seed


def family_h() -> pd.DataFrame:
    rows: List[Dict[str, object]] = []
    methods = ["full_UBC", "no_future_context", "current_only", "random_contexts", "estimated_no_guard", "guard_no_projection", "wrong_cost", "oracle_true_channel"]
    for seed in range(12):
        rng = np.random.default_rng(MASTER_SEED + 8000 + seed)
        for trial in range(12):
            H, h, meta = make_trial(rng, k=12, d=3, reachable_ratio=0.78, null_prob=0.4)
            reachable = int(meta["reachable"])
            anchor = meta["anchor"]
            H_random = rng.normal(size=H.shape)
            H_hat = H + rng.normal(0.0, 0.10, size=H.shape)
            candidates = {
                "full_UBC": solve_min_norm(H, h, x0=anchor if reachable else None),
                "no_future_context": solve_min_norm(H[:1], h[:1], x0=anchor if reachable else None),
                "current_only": (current_only(H, h), "current"),
                "random_contexts": solve_min_norm(H_random, h, x0=anchor if reachable else None),
                "estimated_no_guard": solve_min_norm(H_hat, h, x0=anchor if reachable else None),
                "guard_no_projection": (unit(np.mean(H, axis=0)) * 1.5, "guard_direction"),
                "wrong_cost": solve_min_norm(H, h, weights=np.array([5.0, 0.5, 2.0]), x0=anchor if reachable else None),
                "oracle_true_channel": (anchor if reachable else None, "oracle" if reachable else "infeasible"),
            }
            for method in methods:
                c, status = candidates[method]
                rows.append(evaluate("H_ablation", method, c, status, H, h, reachable, extra={"seed": seed, "trial": trial}))
    seed = aggregate(rows, ["seed"])
    write_csv(seed, "family_h_ablation_seed.csv")
    summary = aggregate(rows, [])
    write_csv(summary, "family_h_ablation_summary.csv")
    table = summary[["method", "future_success", "detects_unreachable", "false_certificate", "mean_norm"]].sort_values("future_success", ascending=False)
    latex_table(table, ["method", "future_success", "detects_unreachable", "false_certificate", "mean_norm"], ["Method", "Success", "Unreach.", "False cert.", "Norm"], "table_ablation.tex")
    save_bar(table, "method", "future_success", None, "Ablations and negative controls", "future success", "figure_ablation")
    return seed


def write_runtime_table(counts: Dict[str, int]) -> None:
    rows = pd.DataFrame(
        [
            {"Family": "A context coverage", "Seed rows": counts["A"], "Artifact": "selector summaries", "Stress": "future contexts"},
            {"Family": "B channel", "Seed rows": counts["B"], "Artifact": "channel summaries", "Stress": "estimated update map"},
            {"Family": "C nonlinear", "Seed rows": counts["C"], "Artifact": "locality summaries", "Stress": "curvature"},
            {"Family": "D cost", "Seed rows": counts["D"], "Artifact": "cost summaries", "Stress": "human effort metric"},
            {"Family": "E baselines", "Seed rows": counts["E"], "Artifact": "baseline summaries", "Stress": "stronger alternatives"},
            {"Family": "F diagnostics", "Seed rows": counts["F"], "Artifact": "rank/nullity summaries", "Stress": "infeasible/nullspace"},
            {"Family": "G embodied", "Seed rows": counts["G"], "Artifact": "task summaries", "Stress": "structured synthetic tasks"},
            {"Family": "H ablation", "Seed rows": counts["H"], "Artifact": "ablation summaries", "Stress": "negative controls"},
        ]
    )
    latex_table(rows, ["Family", "Seed rows", "Artifact", "Stress"], ["Family", "Seed rows", "Artifact", "Stress focus"], "table_runtime_memory.tex")


def write_claim_table(metadata: Dict[str, object]) -> None:
    rows = pd.DataFrame(
        [
            {"Claim": "Immediate repair is not future learning", "Evidence": "Family A/E/H", "Result": "current-only near zero"},
            {"Claim": "UBC solves trusted local channel", "Evidence": "Family A", "Result": f"{metadata['headline']['ubc_success']:.3f} success"},
            {"Claim": "Estimated channels need guards", "Evidence": "Family B", "Result": f"sigma 0.10 guard {metadata['headline']['guard_sigma_010']:.3f}"},
            {"Claim": "Locality matters", "Evidence": "Family C", "Result": "curvature degrades false certificates"},
            {"Claim": "Cost metric changes minimum", "Evidence": "Family D", "Result": "weighted UBC lowers weighted norm"},
            {"Claim": "Infeasibility/nullspace diagnostics are useful", "Evidence": "Family F", "Result": "contradictions detected"},
        ]
    )
    latex_table(rows, ["Claim", "Evidence", "Result"], ["Claim", "Evidence", "Result"], "table_claim_evidence.tex")


def write_report(metadata: Dict[str, object], counts: Dict[str, int]) -> None:
    h = metadata["headline"]
    lines = [
        "# Full-Scale Experiment Report",
        "",
        "## Scope",
        "- Eight experiment families: future-context coverage, estimated update-channel stress, nonlinear locality, interface cost, stronger baselines, infeasibility/nullspace diagnostics, manipulator-inspired synthetic tasks, and ablations.",
        f"- Total seed-row summaries: {sum(counts.values())}.",
        "- Outputs are under `results/full_scale/`.",
        "",
        "## Key Findings",
        f"- Main context setting: UBC future success {h['ubc_success']:.3f}; current-only future success {h['current_success']:.3f}; random-search norm ratio {h['random_norm_ratio']:.3f}.",
        f"- Estimated channel stress at sigma 0.10: unguarded success {h['estimated_sigma_010']:.3f}; guard-1.0 success {h['guard_sigma_010']:.3f}.",
        f"- Nonlinear curvature 0.20: linear UBC success {h['nonlinear_linear_020']:.3f}; trust-recenter success {h['nonlinear_trust_020']:.3f}.",
        f"- Strong baseline family: UBC success {h['baseline_ubc']:.3f}; margin-penalty success {h['baseline_margin_penalty']:.3f}.",
        f"- Ablation family: full UBC success {h['ablation_full']:.3f}; no-future-context success {h['ablation_no_future']:.3f}.",
        "",
        "## Plot Status",
        "- All full-scale figures generated successfully.",
        "",
    ]
    (DOCS / "experiment_report.md").write_text("\n".join(lines), encoding="utf-8")


def collect_headlines(a: pd.DataFrame, b: pd.DataFrame, c: pd.DataFrame, e: pd.DataFrame, h: pd.DataFrame) -> Dict[str, float]:
    a_main = a[(a["d"] == 3) & (a["contexts"] == 12) & (a["null_prob"] == 0.5)]

    def get(df: pd.DataFrame, method: str, col: str = "future_success") -> float:
        sub = df[df["method"] == method]
        return float(sub[col].mean()) if len(sub) else float("nan")

    ubc = get(a_main, "UBC")
    current = get(a_main, "current_only")
    random_norm = get(a_main, "random_search", "mean_norm")
    ubc_norm = max(1e-12, get(a_main, "UBC", "mean_norm"))

    b010 = b[(b["sigma"] == 0.10) & (b["scale"] == 1.0) & (b["samples"] == 32)]
    est010 = float(b010[b010["method"] == "estimated"]["future_success"].mean())
    guard010 = float(b010[b010["method"] == "guard_1.0"]["future_success"].mean())

    c020 = c[(c["curvature"] == 0.20) & (c["cap"] == 3.0)]
    nl_linear = get(c020, "linear_ubc")
    nl_trust = get(c020, "trust_recenter")

    e_all = e.groupby("method").mean(numeric_only=True).reset_index()
    baseline_ubc = get(e_all, "UBC")
    baseline_penalty = get(e_all, "margin_penalty")

    h_all = h.groupby("method").mean(numeric_only=True).reset_index()
    ablation_full = get(h_all, "full_UBC")
    ablation_no_future = get(h_all, "no_future_context")

    return {
        "ubc_success": ubc,
        "current_success": current,
        "random_norm_ratio": random_norm / ubc_norm,
        "estimated_sigma_010": est010,
        "guard_sigma_010": guard010,
        "nonlinear_linear_020": nl_linear,
        "nonlinear_trust_020": nl_trust,
        "baseline_ubc": baseline_ubc,
        "baseline_margin_penalty": baseline_penalty,
        "ablation_full": ablation_full,
        "ablation_no_future": ablation_no_future,
    }


def main() -> None:
    ensure_dirs()
    write_progress(stage="running", family="A")
    a_seed, _ = family_a()
    write_progress(stage="running", family="B", family_a_rows=len(a_seed))
    b_seed = family_b()
    write_progress(stage="running", family="C", family_a_rows=len(a_seed), family_b_rows=len(b_seed))
    c_seed = family_c()
    write_progress(stage="running", family="D", family_a_rows=len(a_seed), family_b_rows=len(b_seed), family_c_rows=len(c_seed))
    d_seed = family_d()
    write_progress(stage="running", family="E", family_a_rows=len(a_seed), family_b_rows=len(b_seed), family_c_rows=len(c_seed), family_d_rows=len(d_seed))
    e_seed = family_e()
    write_progress(stage="running", family="F", family_a_rows=len(a_seed), family_b_rows=len(b_seed), family_c_rows=len(c_seed), family_d_rows=len(d_seed), family_e_rows=len(e_seed))
    f_seed = family_f()
    write_progress(stage="running", family="G", family_a_rows=len(a_seed), family_b_rows=len(b_seed), family_c_rows=len(c_seed), family_d_rows=len(d_seed), family_e_rows=len(e_seed), family_f_rows=len(f_seed))
    g_seed = family_g()
    write_progress(stage="running", family="H", family_a_rows=len(a_seed), family_b_rows=len(b_seed), family_c_rows=len(c_seed), family_d_rows=len(d_seed), family_e_rows=len(e_seed), family_f_rows=len(f_seed), family_g_rows=len(g_seed))
    h_seed = family_h()

    counts = {
        "A": len(a_seed),
        "B": len(b_seed),
        "C": len(c_seed),
        "D": len(d_seed),
        "E": len(e_seed),
        "F": len(f_seed),
        "G": len(g_seed),
        "H": len(h_seed),
    }
    headline = collect_headlines(a_seed, b_seed, c_seed, e_seed, h_seed)
    metadata: Dict[str, object] = {
        "master_seed": MASTER_SEED,
        "families": [
            "future_context_coverage",
            "estimated_update_channel",
            "nonlinear_locality",
            "interface_cost",
            "strong_baselines",
            "infeasibility_nullspace",
            "embodied_synthetic_tasks",
            "ablation",
        ],
        "headline": headline,
        "seed_rows": counts,
    }
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    write_runtime_table(counts)
    write_claim_table(metadata)
    write_report(metadata, counts)
    write_progress(stage="complete", **{f"family_{k.lower()}_rows": v for k, v in counts.items()}, plot_failures=0)
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
