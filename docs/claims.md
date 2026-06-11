# Claims

## Supported by formal local analysis
- Under a locally affine robot update and linear future-behavior margins, the Minimum Effective Correction is the solution of a convex minimum-norm feasibility problem.
- If the projected constraints are infeasible in the correction channel, no physical correction inside that local channel can certify the requested future behavior.
- Any correction component in the nullspace of the composed future-margin/update map cannot alter the certified future margins.

## Supported by runnable simulation
- Immediate minimal repair can have low current-task cost while failing to change future behavior.
- UBC achieves high future-context success on reachable trials with smaller physical norm than a fixed-step gradient correction baseline.
- UBC identifies unreachable correction requests when desired future margins lie outside the image of the physical correction channel.

## Unsupported or deliberately not claimed
- No claim of global optimality for nonlinear robot learners.
- No claim that the human's intent is perfectly inferred.
- No claim that the finite future-context set covers every possible deployment context.
- No hardware validation in this attempt.
- No claim that UBC replaces preference learning, kinesthetic teaching, or shared autonomy in all settings.
