# Claims

## Supported by formal local analysis

- Under a locally affine robot update and linear future-behavior margins, the Minimum Effective Correction is the solution of a convex minimum-cost feasibility problem.
- If the projected constraints are infeasible in the correction channel, no physical correction inside that local channel can certify the requested future behavior.
- Any correction component in the nullspace of the composed future-margin/update map cannot alter the certified future margins.
- Weighted effort changes the meaning of "minimum"; the correct correction depends on the physical interface cost.

## Supported by runnable v3 simulation

- Immediate current repair is not equivalent to future behavior change. In the main context setting, UBC future success is 1.000 while current-only success is 0.000.
- Random feasible search can approach success but is not minimum; in the main setting its norm is 2.259 times the UBC norm.
- Estimated update channels can produce false certificates. At sigma 0.10, unguarded estimated-channel success is 0.344 and guard-1.0 success is 0.906 at larger norm.
- Local linear certificates can fail under nonlinear margins. At curvature 0.20, raw linear UBC success is 0.000 while trust-recentered success is 0.817.
- Stronger baselines do not erase the estimand: UBC success is 1.000 in Family E while margin-penalty success is 0.007.
- Ablations confirm that future contexts and update-channel projection are necessary: full UBC success is 1.000 while no-future-context success is 0.008.

## Unsupported or deliberately not claimed

- No claim of hardware validation.
- No claim of global optimality for nonlinear robot learners.
- No claim that human intent is inferred.
- No claim that finite future contexts cover all deployment cases.
- No claim that learned tactile or high-dimensional policy update channels are solved.
- No claim that exact minimum correction is robust to noisy update-Jacobian estimates without guards or validation.

## Honest Claim Scope

The v3 paper is ready as a full-scale mechanism/counterexample paper. It supports the local estimand: corrections should be minimized after projection through the learner's future-behavior update channel. It is not a real-robot systems result.
