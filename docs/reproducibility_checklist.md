# Reproducibility Checklist

Run from the repository root:

```powershell
python scripts\run_experiments.py
```

Expected artifacts:

- `experiments/episode_results.csv`
- `experiments/summary.json`
- `experiments/channel_noise_stress.csv`
- `experiments/channel_noise_table.tex`
- `figures/success_rates.png`
- `figures/correction_norms.png`
- `docs/evidence_summary.md`

The script uses deterministic NumPy seeds. The optional SciPy fallback in the active-set solver is disabled by default so infeasible local channels return quickly as certificates.
