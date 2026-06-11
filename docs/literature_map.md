# Literature Map

## Field box
Human-robot interaction and correction for embodied robot learning: physical corrections, kinesthetic teaching, corrective demonstrations, shared autonomy, preference or reward learning from human input, intervention-aided imitation/RL, and adjacent safety/control work where a human action changes or fails to change future robot behavior.

## Sweep protocol
- Landscape sweep target: 1000 papers. Matrix rows present: 1000.
- Serious skim set: 300 rows, ranks 1-300 when available.
- Deep-read set: 225 rows, ranks 1-225 when available.
- Hostile prior-work set: 100 rows, ranks 1-100 when available.
- Year range: 1990-2026.

The sweep used title, abstract, venue, citation, and concept metadata. The deep-read labels are abstract-level and claim-mechanism level readings, not full archival verification of every PDF.

## Theme counts

| Theme | Count |
|---|---:|
| safety/control | 425 |
| physical correction | 348 |
| kinesthetic teaching | 326 |
| intervention learning | 303 |
| embodied hri | 237 |
| reward inference | 214 |
| preference learning | 136 |
| shared autonomy | 108 |
| robot learning adjacent | 46 |

## Most relevant hostile papers

| Rank | Year | Title | Why it matters |
|---:|---:|---|---|
| 1 | 2023 | Unified Learning from Demonstrations, Corrections, and Preferences during Physical Huma... | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |
| 2 | 2022 | Unified Learning from Demonstrations, Corrections, and Preferences during Physical Huma... | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |
| 3 | 2020 | Quantifying Hypothesis Space Misspecification in Learning From Human-Robot Demonstratio... | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |
| 4 | 2019 | Learning the Correct Robot Trajectory in Real-Time from Physical Human Interactions | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |
| 5 | 2021 | Learning reward functions from diverse sources of human feedback: Optimally integrating... | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 6 | 2019 | Recent Advances in Robot Learning from Demonstration | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 7 | 2017 | Learning Robot Objectives from Physical Human Interaction | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 8 | 2020 | Learning from Interventions: Human-robot interaction as both explicit and implicit feed... | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 9 | 2009 | Learning mobile robot motion control from demonstration and corrective feedback | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |
| 10 | 2023 | An Incremental Inverse Reinforcement Learning Approach for Motion Planning with Separat... | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 11 | 2018 | Learning and Personalizing Socially Assistive Robot Behaviors to Aid with Activities of... | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 12 | 2021 | Learning Human Objectives from Sequences of Physical Corrections | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |
| 13 | 2017 | Active Preference-Based Learning of Reward Functions | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 14 | 2018 | Robot Learning from Demonstration in Robotic Assembly: A Survey | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 15 | 2019 | Reinforcement learning of motor skills using Policy Search and human corrective advice | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |
| 16 | 2019 | Learning Reward Functions by Integrating Human Demonstrations and Preferences | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 17 | 2023 | An Incremental Inverse Reinforcement Learning Approach for Motion Planning with Separat... | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 18 | 2021 | Concept2Robot: Learning manipulation concepts from instructions and human demonstrations | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 19 | 2011 | Task Refinement for Autonomous Robots Using Complementary Corrective Human Feedback | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |
| 20 | 2018 | Learning from Physical Human Corrections, One Feature at a Time | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |
| 21 | 2015 | Efficient Model Learning from Joint-Action Demonstrations for Human-Robot Collaborative... | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 22 | 2025 | RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |
| 23 | 2023 | Robot Programming by Demonstration: Trajectory Learning Enhanced by sEMG-Based User Han... | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 24 | 2020 | Training Human Teacher to Improve Robot Learning from Demonstration: A Pilot Study on K... | Makes it less novel to merely use human corrections or feedback to update a robot policy. |
| 25 | 2021 | Informing Real-Time Corrections in Corrective Shared Autonomy Through Expert Demonstrat... | Makes it less novel to treat physical corrections as reward or feature-learning evidence. |

## Reading outcome
The corpus strongly covers human corrections as data, reward inference from corrections, preference and coactive learning, shared autonomy, and intervention-aided training. What remains weakly covered is not another feedback modality, but a formal object that asks whether a physical correction is the minimum input that crosses the learner's future-behavior boundary. This shifts the center from 'what did the human mean?' to 'what part of this physical correction can the robot's update rule actually use?'

## Chosen thesis
The smallest useful physical robot correction is not the smallest displacement that fixes the current motion; it is the minimum-energy correction whose image through the robot's update channel crosses a future-behavior decision boundary. This paper formalizes that object as a Minimum Effective Correction and gives a local certificate that separates behavior-changing corrections from compliance-only motion.
