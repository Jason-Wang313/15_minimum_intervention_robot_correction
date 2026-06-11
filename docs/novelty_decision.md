# Novelty Decision

## Hidden assumptions considered

1. A correction that improves the current trajectory also changes the future autonomous policy.
2. Human physical effort is aligned with the robot learner's parameter update directions.
3. The robot's update rule is fully actuated by the correction interface.
4. The same correction channel is informative across future task contexts.
5. A larger correction is more informative than a smaller one.
6. A smaller geometric displacement is the same as a smaller learning intervention.
7. Corrections can be interpreted without modeling the update nullspace.
8. Robot compliance during contact is evidence of learning.
9. Feature maps used for reward learning already contain the corrected concept.
10. Preference or ranking feedback is equivalent to physical correction feedback.
11. The teacher knows how the robot will generalize from the correction.
12. The learner's local linearization is accurate enough for all correction magnitudes.
13. Corrective demonstrations are cheaper than targeted boundary-crossing inputs.
14. Shared autonomy assistance reveals future autonomous behavior.
15. Human interventions are always labels for the action the robot should have taken.
16. A safe takeover implies that the policy has learned the safety constraint.
17. A single corrected episode identifies the intended future behavior class.
18. All physically feasible corrections are equally easy for the human.
19. The correction cost should be measured in task-space Euclidean norm.
20. Human corrections remain independent of robot adaptation over repeated interactions.
21. The relevant future contexts are known or adequately sampled.
22. The robot planner's decision boundary is smooth near the corrected behavior.
23. Infeasible correction requests are rare enough to ignore.
24. Evaluation on immediate task repair is sufficient evidence for correction learning.

## Candidate directions

| Direction | Broken assumption | Mechanism | Risk | Decision |
|---|---|---|---|---|
| Minimum Effective Correction certificates | Current-fix equals future-learning. | Compute the min-norm physical correction that crosses future behavior margins through the learner update Jacobian. | Local linearization and chosen future-context set may be incomplete. | chosen |
| Correction-channel discovery | The robot knows which physical dimensions update its world model. | Estimate the correction-to-update map from repeated contacts and expose unlearnable directions. | Can degrade into system identification plus uncertainty unless the intervention object is new. | defer |
| Nullspace-aware teaching interface | The human can infer what the learner understood. | Render or haptically signal directions that are compliance-only under the learner. | Mostly an interface contribution without a new robot-learning object. | defer |
| Nonlinear correction continuation | Local decision boundaries are enough. | Track correction feasibility across nonlinear replanning boundaries. | More complex, weaker as a first paper without strong benchmarks. | defer |
| Adversarial correction benchmark | Existing benchmarks expose correction-learning failures. | Benchmark tasks with hidden update nullspaces. | Forbidden weak move if only a benchmark. | reject as central thesis |

## Chosen idea
Minimum Effective Correction certificates.

## Reason for choosing it
The strongest hostile prior work already has correction-as-learning-signal mechanisms. The uncovered gap is the absence of a correction object that is simultaneously physical, future-behavior-directed, and update-reachability-aware. UBC makes the robot learner's correction channel central; this is a different mechanism rather than a larger model, more data, an uncertainty wrapper, or a verifier bolted onto existing correction learning.

## Thesis
The smallest useful physical robot correction is not the smallest displacement that fixes the current motion; it is the minimum-energy correction whose image through the robot's update channel crosses a future-behavior decision boundary. This paper formalizes that object as a Minimum Effective Correction and gives a local certificate that separates behavior-changing corrections from compliance-only motion.
