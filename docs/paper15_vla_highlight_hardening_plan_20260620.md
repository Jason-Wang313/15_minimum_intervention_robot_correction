# Paper15 VLA Highlight Hardening Plan

Date: 2026-06-20

## Objective

Make `C:/Users/wangz/Downloads/15.pdf` explicitly match the visible VLA-v4
role model's boxed-link behavior while preserving the final 25-page minimum
intervention paper:

- citation links use green one-point boxes;
- internal figure/table/equation/section links use red one-point boxes;
- URL links use green one-point boxes;
- the final PDF is rebuilt, copied to Downloads, visually checked, and leaves
  no local `paper/main.pdf`.

## Plan-Start Evidence

Baseline artifact:

- Canonical PDF: `C:/Users/wangz/Downloads/15.pdf`
- Pages: 25
- Size: 414,131 bytes
- SHA256: `A3C35CED8E413B92C2DE1C58B54265EB3EBFCE4A46420AE65A23C31EAB2F66B9`
- Local `paper/main.pdf`: absent
- Repository branch: `master`

Baseline link inventory from the current Downloads PDF:

- Link pages: `[(1, 14), (2, 34), (4, 2), (5, 1), (6, 2), (14, 1), (15, 1), (17, 2)]`
- Annotation colors: green = 48, red = 9, cyan = 0
- Border widths: `(0, 0, 1)` for all 57 link annotations

Source finding:

- `paper/main.tex` is the active manuscript source.
- The preamble loads plain `\usepackage{hyperref}` but does not explicitly
  lock `citebordercolor`, `linkbordercolor`, `urlbordercolor`, or
  `pdfborder`.
- The current PDF already has green citation/URL boxes, red internal-reference
  boxes, and no cyan, but the target is to make that behavior explicit and
  reproducible.
- There is no dedicated build script in `scripts/`; use the documented manual
  LaTeX flow from `paper/`, with a fresh `pdflatex`, `bibtex`, and repeated
  `pdflatex` sequence before export.

## Role-Model Target

Install the same explicit hyperref policy as the visible VLA-v4 role model:

```tex
\usepackage{hyperref}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

## Execution Plan

1. Add the VLA `\hypersetup` block immediately after `\usepackage{hyperref}`
   in `paper/main.tex`.
2. Rebuild manually from `paper/` with `pdflatex`, `bibtex`, and repeated
   `pdflatex` passes.
3. If the log asks for another pass for cross-references, run the final
   canonical pass before recording metadata.
4. Copy the rebuilt `paper/main.pdf` to `C:/Users/wangz/Downloads/15.pdf`.
5. Remove local `paper/main.pdf` after export.
6. Recompute page count, byte size, SHA256, annotation colors, border widths,
   and link pages from the final Downloads PDF.
7. Render every page that contains link annotations into
   `tmp/pdfs/paper15_after`.
8. Visually inspect rendered affected pages:
   - green citation and URL boxes are crisp and aligned;
   - red internal-reference boxes are crisp and aligned;
   - no cyan boxes appear;
   - layout, figures, tables, headers, and page count remain stable.
9. Update README/status/audit/version/validation metadata with the new hash and
   VLA-style boxed-link inventory.
10. Validate build logs, diff hygiene, final PDF hash, and absence of local
    `paper/main.pdf`.
11. Remove Paper15 temp renders, leaving only the shared role-model render
    directory.
12. Stage only Paper15 source and metadata files, commit, push, and verify a
    clean repository before moving to Paper14.

## Non-Goals

- Do not alter experiment results, claims, figures, tables, bibliography
  content, or page count.
- Do not add or remove citations, references, or URLs merely to change link
  counts.
- Do not leave intermediate PDFs or render folders behind.

## Completion Evidence

- Added the explicit VLA `\hypersetup` block immediately after
  `\usepackage{hyperref}` in `paper/main.tex`.
- Rebuilt from `paper/` with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Exported canonical PDF: `C:/Users/wangz/Downloads/15.pdf`
- Pages: 25
- Size: 414,131 bytes
- SHA256: `DDDB3B1F90A4DB4E4470E531BA21407737A088B5A5A2B313F3FD8244F83E1E1F`
- Link inventory: 57 annotations on pages `[(1, 14), (2, 34), (4, 2), (5, 1), (6, 2), (14, 1), (15, 1), (17, 2)]`; green = 48, red = 9, cyan = 0; all borders `(0, 0, 1)`.
- Visual audit: rendered pages 1, 2, 4, 5, 6, 14, 15, and 17; green citation/URL boxes and red internal-reference boxes are crisp and aligned.
- Local `paper/main.pdf`: removed after export.
