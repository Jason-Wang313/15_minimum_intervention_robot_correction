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

## v3

Checked: 2026-06-14

- Wrote a paper-specific full-scale execution plan before substantive edits.
- Added `experiments/full_scale_minimum_intervention.py`.
- Generated eight full-scale experiment families under `results/full_scale/`.
- Expanded the manuscript to 25 pages with new experiments, figures, tables, proofs, baseline audits, deployment criteria, and artifact-to-claim audit.
- Main setting: UBC future success 1.000, current-only success 0.000, random-search norm ratio 2.259.
- Estimated-channel sigma 0.10: unguarded success 0.344, guard-1.0 success 0.906.
- Decision: ready as a full-scale mechanism/counterexample paper under the stated claim scope.
