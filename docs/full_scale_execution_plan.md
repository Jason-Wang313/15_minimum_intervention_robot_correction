# Paper 15 Full-Scale Execution Plan

Paper: Minimum Effective Corrections for Future Robot Behavior
Repository: `15_minimum_intervention_robot_correction`
Date: 2026-06-14

## Current Claim

The smallest useful physical correction is not necessarily the smallest correction that fixes the current motion. It is the minimum physical effort whose image through the robot learner's update channel crosses future-behavior decision boundaries. Update-Boundary Correction (UBC) solves the local minimum-norm halfspace problem, reports unreachable future-behavior requests, and exposes correction directions that are physically visible but learning-null.

## Current State

- Current canonical PDF is 5 pages and stale under the current 25-page standard.
- Existing evidence is a 600-trial abstract correction simulator.
- Trusted-channel result: UBC succeeds on 1.000 of reachable trials and detects 1.000 of unreachable trials.
- Existing baselines: current-only, one-axis current, gradient line search, random search.
- Existing v2 channel-estimation stress: unguarded UBC success drops to 0.330 at channel-noise sigma 0.10 and 0.260 at sigma 0.20; guarded UBC improves to 0.750 and 0.600 at larger norms.
- Existing decision is workshop-only because evidence is abstract, future contexts are designer-picked, and the update channel is assumed locally known.

## Reviewer Attacks To Resolve

1. The result is only an active-set solution of a small linear program.
2. The local affine channel is trusted; noisy or biased update-Jacobian estimates break the certificate.
3. Future contexts are hand-picked, so the guarantee may miss deployment behavior.
4. The simulator is abstract and has no manipulator, tactile, or shared-autonomy structure.
5. Baselines are weak compared with preference, reward-learning, and safe-correction methods.
6. Minimum Euclidean correction may not match human comfort, force limits, or interface anisotropy.
7. Infeasibility may be a model artifact rather than a useful teaching diagnostic.
8. Nullspace directions are asserted but not characterized across ranks, dimensions, and context coverage.
9. The paper does not test nonlinear margins, finite-difference Jacobian estimation, or online validation.
10. Five pages do not give enough proof, algorithmic, reproducibility, and failure-analysis detail.

## Experimental Expansion

Create a RAM-light v3 runner under `experiments/full_scale_minimum_intervention.py`. Keep `scripts/run_experiments.py` as the v2 baseline. Store all v3 outputs under `results/full_scale/`. Run families sequentially and update `results/full_scale/progress.json` after each family.

### Family A: Future-Context Coverage

Purpose: replace the single 600-trial setting with a broad grid over number of future margins, correction dimension, parameter dimension, reachable/unreachable mix, and context redundancy.

Settings:
- Correction dimensions: 2, 3, 5, 8.
- Future contexts: 3, 6, 12, 24, 48.
- Reachable ratio: 0.50, 0.75, 0.90.
- Nullspace probability: 0.0, 0.25, 0.50, 0.75.
- Seeds: at least 30 for headline settings, compact replicated grids elsewhere.

Baselines:
- UBC exact active-set projection.
- Current-only first-margin correction.
- One-axis current correction.
- Aggregate-gradient line search.
- Random feasible search.
- Least-squares margin repair.
- Soft-penalty QP surrogate.
- Oracle feasible anchor.

Metrics:
- Reachable future success, unreachable detection, mean successful norm, current-margin success, regret to UBC norm, solver status, active-set size, rank, nullspace dimension, and violation margin.

### Family B: Estimated Update-Channel Stress

Purpose: deepen the v2 channel-noise stress into bias, anisotropy, finite samples, and online validation.

Settings:
- Additive channel noise sigma: 0.00, 0.02, 0.05, 0.10, 0.20, 0.35.
- Multiplicative scale bias: 0.50, 0.75, 1.00, 1.25, 1.50.
- Rank-dropping estimation error.
- Finite-difference sample counts: 4, 8, 16, 32, 64, 128.
- Guard margins: 0, 0.25 sigma, 0.5 sigma, 1.0 sigma.

Metrics:
- True-margin success, false certificate rate, conservative rejection rate, successful norm, guard overhead, and estimated/true channel angle.

### Family C: Nonlinear Learner And Locality Radius

Purpose: test how far the local certificate survives when the true update and future margins are nonlinear.

Settings:
- Nonlinear curvature: 0.0, 0.05, 0.10, 0.20, 0.40.
- Correction norm cap: 1, 2, 3, 5.
- Local validation steps: none, one-step recenter, two-step recenter, trust-region shrink.

Metrics:
- True nonlinear success, linear-predicted success, certificate mismatch, recenter improvement, norm overhead, and failure attribution.

### Family D: Interface Cost And Human Effort Models

Purpose: show that "minimum" depends on the physical interface cost, not only Euclidean norm.

Settings:
- Isotropic Euclidean cost.
- Anisotropic force cost.
- Joint-limited cost.
- Comfort-weighted cost.
- Sparse/contact-channel cost.

Metrics:
- Success, weighted correction norm, Euclidean norm, active coordinates, cost-regret to matching-cost oracle, and qualitative direction changes.

### Family E: Stronger Correction-Learning Baselines

Purpose: compare UBC against plausible alternatives, not only toy current-repair baselines.

