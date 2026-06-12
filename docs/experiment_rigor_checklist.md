# Experiment Rigor Checklist

- Fixed seeds: yes (`15` for the main experiment, `1515` for channel-noise stress).
- Main trials: 600 total, 464 reachable, 136 intentionally unreachable.
- Channel-noise stress: 6 noise levels x 100 reachable trials.
- Main raw output: `experiments/episode_results.csv`.
- Main summary: `experiments/summary.json`.
- V2 stress output: `experiments/channel_noise_stress.csv`.
- V2 manuscript table: `experiments/channel_noise_table.tex`.
- Baselines: current-only, one-axis current, gradient line search, random search, UBC, guarded UBC in stress.
- Remaining empirical gap: no hardware, no learned update Jacobian, no real human-correction interface, and no high-dimensional policy learner.
