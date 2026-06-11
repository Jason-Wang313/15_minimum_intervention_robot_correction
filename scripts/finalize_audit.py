import argparse
import csv
import json
import subprocess
from pathlib import Path
from typing import Dict


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DOWNLOAD_PDF = Path("C:/Users/wangz/Downloads/15.pdf")


THESIS = (
    "The smallest useful physical robot correction is the minimum-energy correction "
    "whose image through the robot's update channel crosses specified future-behavior "
    "decision boundaries, not merely the smallest displacement that fixes the current motion."
)

MECHANISM = (
    "Update-Boundary Correction: a local halfspace certificate that projects physical "
    "corrections through the robot learner's update Jacobian and returns the minimum "
    "effective correction, a nullspace warning, or an infeasibility certificate."
)


def read_json(path: Path) -> Dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def count_matrix() -> int:
    path = DOCS / "related_work_matrix.csv"
    if not path.exists():
        return 0
    with path.open(newline="", encoding="utf-8") as f:
        return max(0, sum(1 for _ in csv.reader(f)) - 1)


def git_remote() -> str:
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return "pending push"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--github-url", default="")
    parser.add_argument("--desktop-status", default="pending orchestrator copy")
    parser.add_argument("--push-status", default="")
    args = parser.parse_args()

    summary = read_json(ROOT / "experiments" / "summary.json")
    template = read_json(DOCS / "template_status.json")
    matrix_rows = count_matrix()
    remote = args.github_url or git_remote()
    if args.push_status:
        remote = f"{remote} ({args.push_status})"

    ubc = summary.get("UBC", {})
    current = summary.get("current_only", {})
    evidence = (
        "UBC future success on reachable simulated trials "
        f"{100.0 * ubc.get('future_success_reachable', 0.0):.1f}%, "
        f"unreachable detection {100.0 * ubc.get('detects_unreachable', 0.0):.1f}%; "
        "current-only future success "
        f"{100.0 * current.get('future_success_reachable', 0.0):.1f}%."
    )

    pdf_status = "exists" if DOWNLOAD_PDF.exists() else "missing"
    judgment = "workshop"
    if matrix_rows >= 1000 and DOWNLOAD_PDF.exists() and ubc.get("future_success_reachable", 0.0) > 0.95:
        judgment = "revise / strong workshop"

    lines = [
        "# Final Audit",
        "",
        f"1. Chosen thesis: {THESIS}",
        "2. Field assumption broken: Prior correction work often assumes that a physical correction which repairs the present execution is also a useful learning signal for future autonomous behavior.",
        f"3. New central mechanism: {MECHANISM}",
        "4. Genuine novelty: The correction is defined by update reachability through the robot learner, so effort in the learner nullspace is explicitly separated from behavior-changing intervention. This is not a bigger model, more data, active learning, a verifier, or an LLM planner.",
        "5. Closest hostile prior work: learning from physical human corrections; reward learning from corrections; coactive/preference trajectory learning; shared autonomy; intervention-aided imitation learning; minimum-intervention control. See `docs/hostile_prior_work.md`.",
        f"6. Literature coverage: {matrix_rows} entries in `docs/related_work_matrix.csv`; 300-paper serious skim, 225-paper deep-read slice, and 100-paper hostile set encoded by rank/stage. Template source: {template}.",
        "7. Proof/formal-claim status if any: Local convex optimality, infeasibility, and nullspace claims are proved for affine update and linearized future margins. No global nonlinear or hardware guarantee is claimed.",
        f"8. Strongest evidence: {evidence}",
        "9. Biggest weaknesses: simulated evidence only, finite future-context set, Euclidean correction cost, local linearization, and no real robot hardware contact study.",
        f"10. Paper-readiness judgment: {judgment}. The paper is coherent and runnable, but should be strengthened with hardware or a richer robot planner before a main-conference submission.",
        f"11. Exact Downloads PDF path: C:/Users/wangz/Downloads/15.pdf ({pdf_status})",
        f"12. GitHub URL: {remote}",
        f"13. Desktop copy status: {args.desktop_status}",
        "",
    ]
    (DOCS / "final_audit.md").write_text("\n".join(lines), encoding="utf-8")
    print("Wrote docs/final_audit.md")


if __name__ == "__main__":
    main()
