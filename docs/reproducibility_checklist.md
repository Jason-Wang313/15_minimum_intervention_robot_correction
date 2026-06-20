# Reproducibility Checklist

Run from the repository root:

```powershell
python -m py_compile experiments\full_scale_minimum_intervention.py
python -m py_compile scripts\run_experiments.py
python scripts\run_experiments.py
python experiments\full_scale_minimum_intervention.py
```

Then build from `paper/`:

```powershell
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Expected v3 artifacts:

- `results/full_scale/family_a_context_coverage_seed.csv`
- `results/full_scale/family_b_channel_seed.csv`
- `results/full_scale/family_c_nonlinear_seed.csv`
- `results/full_scale/family_d_interface_cost_seed.csv`
- `results/full_scale/family_e_strong_baselines_seed.csv`
- `results/full_scale/family_f_infeasibility_nullspace_seed.csv`
- `results/full_scale/family_g_embodied_seed.csv`
- `results/full_scale/family_h_ablation_seed.csv`
- `results/full_scale/figure_*.pdf`
- `results/full_scale/table_*.tex`
- `results/full_scale/metadata.json`
- `results/full_scale/progress.json`
- `docs/experiment_report.md`

Expected verification:

- `progress.json` has stage `complete`.
- `metadata.json` records UBC success 1.0, current-only success 0.0, estimated sigma 0.10 success 0.34375, guard sigma 0.10 success 0.90625, and trust-recentered curvature 0.20 success about 0.817.
- Final manuscript builds to 25 pages.
- Log scan has no unresolved citations, undefined references, LaTeX errors, fatal stops, missing files, or overfull boxes.

## Final Export Verification

- Canonical PDF: `C:/Users/wangz/Downloads/15.pdf`
- Pages: 25
- Size: 414,131 bytes
- SHA256: `DDDB3B1F90A4DB4E4470E531BA21407737A088B5A5A2B313F3FD8244F83E1E1F`
- VLA-style boxed-link inventory: 57 annotations on pages `[(1, 14), (2, 34), (4, 2), (5, 1), (6, 2), (14, 1), (15, 1), (17, 2)]`; green = 48, red = 9, cyan = 0; all borders `(0, 0, 1)`.
- Visual render audit: pages 1, 2, 4, 5, 6, 14, 15, and 17 checked after export.
- Local build artifact: `paper/main.pdf` removed after export.
