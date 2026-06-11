# Plan

## Goal
Produce a complete, honest robotics/embodied-intelligence research paper for paper 15, including a broad literature sweep, adversarial novelty analysis, runnable evidence, an ICLR-style manuscript, compiled PDF at `C:/Users/wangz/Downloads/15.pdf`, and a public GitHub repository named `15_minimum_intervention_robot_correction`.

## Safety And Execution Rules
- Use bounded, non-interactive commands with explicit timeouts for long-running work.
- Prefer Python helper scripts for literature processing, experiments, plotting, and LaTeX-safe text generation.
- Reuse existing artifacts if valid; never delete expensive caches unless inadequate.
- Keep `child_status.md` compact and update it after each stage with commands, failures, and recovery.
- Treat literature and novelty claims adversarially; mark unsupported claims honestly.

## Stages
1. Initialize status and inspect existing folder artifacts.
2. Build/reuse a literature corpus:
   - 1000-paper landscape sweep saved to `docs/related_work_matrix.csv`.
   - 300-paper serious skim.
   - 200-250-paper deep read subset.
   - 100-paper hostile prior-work set.
3. Write literature artifacts:
   - `docs/literature_map.md`
   - `docs/hostile_prior_work.md`
   - `docs/novelty_boundary_map.md`
   - `docs/novelty_decision.md`
4. Choose the strongest paper direction only after mapping assumptions and hostile prior work.
5. Implement runnable evidence:
   - Formal toy model/simulator for minimum-intervention physical correction.
   - Baselines and adversarial checks.
   - Figures and tables from reproducible scripts.
6. Write paper artifacts:
   - `docs/claims.md`
   - `docs/reviewer_attacks.md`
   - ICLR-style LaTeX paper with sanitized bibliography.
7. Compile with direct `pdflatex`/`bibtex` passes, recover from common Unicode/bibliography failures, and copy final PDF to `C:/Users/wangz/Downloads/15.pdf`.
8. Create/update public GitHub repo `15_minimum_intervention_robot_correction`, commit, and push.
9. Write `docs/final_audit.md` answering all required audit questions, including GitHub URL and Desktop-copy status.

## Working Thesis Placeholder
Do not lock the thesis yet. Initial seed: formalize the smallest physical correction that changes future robot behavior. Replace it if the literature sweep reveals a stronger robotics contribution.
