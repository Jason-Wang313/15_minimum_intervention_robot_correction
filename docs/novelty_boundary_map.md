# Novelty Boundary Map

## Not novel enough
- Learning a reward from physical corrections.
- Treating a correction as a preference, ranking, or improved trajectory.
- Adding uncertainty, active querying, a verifier, or a larger model to existing correction learning.
- Demonstrating another correction dataset or benchmark without a new mechanism.
- Shared-autonomy assistance that helps the current execution but does not certify future autonomous change.

## Claimed new boundary
The smallest useful physical robot correction is not the smallest displacement that fixes the current motion; it is the minimum-energy correction whose image through the robot's update channel crosses a future-behavior decision boundary. This paper formalizes that object as a Minimum Effective Correction and gives a local certificate that separates behavior-changing corrections from compliance-only motion.

## Central mechanism
Update-Boundary Correction (UBC): linearize the robot's parameter update with respect to a physical correction, express desired future behavior as halfspace margins over the updated robot state, and solve the minimum-norm correction in the reachable image of that update map. The same calculation returns an infeasibility or nullspace warning when physical effort cannot change the future policy under the robot's current learner.

## What the closest prior work already owns
- Human corrections can be informative about desired reward features.
- Physical interaction can teach motion, constraints, and preferences.
- Coactive/preference learning can reduce query burden relative to full demonstrations.
- Shared autonomy can infer goals and blend autonomy with human input.
- Human interventions can improve safety or supply corrective labels during policy learning.

## What this paper keeps
- A robot learner with a known or estimated local update map.
- A finite set of future contexts or behavior predicates to certify.
- A local linearization of update and future margins.

## What this paper changes
- The unit of analysis is the correction's image through the learner update map, not the correction's raw geometry.
- The method can declare a correction request unreachable under the current learner.
- The paper compares immediate repair against future-behavior change, exposing a false equivalence in much correction work.

## Boundary table

| Prior cluster | Already covers | Boundary left for this paper |
|---|---|---|
| Physical human corrections | Corrections update reward/features/policy | Minimum physical correction that crosses future-behavior boundary through update map |
| Learning from demonstration | Human traces provide task examples | Smaller targeted correction than re-demonstration; nullspace certificate |
| Preference/coactive learning | Human rankings improve trajectory optimization | Physical correction effort and update reachability rather than query labels |
| Shared autonomy | Assistance improves current control | Whether autonomous future behavior changed after contact |
| Intervention-aided learning | Takeovers provide corrective labels/safety | Minimum intervention and infeasibility certificate for future contexts |
| Minimum intervention control | Control changes current trajectory minimally | Learning-aware intervention that changes future policy, not only state |
