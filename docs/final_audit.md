# Final Audit

1. Chosen thesis: The smallest useful physical robot correction is the minimum-energy correction whose image through the robot's update channel crosses specified future-behavior decision boundaries, not merely the smallest displacement that fixes the current motion.
2. Field assumption broken: Prior correction work often assumes that a physical correction which repairs the present execution is also a useful learning signal for future autonomous behavior.
3. New central mechanism: Update-Boundary Correction: a local halfspace certificate that projects physical corrections through the robot learner's update Jacobian and returns the minimum effective correction, a nullspace warning, or an infeasibility certificate.
4. Genuine novelty: The correction is defined by update reachability through the robot learner, so effort in the learner nullspace is explicitly separated from behavior-changing intervention. This is not a bigger model, more data, active learning, a verifier, or an LLM planner.
5. Closest hostile prior work: learning from physical human corrections; reward learning from corrections; coactive/preference trajectory learning; shared autonomy; intervention-aided imitation learning; minimum-intervention control. See `docs/hostile_prior_work.md`.
6. Literature coverage: 1000 entries in `docs/related_work_matrix.csv`; 300-paper serious skim, 225-paper deep-read slice, and 100-paper hostile set encoded by rank/stage. Template source: {'official_author_guide': 'https://iclr.cc/Conferences/2026/AuthorGuide', 'template_url': 'https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip', 'downloaded': True, 'extracted': ['iclr2026_conference.bst', 'iclr2026_conference.sty'], 'warnings': []}.
7. Proof/formal-claim status if any: Local convex optimality, infeasibility, and nullspace claims are proved for affine update and linearized future margins. No global nonlinear or hardware guarantee is claimed.
8. Strongest evidence: UBC future success on reachable simulated trials 100.0%, unreachable detection 100.0%; current-only future success 0.0%. V2 channel-noise stress shows unguarded UBC success drops to 0.330 at update-channel noise sigma 0.10 and 0.260 at sigma 0.20, while guarded UBC reaches 0.750 and 0.600.
9. Biggest weaknesses: simulated evidence only, finite future-context set, Euclidean correction cost, exact local update-channel assumption, local linearization, and no real robot hardware contact study.
10. Paper-readiness judgment: workshop-only / revise before main-conference submission. The paper is coherent and runnable, but should be strengthened with learned update-Jacobian estimates, hardware correction data, or a richer robot planner before a main-conference submission.
11. Exact Downloads PDF path: C:/Users/wangz/Downloads/15.pdf (263,370 bytes)
12. GitHub URL: https://github.com/Jason-Wang313/15_minimum_intervention_robot_correction (pushed by parent recovery; commit 6270272)
13. Desktop copy status: copied by parent recovery to C:\Users\wangz\OneDrive\Desktop\15.pdf

## Submission-Hardening v2

Checked: 2026-06-13 00:16:16 +01:00

- Added estimated-update-channel stress tests and a manuscript table.
- Original trusted-channel result retained: UBC future success on reachable trials 1.000; unreachable detection 1.000.
- V2 boundary: unguarded UBC success under noisy estimated channels is 0.330 at sigma 0.10 and 0.260 at sigma 0.20.
- V2 boundary: guarded UBC improves to 0.750 at sigma 0.10 and 0.600 at sigma 0.20, but gives up the exact minimum-correction interpretation.
- Canonical v2 PDF: `C:/Users/wangz/Downloads/15.pdf` (263,370 bytes).
- Terminal decision: workshop-only / revise before main-conference submission.
- Desktop policy: no new Desktop copy created during v2 hardening.
