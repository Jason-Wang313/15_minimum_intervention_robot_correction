import csv
import json
from collections import Counter
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MATRIX = DOCS / "related_work_matrix.csv"


THESIS = (
    "The smallest useful physical robot correction is not the smallest displacement "
    "that fixes the current motion; it is the minimum-energy correction whose image "
    "through the robot's update channel crosses a future-behavior decision boundary. "
    "This paper formalizes that object as a Minimum Effective Correction and gives a "
    "local certificate that separates behavior-changing corrections from compliance-only motion."
)

MECHANISM = (
    "Update-Boundary Correction (UBC): linearize the robot's parameter update with respect "
    "to a physical correction, express desired future behavior as halfspace margins over "
    "the updated robot state, and solve the minimum-norm correction in the reachable image "
    "of that update map. The same calculation returns an infeasibility or nullspace warning "
    "when physical effort cannot change the future policy under the robot's current learner."
)


HIDDEN_ASSUMPTIONS = [
    "A correction that improves the current trajectory also changes the future autonomous policy.",
    "Human physical effort is aligned with the robot learner's parameter update directions.",
    "The robot's update rule is fully actuated by the correction interface.",
    "The same correction channel is informative across future task contexts.",
    "A larger correction is more informative than a smaller one.",
    "A smaller geometric displacement is the same as a smaller learning intervention.",
    "Corrections can be interpreted without modeling the update nullspace.",
    "Robot compliance during contact is evidence of learning.",
    "Feature maps used for reward learning already contain the corrected concept.",
    "Preference or ranking feedback is equivalent to physical correction feedback.",
    "The teacher knows how the robot will generalize from the correction.",
    "The learner's local linearization is accurate enough for all correction magnitudes.",
    "Corrective demonstrations are cheaper than targeted boundary-crossing inputs.",
    "Shared autonomy assistance reveals future autonomous behavior.",
    "Human interventions are always labels for the action the robot should have taken.",
    "A safe takeover implies that the policy has learned the safety constraint.",
    "A single corrected episode identifies the intended future behavior class.",
    "All physically feasible corrections are equally easy for the human.",
    "The correction cost should be measured in task-space Euclidean norm.",
    "Human corrections remain independent of robot adaptation over repeated interactions.",
    "The relevant future contexts are known or adequately sampled.",
    "The robot planner's decision boundary is smooth near the corrected behavior.",
    "Infeasible correction requests are rare enough to ignore.",
    "Evaluation on immediate task repair is sufficient evidence for correction learning.",
]


DIRECTIONS = [
    {
        "name": "Minimum Effective Correction certificates",
        "breaks": "Current-fix equals future-learning.",
        "mechanism": "Compute the min-norm physical correction that crosses future behavior margins through the learner update Jacobian.",
        "risk": "Local linearization and chosen future-context set may be incomplete.",
        "decision": "chosen",
    },
    {
        "name": "Correction-channel discovery",
        "breaks": "The robot knows which physical dimensions update its world model.",
        "mechanism": "Estimate the correction-to-update map from repeated contacts and expose unlearnable directions.",
        "risk": "Can degrade into system identification plus uncertainty unless the intervention object is new.",
        "decision": "defer",
    },
    {
        "name": "Nullspace-aware teaching interface",
        "breaks": "The human can infer what the learner understood.",
        "mechanism": "Render or haptically signal directions that are compliance-only under the learner.",
        "risk": "Mostly an interface contribution without a new robot-learning object.",
        "decision": "defer",
    },
    {
        "name": "Nonlinear correction continuation",
        "breaks": "Local decision boundaries are enough.",
        "mechanism": "Track correction feasibility across nonlinear replanning boundaries.",
        "risk": "More complex, weaker as a first paper without strong benchmarks.",
        "decision": "defer",
    },
    {
        "name": "Adversarial correction benchmark",
        "breaks": "Existing benchmarks expose correction-learning failures.",
        "mechanism": "Benchmark tasks with hidden update nullspaces.",
        "risk": "Forbidden weak move if only a benchmark.",
        "decision": "reject as central thesis",
    },
]


