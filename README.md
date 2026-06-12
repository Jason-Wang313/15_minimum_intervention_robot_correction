# Minimum Effective Corrections for Future Robot Behavior

This repository contains Paper 15 from the robotics/embodied-intelligence batch.

## Thesis

The smallest useful physical robot correction is not necessarily the smallest displacement that fixes the current motion. It is the minimum-energy correction whose image through the robot learner's update channel crosses specified future-behavior decision boundaries.

## Reproduce

```powershell
python scripts/literature_pipeline.py
python scripts/synthesize_docs.py
python scripts/run_experiments.py
python scripts/fetch_iclr_template.py
python scripts/generate_paper.py
```

Build the paper from `paper/` with direct pdfLaTeX/BibTeX passes:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final orchestrated PDF target is `C:/Users/wangz/Downloads/15.pdf`.

## Submission-Hardening v2

- Added estimated-update-channel stress in `experiments/channel_noise_stress.csv`.
- The original 600-trial synthetic result is retained: UBC succeeds on 1.000 of reachable trials and detects 1.000 of unreachable trials under the trusted local channel.
- With noisy channel estimates, unguarded UBC success drops to 0.330 at sigma 0.10 and 0.260 at sigma 0.20.
- A simple guarded variant improves sigma 0.10 success to 0.750 and sigma 0.20 success to 0.600, but it gives up the exact minimum-correction interpretation.
- Decision remains workshop-only until validated with learned update Jacobians, hardware corrections, and richer future-context sets.

## Key artifacts

- `docs/related_work_matrix.csv`: 1000-paper landscape matrix.
- `docs/literature_map.md`: field map and sweep outcome.
- `docs/hostile_prior_work.md`: 100-paper hostile prior-work set.
- `docs/novelty_boundary_map.md`: novelty boundaries.
- `docs/novelty_decision.md`: hidden assumptions and chosen direction.
- `docs/claims.md`: supported and unsupported claims.
- `docs/reviewer_attacks.md`: adversarial review notes.
- `docs/final_audit.md`: final readiness audit.
- `experiments/episode_results.csv`: runnable simulation results.
- `figures/`: generated plots used in the paper.
