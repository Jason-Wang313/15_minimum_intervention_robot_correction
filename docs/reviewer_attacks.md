# Reviewer Attacks

## Attack 1: This is only a local linearization.

Response: Correct. The claim is local. Family C stresses nonlinear curvature: raw linear UBC has 0.000 success at curvature 0.20, while trust-recentered UBC reaches 0.817. The manuscript states that local validation is required.

## Attack 2: The update channel may be unknown or noisy.

Response: Correct and central. Family B evaluates estimated channels. At sigma 0.10, unguarded success is 0.344 and guard-1.0 success is 0.906 at larger norm. The paper does not claim robustness without guard margins or validation.

## Attack 3: Future contexts are designer-selected.

Response: Correct. The guarantee is conditional on the finite context set. Family H shows that removing future contexts or using random contexts collapses the mechanism. The manuscript calls context selection a deployment requirement.

## Attack 4: There is no hardware.

Response: Correct. The v3 paper is a mechanism/counterexample paper, not a real-robot systems result.

## Attack 5: Stronger correction-learning baselines might close the gap.

Response: Partially addressed. Family E includes reward-gradient, coactive direction, margin penalty, safe guard, robust UBC, and sequential greedy baselines. UBC success is 1.000; margin-penalty success is 0.007. Guarded methods can match success at larger norm.

## Attack 6: Minimum Euclidean norm is not human effort.

Response: Correct. Family D evaluates anisotropic force, joint-limited, comfort-weighted, and sparse-contact costs. The manuscript defines MEC with a positive definite cost matrix `W`.

## Attack 7: Infeasibility may be a model artifact.

Response: It is explicitly learner-relative. An infeasibility certificate means the current channel cannot certify the requested future margins, not that the task is impossible for all interfaces.

## Attack 8: Nullspace warnings are abstract.

Response: Family F measures nullspace effort directly, and Family G includes force/tactile and peg-compliance synthetic tasks where low-rank channels are structurally plausible.

## Attack 9: The title suggests future robot behavior but the evidence is synthetic.

Response: The title is acceptable only under the local mechanism scope. The abstract and limitations state that there is no hardware or learned high-dimensional policy.

## Numeric Stress Points

- Main setting: UBC future success 1.000, current-only future success 0.000.
- Random-search norm ratio: 2.259.
- Estimated-channel sigma 0.10: unguarded success 0.344, guard-1.0 success 0.906.
- Nonlinear curvature 0.20: raw linear UBC success 0.000, trust-recentered success 0.817.
- Ablation: full UBC success 1.000, no-future-context success 0.008.