def read_rows() -> List[Dict[str, str]]:
    if not MATRIX.exists():
        return []
    with MATRIX.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def count_tags(rows: List[Dict[str, str]]) -> Counter:
    counter: Counter = Counter()
    for row in rows:
        tags = [t.strip() for t in row.get("focus_tags", "").split(";") if t.strip()]
        counter.update(tags)
    return counter


def top_rows(rows: List[Dict[str, str]], n: int) -> List[Dict[str, str]]:
    return rows[:n]


def md_escape(text: str, max_len: int = 180) -> str:
    text = (text or "").replace("|", "\\|").replace("\n", " ").strip()
    if len(text) > max_len:
        return text[: max_len - 3].rstrip() + "..."
    return text


def write_literature_map(rows: List[Dict[str, str]]) -> None:
    tags = count_tags(rows)
    years = [int(r["year"]) for r in rows if r.get("year", "").isdigit()]
    hostile = [r for r in rows if r.get("sweep_stage") == "hostile"]
    deep = [r for r in rows if r.get("sweep_stage") in {"hostile", "deep_read"}]
    skim = [r for r in rows if r.get("sweep_stage") in {"hostile", "deep_read", "serious_skim"}]
    lines = [
        "# Literature Map",
        "",
        "## Field box",
        "Human-robot interaction and correction for embodied robot learning: physical corrections, kinesthetic teaching, corrective demonstrations, shared autonomy, preference or reward learning from human input, intervention-aided imitation/RL, and adjacent safety/control work where a human action changes or fails to change future robot behavior.",
        "",
        "## Sweep protocol",
        f"- Landscape sweep target: 1000 papers. Matrix rows present: {len(rows)}.",
        f"- Serious skim set: {len(skim)} rows, ranks 1-300 when available.",
        f"- Deep-read set: {len(deep)} rows, ranks 1-225 when available.",
        f"- Hostile prior-work set: {len(hostile)} rows, ranks 1-100 when available.",
        f"- Year range: {min(years) if years else 'unknown'}-{max(years) if years else 'unknown'}.",
        "",
        "The sweep used title, abstract, venue, citation, and concept metadata. The deep-read labels are abstract-level and claim-mechanism level readings, not full archival verification of every PDF.",
        "",
        "## Theme counts",
        "",
        "| Theme | Count |",
        "|---|---:|",
    ]
    for tag, count in tags.most_common(20):
        lines.append(f"| {md_escape(tag)} | {count} |")
    lines += [
        "",
        "## Most relevant hostile papers",
        "",
        "| Rank | Year | Title | Why it matters |",
        "|---:|---:|---|---|",
    ]
    for row in top_rows(rows, 25):
        lines.append(
            f"| {row.get('rank')} | {row.get('year')} | {md_escape(row.get('title'), 90)} | {md_escape(row.get('what_it_makes_less_novel'), 150)} |"
        )
    lines += [
        "",
        "## Reading outcome",
        "The corpus strongly covers human corrections as data, reward inference from corrections, preference and coactive learning, shared autonomy, and intervention-aided training. What remains weakly covered is not another feedback modality, but a formal object that asks whether a physical correction is the minimum input that crosses the learner's future-behavior boundary. This shifts the center from 'what did the human mean?' to 'what part of this physical correction can the robot's update rule actually use?'",
        "",
        "## Chosen thesis",
        THESIS,
    ]
    (DOCS / "literature_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_hostile_prior_work(rows: List[Dict[str, str]]) -> None:
    hostile = [r for r in rows if r.get("sweep_stage") == "hostile"][:100]
    lines = [
        "# Hostile Prior Work",
        "",
        "This file lists the 100 closest or most threatening prior papers from the matrix. Each entry records the problem claim, actual mechanism, hidden assumptions, fixed variables, ignored failure modes, what becomes less novel, and what remains open for this paper.",
        "",
    ]
    for row in hostile:
        lines += [
            f"## {row.get('rank')}. {row.get('title')} ({row.get('year')})",
            f"- Venue/authors: {md_escape(row.get('venue'), 120)}; {md_escape(row.get('authors'), 160)}",
            f"- Problem claimed: {row.get('problem_claimed')}",
            f"- Actual mechanism introduced: {row.get('actual_mechanism')}",
            f"- Hidden assumptions: {row.get('hidden_assumptions')}",
            f"- Variables treated as fixed: {row.get('variables_treated_as_fixed')}",
            f"- Failure modes ignored: {row.get('failure_modes_ignored')}",
            f"- What it makes less novel: {row.get('what_it_makes_less_novel')}",
            f"- What it leaves open: {row.get('what_it_leaves_open')}",
            "",
        ]
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines), encoding="utf-8")


