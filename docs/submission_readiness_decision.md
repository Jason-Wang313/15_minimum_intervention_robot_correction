# Submission Readiness Decision

Decision: workshop-only / revise before main-conference submission.

The paper has a crisp formal mechanism: corrections should be minimized after projection through the robot learner's update channel, not just by current-task displacement. The simulation is runnable and demonstrates the gap between immediate repair and future behavior change.

The paper is not main-conference-ready as a robotics systems result. It assumes the update channel is locally known and evaluates an abstract correction map rather than a physical robot or learned high-dimensional policy.

Minimum next evidence for a stronger submission:

- Estimate the update Jacobian from noisy robot correction data.
- Evaluate on a manipulator or high-fidelity shared-autonomy task.
- Add future-context selection protocols rather than designer-picked contexts.
- Compare against stronger preference/correction learning baselines with learned features.
