# Novelty Decision

## Chosen Thesis

Minimum useful correction should be defined through the learner's update channel: the physical intervention is effective only if it crosses specified future-behavior decision boundaries after projection through the robot update map.

## Central Mechanism

The central mechanism is the Minimum Effective Correction:

`c* = argmin_c ||c||_W^2 subject to H c >= h`,

where `H = A J` maps physical correction coordinates into future-behavior margins through the learner update channel.

## Why This Direction Beats Alternatives

- It changes the correction objective, not only the optimizer.
- It separates immediate compliance from future learning.
- It makes infeasibility and nullspace directions diagnostic outputs.
- It gives a crisp local certificate while exposing the exact boundaries where the certificate fails.
- v3 tests the mechanism across context coverage, estimated channels, nonlinear locality, interface costs, baselines, nullspaces, embodied synthetic tasks, and ablations.

## Rejected Directions

- A new preference-learning architecture: too broad and not necessary for the estimand claim.
- A hardware-first paper: not supported by current evidence.
- A larger nonlinear optimizer: would hide the local certificate boundary.
- A human-intent inference paper: MEC assumes future predicates and does not infer them.

## Final Choice

Proceed with `Minimum Effective Corrections for Future Robot Behavior` as a mechanism/counterexample paper. The novelty is the learner-relative correction estimand and its diagnostic outputs, not hardware performance.
