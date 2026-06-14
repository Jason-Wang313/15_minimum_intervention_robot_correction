# Minimum Effective Corrections for Future Robot Behavior

This repository contains Paper 15 from the robotics/embodied-intelligence batch.

## Thesis

The smallest useful physical robot correction is not necessarily the smallest displacement that fixes the current motion. It is the minimum-cost correction whose image through the robot learner's update channel crosses specified future-behavior decision boundaries.

## Reproduce

```powershell
python scripts\run_experiments.py
python experiments\full_scale_minimum_intervention.py
cd paper
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final verified PDF is `C:/Users/wangz/Downloads/15.pdf` (25 pages, 414,131 bytes, SHA256 `A3C35CED8E413B92C2DE1C58B54265EB3EBFCE4A46420AE65A23C31EAB2F66B9`).

## Submission-Hardening v3

- Replaced the 5-page v2 artifact with a 25-page full-scale mechanism paper.
- Added `docs/full_scale_execution_plan.md` before substantive v3 edits.
- Added `experiments/full_scale_minimum_intervention.py`.
- Generated eight experiment families and 2,426 seed-row summaries under `results/full_scale/`.
- Main context setting: UBC future success 1.000, current-only future success 0.000, and random-search norm ratio 2.259.
- Estimated-channel stress at sigma 0.10: unguarded success 0.344, guard-1.0 success 0.906.
- Nonlinear curvature 0.20: raw linear UBC success 0.000, trust-recentered success 0.817.
- Decision: ready as a full-scale mechanism/counterexample paper, not as a hardware robot or learned tactile-policy result.

## Key Artifacts

- `docs/full_scale_execution_plan.md`: v3 plan and acceptance checklist.
- `docs/experiment_report.md`: generated full-scale experiment report.
- `experiments/full_scale_minimum_intervention.py`: v3 experiment runner.
- `results/full_scale/`: v3 CSV summaries, figures, tables, metadata, and progress log.
- `paper/main.tex`: anonymous ICLR-style manuscript source.
