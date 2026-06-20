# Submission Version Log

## v1

- Generated initial formal mechanism paper and ICLR-style PDF.
- Published initial repository.

## v2

Checked: 2026-06-13

- Added estimated-update-channel stress.
- Trusted-channel result retained: reachable success 1.000 and unreachable detection 1.000.
- Unguarded UBC under channel noise: success 0.330 at sigma 0.10 and 0.260 at sigma 0.20.
- Guarded UBC under channel noise: success 0.750 at sigma 0.10 and 0.600 at sigma 0.20.
- Decision: workshop-only / revise before main-conference submission.

## v3-link-hardening

Checked: 2026-06-20

- Added explicit VLA-style `\hypersetup` policy for boxed PDF links.
- Rebuilt from `paper/` with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Canonical PDF: `C:/Users/wangz/Downloads/15.pdf` (25 pages, 414,131 bytes).
- SHA256: `DDDB3B1F90A4DB4E4470E531BA21407737A088B5A5A2B313F3FD8244F83E1E1F`.
- Link inventory: 57 annotations on pages `[(1, 14), (2, 34), (4, 2), (5, 1), (6, 2), (14, 1), (15, 1), (17, 2)]`; green = 48, red = 9, cyan = 0; all borders `(0, 0, 1)`.
- Rendered pages 1, 2, 4, 5, 6, 14, 15, and 17 after export and confirmed crisp green citation/URL boxes and red internal-reference boxes.
- Local `paper/main.pdf` removed after the canonical copy.

## v3

Checked: 2026-06-14

- Wrote a paper-specific full-scale execution plan before substantive edits.
- Added `experiments/full_scale_minimum_intervention.py`.
- Generated eight full-scale experiment families under `results/full_scale/`.
- Expanded the manuscript to 25 pages with new experiments, figures, tables, proofs, baseline audits, deployment criteria, and artifact-to-claim audit.
- Main setting: UBC future success 1.000, current-only success 0.000, random-search norm ratio 2.259.
- Estimated-channel sigma 0.10: unguarded success 0.344, guard-1.0 success 0.906.
- Decision: ready as a full-scale mechanism/counterexample paper under the stated claim scope.
