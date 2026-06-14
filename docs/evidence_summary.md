# Evidence Summary

The v3 evidence package is synthetic and local. It isolates the paper's mechanism claim: present repair and future learning are different because physical corrections are projected through the robot learner's update channel.

## Original Evidence

- v2 baseline: 600 abstract correction trials.
- Trusted-channel UBC reached 1.000 success on reachable trials and 1.000 unreachable detection.
- v2 estimated-channel stress showed unguarded success dropping under noisy `H_hat`, with guarded variants improving success at larger norm.

## Full-Scale v3 Evidence

- Eight experiment families completed under `results/full_scale/`.
- Total seed-row summaries: 2,426.
- Plot failures: 0.
- Family A context coverage: main UBC future success 1.000, current-only success 0.000, random-search norm ratio 2.259.
- Family B estimated channel: at sigma 0.10, unguarded success 0.344 and guard-1.0 success 0.906.
- Family C nonlinear locality: at curvature 0.20, linear UBC success 0.000 and trust-recentered success 0.817.
- Family D interface cost: matching weighted UBC changes the minimum correction under anisotropic physical costs.
- Family E stronger baselines: UBC success 1.000; margin-penalty success 0.007; safe large guard and robust UBC can match success with higher norms.
- Family F diagnostics: contradictory requests and low-rank channels expose infeasibility and nullspace effort.
- Family G embodied synthetic tasks: planar pushing, shared waypoint, force/tactile, and peg-compliance structures preserve the mechanism pattern without claiming hardware.
- Family H ablations: full UBC success 1.000, no-future-context success 0.008.

## Interpretation

The evidence supports a mechanism paper: UBC identifies minimum effective corrections for a modeled local channel and exposes current-repair failures, false certificates, nullspaces, and infeasibility. It does not support claims about real robot performance, learned Jacobians, human-intent inference, or tactile-policy deployment.
