# Submission Attack Log

Checked: 2026-06-14

## Hostile Round 1: The paper is too small and only proves a toy QP

Result: Addressed for mechanism-scope submission.

Action: Added a v3 full-scale suite with eight experiment families, 2,426 seed-row summaries, generated figures, generated tables, expanded proofs, and failure-analysis appendices.

## Hostile Round 2: The update channel is assumed known

Result: Addressed as a central limitation.

Action: Added estimated-channel stress with noise, scale, sample-quality, and guard margins. At sigma 0.10, unguarded success is 0.344 and guard-1.0 success is 0.906.

## Hostile Round 3: Local linear theory will fail under nonlinear learners

Result: Addressed.

Action: Added nonlinear locality stress. At curvature 0.20, raw linear UBC success is 0.000 and trust-recentered success is 0.817.

## Hostile Round 4: Baselines are weak

Result: Partially addressed.

Action: Added reward-gradient, coactive direction, margin-penalty, sequential greedy, robust UBC, safe large guard, random context, wrong-cost, and oracle-channel baselines.

## Hostile Round 5: The paper overpromises hardware

Result: Claim narrowed.

Action: README, claims, readiness decision, reviewer response, and manuscript limitations all state that this is not a hardware or learned tactile-policy result.
