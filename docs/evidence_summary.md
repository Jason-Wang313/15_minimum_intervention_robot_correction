# Evidence Summary

Trials: 600 total, 464 reachable, 136 intentionally unreachable.

The synthetic embodied-correction environment represents a robot whose physical correction `c` changes future behavior margins through a composed update map `H = A J`, where `J` is the learner's correction-to-parameter channel and `A` maps updated parameters to future behavior margins. The proposed UBC method solves `min ||c||_2` subject to `H c >= h`.

| Method | Future success on reachable | Detects unreachable | Mean norm on successful reachable |
|---|---:|---:|---:|
| UBC | 1.000 | 1.000 | 0.617 |
| current_only | 0.000 | 0.000 | nan |
| one_axis_current | 0.006 | 0.000 | 0.463 |
| gradient_line_search | 0.640 | 1.000 | 1.019 |
| random_search | 1.000 | 1.000 | 1.174 |

## Interpretation
- Current-only corrections usually satisfy the immediate constraint but often fail the future-context set, demonstrating that present repair is not equivalent to future learning.
- UBC succeeds on the reachable local problems because it solves the exact minimum-norm projected halfspace problem.
- Unreachable trials contain contradictory future margins in the physical correction channel; UBC returns an infeasibility certificate rather than pretending a larger correction would help.
- V2 channel-noise stress: when UBC solves with a noisy update channel and is evaluated on the true margins, success drops from 1.000 at sigma 0.00 to 0.330 at sigma 0.10, 0.260 at sigma 0.20, and 0.260 at sigma 0.35.
- A simple guarded variant improves the sigma 0.20 stress to 0.600 but increases mean successful norm to 0.937; the certificate is therefore only as good as the estimated update channel.
- The evidence is simulated and local. It supports the formal mechanism, not a hardware or global nonlinear claim.

Generated artifacts:
- `experiments/episode_results.csv`
- `experiments/summary.json`
- `experiments/channel_noise_stress.csv`
- `experiments/channel_noise_table.tex`
- `figures/success_rates.png`
- `figures/correction_norms.png`
