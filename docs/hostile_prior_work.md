# Hostile Prior Work

This file lists the 100 closest or most threatening prior papers from the matrix. Each entry records the problem claim, actual mechanism, hidden assumptions, fixed variables, ignored failure modes, what becomes less novel, and what remains open for this paper.

## 1. Unified Learning from Demonstrations, Corrections, and Preferences during Physical Human-Robot Interaction (2023)
- Venue/authors: ACM Transactions on Human-Robot Interaction; Shaunak A. Mehta; Dylan P. Losey
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: feature map; trajectory parameterization; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 2. Unified Learning from Demonstrations, Corrections, and Preferences during Physical Human-Robot Interaction (2022)
- Venue/authors: arXiv (Cornell University); Shaunak A. Mehta; Dylan P. Losey
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 3. Quantifying Hypothesis Space Misspecification in Learning From Human-Robot Demonstrations and Physical Corrections (2020)
- Venue/authors: IEEE Transactions on Robotics; Andreea Bobu; Andrea Bajcsy; Jaime F. Fisac; Sampada Deglurkar; Anca D. Dragan
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 4. Learning the Correct Robot Trajectory in Real-Time from Physical Human Interactions (2019)
- Venue/authors: ACM Transactions on Human-Robot Interaction; Dylan P. Losey; Marcia K. O'Malley
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 5. Learning reward functions from diverse sources of human feedback: Optimally integrating demonstrations and preferences (2021)
- Venue/authors: The International Journal of Robotics Research; Erdem Byk; Dylan P. Losey; Malayandi Palan; Nicholas C. Landolfi; Gleb Shevchuk; Dorsa Sadigh
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 6. Recent Advances in Robot Learning from Demonstration (2019)
- Venue/authors: Annual Review of Control Robotics and Autonomous Systems; Harish Ravichandar; Athanasios Polydoros; Sonia Chernova; Aude Billard
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 7. Learning Robot Objectives from Physical Human Interaction (2017)
- Venue/authors: Rice University's digital scholarship archive (Rice University); Andrea Bajcsy; Dylan P. Losey; Marcia K. O'Malley; Anca D. Dragan
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Infers an objective or reward model from observed human input, demonstrations, or feedback.
- Hidden assumptions: the feedback can be explained by a stable latent objective
- Variables treated as fixed: reward family; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 8. Learning from Interventions: Human-robot interaction as both explicit and implicit feedback (2020)
- Venue/authors: Robotics: Science and Systems; Jonathan Spencer; Sanjiban Choudhury; Matt Barnes; Matthew Schmittle; Mung Chiang; Peter J. Ramadge; Siddhartha S Srinivasa
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 9. Learning mobile robot motion control from demonstration and corrective feedback (2009)
- Venue/authors: ; Brett Browning; Manuela Veloso; Brenna Argall
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 10. An Incremental Inverse Reinforcement Learning Approach for Motion Planning with Separated Path and Velocity Preferences (2023)
- Venue/authors: Robotics; Armin Avaei; Linda van der Spaa; Luka Peternel; Jens Kober
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: feature map; trajectory parameterization; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 11. Learning and Personalizing Socially Assistive Robot Behaviors to Aid with Activities of Daily Living (2018)
- Venue/authors: ACM Transactions on Human-Robot Interaction; Christina Moro; Goldie Nejat; Alex Mihailidis
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 12. Learning Human Objectives from Sequences of Physical Corrections (2021)
- Venue/authors: ; Mengxi Li; Alper Canberk; Dylan P. Losey; Dorsa Sadigh
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Infers an objective or reward model from observed human input, demonstrations, or feedback.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; future behavior changes smoothly with the learned cost or trajectory parameters; the robot can infer intent while sharing control authority
- Variables treated as fixed: trajectory parameterization; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 13. Active Preference-Based Learning of Reward Functions (2017)
- Venue/authors: ; Dorsa Sadigh; Anca D. Dragan; S. Shankar Sastry; Sanjit A. Seshia
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 14. Robot Learning from Demonstration in Robotic Assembly: A Survey (2018)
- Venue/authors: Robotics; Zuyuan Zhu; Huosheng Hu
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: feature map
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 15. Reinforcement learning of motor skills using Policy Search and human corrective advice (2019)
- Venue/authors: The International Journal of Robotics Research; Carlos Celemin; Guilherme Maeda; Javier Ruz-del-Solar; Jan Peters; Jens Kober
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: reward family; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 16. Learning Reward Functions by Integrating Human Demonstrations and Preferences (2019)
- Venue/authors: ; Malayandi Palan; Gleb Shevchuk; Nicholas C. Landolfi; Dorsa Sadigh
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 17. An Incremental Inverse Reinforcement Learning Approach for Motion Planning with Separated Path and Velocity Preferences (2023)
- Venue/authors: arXiv (Cornell University); Armin Avaei; Linda van der Spaa; Luka Peternel; Jens Kober
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: feature map; trajectory parameterization; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 18. Concept2Robot: Learning manipulation concepts from instructions and human demonstrations (2021)
- Venue/authors: The International Journal of Robotics Research; Lin Shao; Toki Migimatsu; Qiang Zhang; Karen Yang; Jeannette Bohg
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters; the robot can infer intent while sharing control authority
- Variables treated as fixed: trajectory parameterization; reward family; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 19. Task Refinement for Autonomous Robots Using Complementary Corrective Human Feedback (2011)
- Venue/authors: International Journal of Advanced Robotic Systems; etin Merili; Manuela Veloso; H. Levent Akn
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 20. Learning from Physical Human Corrections, One Feature at a Time (2018)
- Venue/authors: ; Andrea Bajcsy; Dylan P. Losey; Marcia K. O'Malley; Anca D. Dragan
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Infers an objective or reward model from observed human input, demonstrations, or feedback.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective
- Variables treated as fixed: feature map; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 21. Efficient Model Learning from Joint-Action Demonstrations for Human-Robot Collaborative Tasks (2015)
- Venue/authors: ; Stefanos Nikolaidis; Ramya Ramakrishnan; Keren Gu; Julie Shah
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: reward family; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 22. RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction (2025)
- Venue/authors: arXiv.org; Zheyuan Hu; Robyn Wu; Naveen Enock; Jasmine Li; Riya Kadakia; Zackory Erickson; Aviral Kumar
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 23. Robot Programming by Demonstration: Trajectory Learning Enhanced by sEMG-Based User Hand Stiffness Estimation (2023)
- Venue/authors: IEEE Transactions on Robotics; Luigi Biagiotti; Roberto Meattini; Davide Chiaravalli; Gianluca Palli; Claudio Melchiorri
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 24. Training Human Teacher to Improve Robot Learning from Demonstration: A Pilot Study on Kinesthetic Teaching (2020)
- Venue/authors: ; Maram Sakr; Martin Freeman; H. F. Machiel Van der Loos; Elizabeth A. Croft
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 25. Informing Real-Time Corrections in Corrective Shared Autonomy Through Expert Demonstrations (2021)
- Venue/authors: IEEE Robotics and Automation Letters; Michael Hagenow; Emmanuel Senft; Robert Radwin; Michael Gleicher; Bilge Mutlu; Michael Zinn
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 26. Training Robots Without Robots: Deep Imitation Learning for Master-to-Robot Policy Transfer (2023)
- Venue/authors: IEEE Robotics and Automation Letters; Heecheol Kim; Yoshiyuki Ohmura; Akihiko Nagakubo; Yasuo Kuniyoshi
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 27. A Socially Assistive Robot Exercise Coach for the Elderly (2013)
- Venue/authors: Journal of Human-Robot Interaction; Juan Fasola; Maja Matari
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Elicits human preferences or improvements and fits a reward, ranking, or trajectory optimizer.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 28. Physical interaction as communication: Learning robot objectives online from human corrections (2021)
- Venue/authors: The International Journal of Robotics Research; Dylan P. Losey; Andrea Bajcsy; Marcia K. O'Malley; Anca D. Dragan
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Infers an objective or reward model from observed human input, demonstrations, or feedback.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 29. Learning from Demonstration and Correction via Multiple Modalities for a Humanoid Robot (2011)
- Venue/authors: BIO Web of Conferences; Brenna Argall; Aude Billard
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 30. Intrinsic interactive reinforcement learning - Using error-related potentials for real world human-robot interaction (2017)
- Venue/authors: Scientific Reports; Su Kyoung Kim; Elsa Andrea Kirchner; Arne Stefes; Frank Kirchner
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Infers an objective or reward model from observed human input, demonstrations, or feedback.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 31. Robotic Imitation of Human Assembly Skills Using Hybrid Trajectory and Force Learning (2021)
- Venue/authors: ; Yan Wang; Cristian C. Beltran-Hernandez; Weiwei Wan; Kensuke Harada
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters; the robot can infer intent while sharing control authority
- Variables treated as fixed: trajectory parameterization; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 32. Quantifying teaching behavior in robot learning from demonstration (2019)
- Venue/authors: The International Journal of Robotics Research; Aran Sena; Matthew Howard
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 33. An Algorithmic Perspective on Imitation Learning (2018)
- Venue/authors: Foundations and Trends in Robotics; Takayuki Osa; Joni Pajarinen; Gerhard Neumann; J. Andrew Bagnell; Pieter Abbeel; Jan Peters
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 34. Artificial intelligence, machine learning and deep learning in advanced robotics, a review (2023)
- Venue/authors: Cognitive Robotics; Mohsen Soori; Behrooz Arezoo; Roza Dastres
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 35. A Survey on Policy Search Algorithms for Learning Robot Controllers in a Handful of Trials (2019)
- Venue/authors: IEEE Transactions on Robotics; Konstantinos Chatzilygeroudis; Vassilis Vassiliades; Freek Stulp; Sylvain Calinon; Jean-Baptiste Mouret
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: reward family; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 36. Instructing Robots by Sketching: Learning from Demonstration via Probabilistic Diagrammatic Teaching (2024)
- Venue/authors: ; Weiming Zhi; Tianyi Zhang; Matthew JohnsonRoberson
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters; the robot can infer intent while sharing control authority
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 37. Nonparametric Online Learning Control for Soft Continuum Robot: An Enabling Technique for Effective Endoscopic Navigation (2017)
- Venue/authors: Soft Robotics; Kit-Hang Lee; Denny K.C. Fu; Martin C. W. Leong; Marco C. K. Chow; Hing-Choi Fu; Kaspar Althoefer; K. Y. Sze; ChungKwong Yeung
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Formulates correction or stabilization through a control objective or constrained optimization.
- Hidden assumptions: future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 38. Safe Learning in Robotics: From Learning-Based Control to Safe Reinforcement Learning (2022)
- Venue/authors: Annual Review of Control Robotics and Autonomous Systems; Lukas Brunke; Melissa Greeff; Adam W. Hall; Zhaocong Yuan; Siqi Zhou; Jacopo Panerati; Angela P. Schoellig
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Elicits human preferences or improvements and fits a reward, ranking, or trajectory optimizer.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 39. Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (2023)
- Venue/authors: ; Tony Z. Zhao; Vikas Kumar; Sergey Levine; Chelsea Finn
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 40. Learning and correcting robot trajectory keypoints from a single demonstration (2017)
- Venue/authors: ; Iigo Iturrate; E.H. Ostergaard; Martin Rytter; Thiusius Rajeeth Savarimuthu
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 41. Learning preferences for manipulation tasks from online coactive feedback (2015)
- Venue/authors: The International Journal of Robotics Research; Ashesh Jain; Shikhar Sharma; Thorsten Joachims; Ashutosh Saxena
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 42. Active Preference-Based Gaussian Process Regression for Reward Learning (2020)
- Venue/authors: ; Erdem Byk; Nicolas Huynh; Mykel J. Kochenderfer; Dorsa Sadigh
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: feature map; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 43. Predictive Preference Learning from Human Interventions (2025)
- Venue/authors: arXiv.org; Haoyuan Cai; Zhenghao Peng; Bolei Zhou
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 44. IntervenGen: Interventional Data Generation for Robust and Data-Efficient Robot Imitation Learning (2024)
- Venue/authors: IEEE/RJS International Conference on Intelligent RObots and Systems; Ryan Hoque; Ajay Mandlekar; Caelan Reed Garrett; Ken Goldberg; Dieter Fox
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses human interventions as corrective labels or safety takeovers during policy learning.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 45. Biped Walk Learning Through Playback and Corrective Demonstration (2010)
- Venue/authors: Proceedings of the AAAI Conference on Artificial Intelligence; etin Merili; Manuela Veloso
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 46. Robot learning of industrial assembly task via human demonstrations (2018)
- Venue/authors: Autonomous Robots; Maria Kyrarini; Muhammad Haseeb; Danijela Risti-Durrant; Axel Grser
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 47. Continual learning from demonstration of robotics skills (2023)
- Venue/authors: Robotics and Autonomous Systems; Sayantan Auddy; Jakob Hollenstein; Matteo Saveriano; Antonio Rodrguez-Snchez; Justus Piater
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 48. Learning to Pick at Non-Zero-Velocity From Interactive Demonstrations (2022)
- Venue/authors: IEEE Robotics and Automation Letters; Anna Mszros; Giovanni Franzese; Jens Kober
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 49. Robotic Imitation of Human Assembly Skills Using Hybrid Trajectory and Force Learning (2021)
- Venue/authors: arXiv (Cornell University); Yan Wang; Cristian C. Beltran-Hernandez; Weiwei Wan; Kensuke Harada
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters; the robot can infer intent while sharing control authority
- Variables treated as fixed: trajectory parameterization; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 50. Approaches to Safety in Inverse Reinforcement Learning (2020)
- Venue/authors: eScholarship (California Digital Library); Dexter R. R. Scobee
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 51. Learning Collaborative Impedance-Based Robot Behaviors (2013)
- Venue/authors: Proceedings of the AAAI Conference on Artificial Intelligence; Leonel Rozo; Sylvain Calinon; Darwin G. Caldwell; Pablo Jimnez; Carme Torras
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 52. Occupational health and safety issues in human-robot collaboration: State of the art and open challenges (2023)
- Venue/authors: Safety Science; Antonio Giallanza; Giada La Scalia; Rosa Micale; Concetta Manuela La Fata
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 53. Online learning of varying stiffness through physical human-robot interaction (2012)
- Venue/authors: ; Klas Kronander; Aude Billard
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 54. Multimodal Human-Robot Interface for Accessible Remote Robotic Interventions in Hazardous Environments (2019)
- Venue/authors: IEEE Access; Giacomo Lunghi; R. Marn; Mario Di Castro; A. Masi; Pedro J. Sanz
- Problem claimed: Claims that human interventions can keep learning robots safe or provide targeted training data.
- Actual mechanism introduced: Uses human interventions as corrective labels or safety takeovers during policy learning.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance
- Variables treated as fixed: feature map
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 55. Learning Trajectory Preferences for Manipulators via Iterative Improvement (2013)
- Venue/authors: arXiv (Cornell University); Ashesh Jain; Brian Wojcik; Thorsten Joachims; Ashutosh Saxena
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 56. Deep Reinforcement Learning for Robotic Manipulation with Asynchronous Off-Policy Updates (2016)
- Venue/authors: arXiv (Cornell University); Shixiang Gu; Ethan Holly; Timothy Lillicrap; Sergey Levine
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 57. Learning from Demonstrations and Human Evaluative Feedbacks: Handling Sparsity and Imperfection Using Inverse Reinforcement Learning Approach (2020)
- Venue/authors: Journal of Robotics; Nafee Mourad; Ali Ezzeddine; Babak Nadjar Araabi; Majid Nili Ahmadabadi
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: reward family; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 58. Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration (2021)
- Venue/authors: IEEE International Conference on Robotics and Automation; Edward Johns
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 59. Using dVRK teleoperation to facilitate deep learning of automation tasks for an industrial robot (2017)
- Venue/authors: ; Jacky Liang; Jeffrey Mahler; Michael Laskey; Pusong Li; Ken Goldberg
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 60. HACTS: a Human-As-Copilot Teleoperation System for Robot Learning (2025)
- Venue/authors: IEEE/RJS International Conference on Intelligent RObots and Systems; Zhiyuan Xu; Yinuo Zhao; Kun Wu; Ning Liu; Junjie Ji; Zhengping Che; Chi Harold Liu; Jian Tang
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 61. Assistive Robots for the Social Management of Health: A Framework for Robot Design and Human-Robot Interaction Research (2020)
- Venue/authors: International Journal of Social Robotics; Meia Chita-Tegmark; Matthias Scheutz
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 62. User Interface Interventions for Improving Robot Learning from Demonstration (2023)
- Venue/authors: International Conference on Human-Agent Interaction; Ornnalin Phaijit; C. Sammut; W. Johal
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 63. Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections (2024)
- Venue/authors: ; Lihan Zha; Yuchen Cui; Li-Heng Lin; Minae Kwon; Montserrat Gonzalez Arenas; Andy Zeng; Fei Xia; Dorsa Sadigh
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Elicits human preferences or improvements and fits a reward, ranking, or trajectory optimizer.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 64. How to Train Your Robots? The Impact of Demonstration Modality on Imitation Learning (2025)
- Venue/authors: ; Haozhuo Li; Yuchen Cui; Dorsa Sadigh
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 65. An Energy Tank-Based Interactive Control Architecture for Autonomous and Teleoperated Robotic Surgery (2015)
- Venue/authors: IEEE Transactions on Robotics; Federica Ferraguti; Nicola Preda; Auralius Manurung; Marcello Bonf; Olivier Lambercy; Roger Gassert; Riccardo Muradore; Paolo Fiorini
- Problem claimed: Claims that autonomy can assist or interpret human control in embodied tasks.
- Actual mechanism introduced: Blends human input with autonomous inference over goals, actions, or assistance modes.
- Hidden assumptions: the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 66. Learning robot motion control with demonstration and advice-operators (2008)
- Venue/authors: ; Brenna Argall; B. Browning; Manuela Veloso
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 67. Proactive human-robot collaboration: Mutual-cognitive, predictable, and self-organising perspectives (2022)
- Venue/authors: Robotics and Computer-Integrated Manufacturing; Shufei Li; Pai Zheng; Sichao Liu; Zuoxu Wang; Xi Vincent Wang; Lianyu Zheng; Lihui Wang
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Formulates correction or stabilization through a control objective or constrained optimization.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 68. Vision-Based Learning from Demonstration System for Robot Arms (2022)
- Venue/authors: Sensors; Pin-Jui Hwang; ChenChien Hsu; PoYung Chou; WeiYen Wang; Cheng-Hung Lin
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 69. Dynamic movement primitives in robotics: A tutorial survey (2023)
- Venue/authors: The International Journal of Robotics Research; Matteo Saveriano; Fares J. AbuDakka; Alja Kramberger; Luka Peternel
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Formulates correction or stabilization through a control objective or constrained optimization.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 70. Motion Planning for Mobile Robots-Focusing on Deep Reinforcement Learning: A Systematic Review (2021)
- Venue/authors: IEEE Access; Huihui Sun; Weijie Zhang; Runxiang Yu; Yujie Zhang
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 71. Hybrid Trajectory and Force Learning of Complex Assembly Tasks: A Combined Learning Framework (2021)
- Venue/authors: IEEE Access; Yan Wang; Cristian C. Beltran-Hernandez; Weiwei Wan; Kensuke Harada
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 72. Opinion Paper: "So what if ChatGPT wrote it?" Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy (2023)
- Venue/authors: International Journal of Information Management; Yogesh K. Dwivedi; Nir Kshetri; Laurie Hughes; Emma Slade; Anand Jeyaraj; Arpan Kumar Kar; Abdullah M. Baabdullah; Alex Koohang
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 73. A Survey of Reinforcement Learning from Human Feedback (2023)
- Venue/authors: arXiv (Cornell University); Timo Kaufmann; Paul Weng; Viktor Bengs; Eyke Hllermeier
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Elicits human preferences or improvements and fits a reward, ranking, or trajectory optimizer.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 74. Correct Me If I am Wrong: Interactive Learning for Robotic Manipulation (2022)
- Venue/authors: IEEE Robotics and Automation Letters; Eugenio Chisari; Tim Welschehold; Joschka Boedecker; Wolfram Burgard; Abhinav Valada
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 75. Feature Expansive Reward Learning (2021)
- Venue/authors: ; Andreea Bobu; Marius Wiggert; Claire J. Tomlin; Anca D. Dragan
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: feature map; reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 76. The Effects of a Robot's Performance on Human Teachers for Learning from Demonstration Tasks (2021)
- Venue/authors: ; Erin Hedlund; Michael Johnson; Matthew Gombolay
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 77. Genetic Algorithm-Based Trajectory Optimization for Digital Twin Robots (2022)
- Venue/authors: Frontiers in Bioengineering and Biotechnology; Xin Liu; Du Jiang; Bo Tao; Guozhang Jiang; Ying Sun; Jianyi Kong; Xiliang Tong; Guojun Zhao
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 78. Redefining Safety in Light of Human-Robot Interaction: A Critical Review of Current Standards and Regulations (2021)
- Venue/authors: Frontiers in Chemical Engineering; Alberto Martinetti; Peter Chemweno; Kostas Nizamis; Eduard FoschVillaronga
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: feature map; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 79. Transfer Learning of Human Preferences for Proactive Robot Assistance in Assembly Tasks (2023)
- Venue/authors: ; Heramb Nemlekar; Neel Dhanaraj; Angelos Guan; Satyandra K. Gupta; Stefanos Nikolaidis
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 80. Knowledge- and ambiguity-aware robot learning from corrective and evaluative feedback (2023)
- Venue/authors: Neural Computing and Applications; Carlos Celemin; Jens Kober
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 81. Using Robotics to Enhance Active Learning in Mathematics: A Multi-Scenario Study (2020)
- Venue/authors: Mathematics; Edgar Omar Lpez-Caudana; Mara Soledad; Sandra Martnez Prez; Guillermo Rodrguez-Abitia
- Problem claimed: Claims that human interventions can keep learning robots safe or provide targeted training data.
- Actual mechanism introduced: Uses human interventions as corrective labels or safety takeovers during policy learning.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 82. Training of construction robots using imitation learning and environmental rewards (2024)
- Venue/authors: Computer-Aided Civil and Infrastructure Engineering; Kangkang Duan; Zhengbo Zou; T.Y. Yang
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: reward family; policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 83. VARIQuery: VAE Segment-Based Active Learning for Query Selection in Preference-Based Reinforcement Learning (2023)
- Venue/authors: ; Daniel Marta; Simon Holk; Christian Pek; Jana Tmov; Iolanda Leite
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the feedback can be explained by a stable latent objective; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 84. Learning Controllers for Reactive and Proactive Behaviors in Human-Robot Collaboration (2016)
- Venue/authors: Frontiers in Robotics and AI; Leonel Rozo; Joo Silvrio; Sylvain Calinon; Darwin G. Caldwell
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters; the robot can infer intent while sharing control authority
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 85. Human-Robot Copilot for Data-Efficient Imitation Learning (2026)
- Venue/authors: ; Rui Yan; Zaitian Gongye; Lars Paulsen; Xuxin Cheng; Xiaolong Wang
- Problem claimed: Claims that a human correction can repair robot behavior more efficiently than full re-demonstration or autonomous trial-and-error.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy; the robot can infer intent while sharing control authority
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input; assistance may mask whether future autonomous behavior actually changed
- What it makes less novel: Makes it less novel to treat physical corrections as reward or feature-learning evidence.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 86. User intent estimation during robot learning using physical human robot interaction primitives (2022)
- Venue/authors: Autonomous Robots; Yujun Lai; Gavin Paul; Yunduan Cui; Takamitsu Matsubara
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 87. Robots in Inspection and Monitoring of Buildings and Infrastructure: A Systematic Review (2023)
- Venue/authors: Applied Sciences; Srijeet Halder; Kereshmeh Afsari
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Formulates correction or stabilization through a control objective or constrained optimization.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 88. Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback (2023)
- Venue/authors: arXiv (Cornell University); Stephen Casper; Xander Davies; Claudia Shi; Thomas Krendl Gilbert; Jrmy Scheurer; Javier Rando; Rachel Freedman; Tomasz Korbak
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 89. Developing a gamified artificial intelligence educational robot to promote learning effectiveness and behavior in laboratory safety courses for undergraduate students (2023)
- Venue/authors: International Journal of Educational Technology in Higher Education; Qifan Yang; Li-Wen Lian; JiaHua Zhao
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Formulates correction or stabilization through a control objective or constrained optimization.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 90. Curricula for teaching end-users to kinesthetically program collaborative robots (2023)
- Venue/authors: PLoS ONE; Gopika Ajaykumar; Gregory D. Hager; ChienMing Huang
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 91. Continual Learning from Demonstration of Robotics Skills (2022)
- Venue/authors: arXiv (Cornell University); Sayantan Auddy; Jakob Hollenstein; Matteo Saveriano; Antonio Rodrguez-Snchez; Justus Piater
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 92. Validating Safety in Human-Robot Collaboration: Standards and New Perspectives (2021)
- Venue/authors: Robotics; Marcello Valori; Adriano Scibilia; Irene Fassi; Jos Saenz; Roland Behrens; Sebastian Herbster; C. Bidard; Eric Lucet
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 93. Cybersecurity, safety and robots: Strengthening the link between cybersecurity and safety in the context of care robots (2021)
- Venue/authors: Computer law & security review; Eduard FoschVillaronga; Tobias Mahler
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: policy class
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 94. Robot learning from demonstration of force-based tasks with multiple solution trajectories (2011)
- Venue/authors: ; Leonel Rozo; Pablo Jimnez; Carme Torras
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy; future behavior changes smoothly with the learned cost or trajectory parameters
- Variables treated as fixed: trajectory parameterization
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 95. Batch Active Learning of Reward Functions from Human Preferences (2024)
- Venue/authors: ACM Transactions on Human-Robot Interaction; Erdem Byk; Nima Anari; Dorsa Sadigh
- Problem claimed: Claims that ranking or preference feedback can teach robot objectives without direct reward engineering.
- Actual mechanism introduced: Elicits human preferences or improvements and fits a reward, ranking, or trajectory optimizer.
- Hidden assumptions: the feedback can be explained by a stable latent objective
- Variables treated as fixed: reward family
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; the smallest useful correction may not be a preference query
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 96. Robot-Supported Collaborative Learning (RSCL): Social Robots as Teaching Assistants for Higher Education Small Group Facilitation (2020)
- Venue/authors: Frontiers in Robotics and AI; Rinat B. RosenbergKima; Yaacov Koren; Goren Gordon
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: the robot can infer intent while sharing control authority
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 97. Crossing the Reality Gap: A Survey on Sim-to-Real Transferability of Robot Controllers in Reinforcement Learning (2021)
- Venue/authors: IEEE Access; Erica Salvato; Gianfranco Fenu; Eric Medvet; Felice Andrea Pellegrino
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Formulates correction or stabilization through a control objective or constrained optimization.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 98. Empathic Robot for Group Learning (2019)
- Venue/authors: ACM Transactions on Human-Robot Interaction; Patrcia AlvesOliveira; Pedro Sequeira; Francisco S. Melo; Ginevra Castellano; Ana Paiva
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Introduces a robot learning, control, or interaction mechanism related to human feedback or embodied adaptation.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: feature map
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 99. Continuous control for robot based on deep reinforcement learning (2019)
- Venue/authors: ; Shansi Zhang
- Problem claimed: Improves how robots use human feedback, corrections, demonstrations, or interaction data.
- Actual mechanism introduced: Formulates correction or stabilization through a control objective or constrained optimization.
- Hidden assumptions: the paper fixes the robot update channel and evaluates feedback quality inside that channel
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.

## 100. ARCap: Collecting High-Quality Human Demonstrations for Robot Learning with Augmented Reality Feedback (2024)
- Venue/authors: IEEE International Conference on Robotics and Automation; Sirui Chen; Chen Wang; Kaden Nguyen; Fei-Fei Li; C. K. Liu
- Problem claimed: Claims that demonstrations can transfer task structure from people to robots.
- Actual mechanism introduced: Uses demonstrations or kinesthetic traces as training data for a robot policy or trajectory representation.
- Hidden assumptions: human input is treated as an informative training signal rather than only transient compliance; the teacher can show behavior close enough to the desired policy
- Variables treated as fixed: robot model and task distribution
- Failure modes ignored: physical correction energy may lie in the nullspace of the robot's learning update; re-demonstration can be larger than the minimum behavior-changing physical input
- What it makes less novel: Makes it less novel to merely use human corrections or feedback to update a robot policy.
- What it leaves open: Leaves open a certificate for the minimum physical intervention that is guaranteed to alter future behavior. This is a hostile comparison because it already targets human correction or intervention.
