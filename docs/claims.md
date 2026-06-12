# Claims

## Supported by formal local analysis
- Under a locally affine robot update and linear future-behavior margins, the Minimum Effective Correction is the solution of a convex minimum-norm feasibility problem.
- If the projected constraints are infeasible in the correction channel, no physical correction inside that local channel can certify the requested future behavior.
- Any correction component in the nullspace of the composed future-margin/update map cannot alter the certified future margins.

## Supported by runnable simulation
- Immediate minimal repair can have low current-task cost while failing to change future behavior.
- UBC achieves high future-context success on reachable trials with smaller physical norm than a fixed-step gradient correction baseline.
- UBC identifies unreachable correction requests when desired future margins lie outside the image of the physical correction channel.
- V2 channel-noise stress shows the local certificate is fragile when the learner update channel is estimated incorrectly: unguarded UBC success is 0.330 at channel-noise sigma 0.10 and 0.260 at sigma 0.20, while a guarded variant reaches 0.750 and 0.600 respectively at larger correction norms.

## Unsupported or deliberately not claimed
- No claim of global optimality for nonlinear robot learners.
- No claim that the human's intent is perfectly inferred.
- No claim that the finite future-context set covers every possible deployment context.
- No hardware validation in this attempt.
- No claim that UBC replaces preference learning, kinesthetic teaching, or shared autonomy in all settings.
- No claim that the exact certificate is robust to noisy update-Jacobian estimates without guard margins or online validation.
