# Experiment Rigor Checklist

- Fixed seeds: yes. v3 master seed is 15015.
- RAM-light execution: yes. The runner stores summary CSVs, generated figures, generated tables, metadata, and progress JSON rather than full per-trial matrices.
- v3 runner: `experiments/full_scale_minimum_intervention.py`.
- v3 outputs: `results/full_scale/*.csv`, `results/full_scale/*.pdf`, `results/full_scale/*.png`, `results/full_scale/*.tex`, `results/full_scale/metadata.json`, and `results/full_scale/progress.json`.
- Baselines: UBC, current-only, one-axis current, gradient line search, random search, least-squares repair, soft margin penalty, sequential greedy repair, reward-gradient correction, coactive direction, robust UBC, safe large guard, wrong-cost UBC, random contexts, and oracle true channel.
- Stress axes: future-context count, correction dimension, nullspace probability, estimated-channel noise, scale bias, finite-sample quality, guard margin, nonlinear curvature, correction cap, interface cost metric, contradictory requests, structured task type, and ablations.
- Metrics: reachable future success, unreachable detection, current success, false certificate rate, mean correction norm, min margin, rank, nullspace dimension, weighted norm, and nullspace effort.
- Manuscript artifacts: generated v3 figures and LaTeX tables imported directly into `paper/main.tex`.
- Remaining evidence gap: no hardware, no real tactile data, no high-dimensional learned policy, no user study, and no learned real update Jacobian.