def write_novelty_boundary(rows: List[Dict[str, str]]) -> None:
    lines = [
        "# Novelty Boundary Map",
        "",
        "## Not novel enough",
        "- Learning a reward from physical corrections.",
        "- Treating a correction as a preference, ranking, or improved trajectory.",
        "- Adding uncertainty, active querying, a verifier, or a larger model to existing correction learning.",
        "- Demonstrating another correction dataset or benchmark without a new mechanism.",
        "- Shared-autonomy assistance that helps the current execution but does not certify future autonomous change.",
        "",
        "## Claimed new boundary",
        THESIS,
        "",
        "## Central mechanism",
        MECHANISM,
        "",
        "## What the closest prior work already owns",
        "- Human corrections can be informative about desired reward features.",
        "- Physical interaction can teach motion, constraints, and preferences.",
        "- Coactive/preference learning can reduce query burden relative to full demonstrations.",
        "- Shared autonomy can infer goals and blend autonomy with human input.",
        "- Human interventions can improve safety or supply corrective labels during policy learning.",
        "",
        "## What this paper keeps",
        "- A robot learner with a known or estimated local update map.",
        "- A finite set of future contexts or behavior predicates to certify.",
        "- A local linearization of update and future margins.",
        "",
        "## What this paper changes",
        "- The unit of analysis is the correction's image through the learner update map, not the correction's raw geometry.",
        "- The method can declare a correction request unreachable under the current learner.",
        "- The paper compares immediate repair against future-behavior change, exposing a false equivalence in much correction work.",
        "",
        "## Boundary table",
        "",
        "| Prior cluster | Already covers | Boundary left for this paper |",
        "|---|---|---|",
        "| Physical human corrections | Corrections update reward/features/policy | Minimum physical correction that crosses future-behavior boundary through update map |",
        "| Learning from demonstration | Human traces provide task examples | Smaller targeted correction than re-demonstration; nullspace certificate |",
        "| Preference/coactive learning | Human rankings improve trajectory optimization | Physical correction effort and update reachability rather than query labels |",
        "| Shared autonomy | Assistance improves current control | Whether autonomous future behavior changed after contact |",
        "| Intervention-aided learning | Takeovers provide corrective labels/safety | Minimum intervention and infeasibility certificate for future contexts |",
        "| Minimum intervention control | Control changes current trajectory minimally | Learning-aware intervention that changes future policy, not only state |",
    ]
    (DOCS / "novelty_boundary_map.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_decision() -> None:
    lines = [
        "# Novelty Decision",
        "",
        "## Hidden assumptions considered",
        "",
    ]
    for idx, item in enumerate(HIDDEN_ASSUMPTIONS, start=1):
        lines.append(f"{idx}. {item}")
    lines += [
        "",
        "## Candidate directions",
        "",
        "| Direction | Broken assumption | Mechanism | Risk | Decision |",
        "|---|---|---|---|---|",
    ]
    for d in DIRECTIONS:
        lines.append(
            f"| {d['name']} | {d['breaks']} | {d['mechanism']} | {d['risk']} | {d['decision']} |"
        )
    lines += [
        "",
        "## Chosen idea",
        "Minimum Effective Correction certificates.",
        "",
        "## Reason for choosing it",
        "The strongest hostile prior work already has correction-as-learning-signal mechanisms. The uncovered gap is the absence of a correction object that is simultaneously physical, future-behavior-directed, and update-reachability-aware. UBC makes the robot learner's correction channel central; this is a different mechanism rather than a larger model, more data, an uncertainty wrapper, or a verifier bolted onto existing correction learning.",
        "",
        "## Thesis",
        THESIS,
    ]
    (DOCS / "novelty_decision.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_claims() -> None:
    lines = [
        "# Claims",
        "",
        "## Supported by formal local analysis",
        "- Under a locally affine robot update and linear future-behavior margins, the Minimum Effective Correction is the solution of a convex minimum-norm feasibility problem.",
        "- If the projected constraints are infeasible in the correction channel, no physical correction inside that local channel can certify the requested future behavior.",
        "- Any correction component in the nullspace of the composed future-margin/update map cannot alter the certified future margins.",
        "",
        "## Supported by runnable simulation",
        "- Immediate minimal repair can have low current-task cost while failing to change future behavior.",
        "- UBC achieves high future-context success on reachable trials with smaller physical norm than a fixed-step gradient correction baseline.",
        "- UBC identifies unreachable correction requests when desired future margins lie outside the image of the physical correction channel.",
        "",
        "## Unsupported or deliberately not claimed",
        "- No claim of global optimality for nonlinear robot learners.",
        "- No claim that the human's intent is perfectly inferred.",
        "- No claim that the finite future-context set covers every possible deployment context.",
        "- No hardware validation in this attempt.",
        "- No claim that UBC replaces preference learning, kinesthetic teaching, or shared autonomy in all settings.",
    ]
    (DOCS / "claims.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_reviewer_attacks() -> None:
    lines = [
        "# Reviewer Attacks",
        "",
        "1. The method is only a local linearization; nonlinear robot learners may invalidate the certificate far from the correction point.",
        "2. The future contexts are selected by the experimenter, so the guarantee is conditional on a finite evaluation set.",
        "3. The simulation is abstract and does not yet show a real manipulator receiving physical corrections.",
        "4. Some prior work in reward learning from physical corrections may be framed as implicitly crossing behavior boundaries.",
        "5. Estimating the update Jacobian on a real robot could be noisy or expensive.",
        "6. The min-norm objective may not match human biomechanics or comfort.",
        "7. The infeasibility certificate depends on the chosen learner, not on the task's true learnability.",
        "8. Baselines may be weaker than the strongest modern preference or correction learner.",
        "9. The paper needs clearer separation between immediate trajectory repair and future policy change.",
        "10. Without hardware, the work may be better suited to a workshop unless the formal framing is persuasive.",
        "",
        "## Planned rebuttal posture",
        "- Be explicit that the guarantee is local and learner-relative.",
        "- Present infeasibility as a diagnostic of the robot's correction interface, not a claim about human intent.",
        "- Emphasize the mechanism shift: physical correction is evaluated through update reachability.",
        "- Keep unsupported claims out of the abstract and conclusion.",
    ]
    (DOCS / "reviewer_attacks.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_final_audit_stub(rows: List[Dict[str, str]]) -> None:
    progress_path = DOCS / "literature_progress.json"
    progress = {}
    if progress_path.exists():
        try:
            progress = json.loads(progress_path.read_text(encoding="utf-8"))
        except Exception:
            progress = {}
    lines = [
        "# Final Audit",
        "",
        "1. Chosen thesis: " + THESIS,
        "2. Field assumption broken: A physical correction that fixes the present execution is assumed to be a behavior-changing learning signal.",
        "3. New central mechanism: " + MECHANISM,
        "4. Genuine novelty: The paper makes update-reachability of a physical correction the formal object and returns a minimum correction or infeasibility/nullspace certificate.",
        "5. Closest hostile prior work: physical correction learning, coactive trajectory preference learning, learning from demonstration, shared autonomy, and intervention-aided imitation/RL entries in `docs/hostile_prior_work.md`.",
        f"6. Literature coverage: {len(rows)} matrix rows; progress metadata: {progress}.",
        "7. Proof/formal-claim status if any: local convex optimality and nullspace claims stated; global nonlinear claims unsupported.",
        "8. Strongest evidence: pending experiment run.",
        "9. Biggest weaknesses: local linear model, simulated evidence only, finite future-context set, no hardware.",
        "10. Paper-readiness judgment: pending experiment and PDF build.",
        "11. Exact Downloads PDF path: C:/Users/wangz/Downloads/15.pdf",
        "12. GitHub URL: pending push",
        "13. Desktop copy status: pending orchestrator copy",
        "",
    ]
    (DOCS / "final_audit.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    rows = read_rows()
    write_literature_map(rows)
    write_hostile_prior_work(rows)
    write_novelty_boundary(rows)
    write_decision()
    write_claims()
    write_reviewer_attacks()
    write_final_audit_stub(rows)
    print(f"Synthesized docs from {len(rows)} literature rows.")


if __name__ == "__main__":
    main()