Baselines:
- Reward-gradient correction.
- Coactive/preference-style update direction.
- Margin-penalty descent.
- Safe intervention with large fixed guard.
- Robust UBC with uncertainty guard.
- Sequential greedy future-context repair.

Metrics:
- Future success, immediate repair, norm, unreachable detection, false-positive certificates, and regret to UBC when the trusted local model is valid.

### Family F: Infeasibility And Nullspace Diagnostics

Purpose: make the diagnostic contribution measurable.

Settings:
- Contradictory future-margin pairs.
- Low-rank correction channels.
- Hidden nullspace dimensions 0 through d-1.
- Future-context sets that either expose or miss the nullspace.

Metrics:
- Infeasibility detection, nullspace effort wasted by baselines, explanatory rank/nullity statistics, and success of context augmentation.

### Family G: Tactile/Manipulator-Inspired Synthetic Tasks

Purpose: add embodied structure without claiming hardware.

Tasks:
- 2D planar pushing correction with future obstacle margins.
- Shared-autonomy waypoint correction with policy-parameter update.
- Force/tactile threshold correction with anisotropic channels.
- Peg-in-hole style compliance correction with nullspace force directions.

Metrics:
- Future policy margin, current trajectory repair, correction norm, channel rank, unreachable diagnosis, and robustness under noisy channel estimates.

### Family H: Ablations And Negative Controls

Purpose: separate the MEC/UBC idea from incidental implementation choices.

Ablations:
- No future contexts.
- Current margin only.
- Random future contexts.
- Estimated channel without guard.
- Guard without update-channel projection.
- UBC without infeasibility certificate.
- UBC with wrong cost metric.
- Oracle true channel.

Metrics:
- Success, false certificate rate, norm, unreachable detection, and claim-specific deltas.

## Figures And Tables

Required figures:
- Future-context coverage curves.
- Channel-noise and guard heatmap.
- Nonlinear locality/trust-region curves.
- Interface-cost direction comparison.
- Strong-baseline comparison.
- Infeasibility/nullspace diagnostic plot.
- Tactile/manipulator-inspired task summary.
- Ablation waterfall.

Required tables:
- Main method comparison.
- Estimated-channel stress table.
- Nonlinear locality table.
- Interface cost table.
- Strong baseline table.
- Infeasibility/nullspace table.
- Embodied task table.
- Runtime/RAM-light table.
- Claim-to-evidence table.

## Manuscript Expansion

Target structure:
- Abstract with v3 full-scale numbers and honest scope.
- Introduction separating immediate correction from future learning.
- Related work boundary against physical correction, preference learning, coactive learning, intervention learning, shared autonomy, and minimum-intervention control.
- Formal definitions of MEC, update channel, future context set, reachable correction request, nullspace correction, and false certificate.
- UBC algorithm with exact active-set projection, weighted-cost extension, guard margins, and receding/local validation variant.
- Theory: projection proof, weighted-norm proof, infeasibility certificate, nullspace result, and channel-error margin bound.
- Experiments across Families A-H.
- Failure analysis: estimated-channel error, nonlinear locality, finite context coverage, wrong cost model, and low-rank interface.
- Limitations: synthetic evidence, no hardware, no high-dimensional learned policy, future contexts chosen by designer, and no guarantee that a human's intended concept is captured.
- Appendices: derivations, pseudocode, parameter grids, artifact schema, baseline fairness, compute/RAM details, self-attacks, deployment roadmap, and final audit.

Page strategy:
- Minimum internal threshold is 25 pages.
- Length must come from real content: expanded experiments, generated figures/tables, proofs, stress tests, baseline descriptions, negative controls, and appendices.

## RAM-Light Execution Strategy

- Use NumPy vectorization and small correction dimensions.
- Store summary rows and selected diagnostic examples, not full per-trial matrices.
- Run families sequentially with progress checkpoints.
- Use CSV summaries, JSON metadata, and compact Matplotlib figures.
- Keep active-set enumeration bounded by correction dimension; use fallback projected/penalty methods only in controlled small settings.
- Avoid multiprocessing and large in-memory trial archives.

## Documentation Updates

Update after the full-scale pass:
- `README.md`
- `child_status.md`
- `docs/claims.md`
- `docs/evidence_summary.md`
- `docs/experiment_rigor_checklist.md`
- `docs/reproducibility_checklist.md`
- `docs/reviewer_attacks.md`
- `docs/hostile_reviewer_response.md`
- `docs/submission_attack_log.md`
- `docs/submission_version_log.md`
- `docs/final_audit.md`
- `docs/submission_readiness_decision.md`
- `docs/novelty_decision.md`
- `docs/novelty_boundary_map.md`

## Acceptance Checklist

Paper 15 is not final until all are true:
- Full-scale runner completes and writes `results/full_scale/progress.json` with stage `complete`.
- Edited Python files pass `python -m py_compile`.
- Figures and tables are regenerated from v3 summaries.
- Manuscript compiles with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Final PDF has at least 25 pages.
- Claims match generated CSVs/tables.
- Limitations explicitly include synthetic evidence, no hardware, no real tactile data, no high-dimensional learned policy, finite future-context coverage, and estimated-channel fragility.
- Canonical PDF is copied to `C:/Users/wangz/Downloads/15.pdf` only after final verification.
- No new Desktop PDF copy is created.
- Local `paper/main.pdf` is removed after final copy.
- Commit is pushed.
- Worktree is clean and `HEAD` matches upstream before moving to Paper 16.
