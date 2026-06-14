# Hostile Reviewer Response

The strongest criticism is correct: UBC is a local certificate for a modeled update channel, not a complete robot teaching system. The v3 paper now makes that boundary the center of the evaluation.

The main positive result is sharp: in the future-context coverage setting, UBC reaches 1.000 future success while current-only correction reaches 0.000, and random search requires 2.259 times the norm. This supports the estimand claim that the minimum useful correction is computed after projection through the learner's update channel.

The strongest negative results are also explicit. At estimated-channel sigma 0.10, unguarded UBC succeeds in only 0.344 of reachable cases, while guard-1.0 reaches 0.906 at larger norm. Under nonlinear curvature 0.20, raw linear UBC has 0.000 true success and trust-recentered UBC reaches 0.817. These results prevent the paper from overclaiming robustness.

The final claim is therefore narrow and submission-safe: UBC identifies minimum effective corrections for specified future margins under a modeled local update channel, and it exposes infeasibility, nullspace effort, and false certificates. It does not claim hardware validation, human-intent inference, or solved learned Jacobians.
