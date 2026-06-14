# Novelty Boundary Map

## Not Novel

- Learning from demonstration.
- Physical human correction as feedback.
- Preference learning or coactive learning.
- Shared autonomy and intervention learning.
- Solving a small convex quadratic program.
- Minimum intervention as a general motor-control principle.
- Linearizing a robot update rule.

## Potentially Novel

- Defining the minimum useful physical correction as the minimum-cost correction that crosses future-behavior boundaries after projection through the robot learner's update channel.
- Treating infeasibility as a diagnostic of the current correction interface rather than as user failure.
- Treating nullspace effort as physical effort that can repair the moment while leaving certified future behavior unchanged.
- Evaluating correction methods by future-context success, unreachable detection, and false certificate rate rather than current repair alone.

## Boundary Conditions

- If current repair always predicts future success in a task, MEC adds little practical value for that task.
- If the update channel is too noisy or unstable, exact UBC can produce false certificates without guards or validation.
- If future contexts are missing or random, the certificate can validate the wrong behavior.
- If human effort is not captured by the cost matrix, the "minimum" claim must be weakened.
- The current evidence does not establish real-robot success.

## Formal Boundary

For local channel `H = A J`, MEC is a statement about the robot's current update map and future context set. A correction can be physically meaningful and still be learning-null if it lies in `Null(H)`. A request can be unreachable through the current interface even if another teaching modality could solve it.
