# Child Status

Stage: parent recovery published

Completed:
- Literature matrix and synthesis artifacts exist, including the 1000-row related-work matrix.
- Experiments were rerun and `experiments/summary.json` supports the UBC evidence table.
- The ICLR-style PDF was built and copied to `C:/Users/wangz/Downloads/15.pdf`.
- The numbered PDF was copied visibly to `C:/Users/wangz/OneDrive/Desktop/15.pdf`.
- Parent recovery refreshed `docs/final_audit.md` with the actual evidence and publication status.
- Parent recovery pushed the repository at commit `6270272`.

Current or recent commands:
- `python scripts/finalize_audit.py --github-url https://github.com/Jason-Wang313/15_minimum_intervention_robot_correction ...`

Failures:
- Child attempts exited 999 after PDF generation during the publish/final-audit phase.
- Semantic Scholar optional 429 remains documented from the literature stage.

Recovery steps:
- Parent recovery is committing and pushing the repository package directly.
- Queue row 15 will be restored to `SUCCESS` now that the push is verified.

Next:
- Patch the batch queue and continue Paper 16 monitoring.

## Submission-hardening v2 terminal status

Checked: 2026-06-13 00:16:16 +01:00

- Added estimated-update-channel stress for noisy `H_hat` evaluated against true future margins.
- Trusted-channel UBC result retained: reachable future success 1.000 and unreachable detection 1.000.
- Unguarded UBC under channel noise: success 0.330 at sigma 0.10 and 0.260 at sigma 0.20.
- Guarded UBC under channel noise: success 0.750 at sigma 0.10 and 0.600 at sigma 0.20, at larger correction norms.
- Rebuilt the manuscript and copied the canonical v2 PDF to `C:/Users/wangz/Downloads/15.pdf` (263,370 bytes).
- Local `paper/main.pdf` was removed after the canonical copy.
- Terminal decision: workshop-only / revise before main-conference submission.
- No new Desktop copy created during v2 hardening.
