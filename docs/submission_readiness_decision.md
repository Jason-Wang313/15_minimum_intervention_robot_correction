# Submission Readiness Decision

Decision: ready under mechanism/counterexample scope after v3 full-scale hardening.

The paper now has a full-scale evidence package for its central mechanism: physical corrections should be minimized after projection through the robot learner's update channel, because current repair and future behavior change can diverge.

Submission-safe claim:

UBC gives a local certificate for whether a physical correction can change specified future margins through the robot's update channel. It returns a minimum-cost correction when reachable, and it exposes infeasibility, nullspace effort, and false certificates when the channel or future-context set is inadequate.

Claims to avoid:

- Do not claim hardware validation.
- Do not claim global nonlinear optimality.
- Do not claim learned tactile or high-dimensional update channels are solved.
- Do not claim human intent is inferred.
- Do not claim robustness to estimated channels without guard margins and validation.
- Do not claim the finite future-context set covers all deployment contexts.

Minimum next evidence for a systems paper:

- Real or high-fidelity manipulator corrections.
- Learned update-Jacobian estimates with held-out validation.
- A future-context selection protocol tied to deployment risk.
- Human effort or comfort calibration for the cost matrix.
- Comparisons against deployed preference-learning, intervention-learning, and shared-autonomy systems.
