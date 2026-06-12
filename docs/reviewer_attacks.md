# Reviewer Attacks

1. The method is only a local linearization; nonlinear robot learners may invalidate the certificate far from the correction point.
2. The future contexts are selected by the experimenter, so the guarantee is conditional on a finite evaluation set.
3. The simulation is abstract and does not yet show a real manipulator receiving physical corrections.
4. Some prior work in reward learning from physical corrections may be framed as implicitly crossing behavior boundaries.
5. Estimating the update Jacobian on a real robot could be noisy or expensive.
6. The min-norm objective may not match human biomechanics or comfort.
7. The infeasibility certificate depends on the chosen learner, not on the task's true learnability.
8. Baselines may be weaker than the strongest modern preference or correction learner.
9. The paper needs clearer separation between immediate trajectory repair and future policy change.
10. Without hardware, the work may be better suited to a workshop unless the formal framing is persuasive.

## Planned rebuttal posture
- Be explicit that the guarantee is local and learner-relative.
- Present infeasibility as a diagnostic of the robot's correction interface, not a claim about human intent.
- Emphasize the mechanism shift: physical correction is evaluated through update reachability.
- Keep unsupported claims out of the abstract and conclusion.

## V2 channel-estimation rebuttal

The hardening pass adds the missing stress. UBC remains exact when the modeled channel is trusted, but if it solves with a noisy estimated channel and the true margins are evaluated under the original channel, success drops sharply: 0.330 at sigma 0.10 and 0.260 at sigma 0.20. A guarded variant recovers 0.750 and 0.600 success respectively, but this is no longer the exact minimum correction. The paper now frames Jacobian estimation as a core deployment blocker, not an implementation detail.
