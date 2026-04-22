# Design Spec: Positron Slide + Notebook Orientation Section

**Date:** 2026-04-22
**Status:** Approved

---

## Overview

Add a "What Is Positron?" slide immediately after the existing "From Google Colab → Positron" comparison slide, and add a brief Positron orientation section near the top of the workshop notebook. Both pieces serve the same goal: give learners enough context about their new environment to feel oriented before the hands-on portion begins.

---

## 1. Slide: "What Is Positron?"

### Placement

Inserted immediately after the existing `# From Google Colab → Positron (Local Development)` slide (currently slide 5 in the deck).

### Structure

Single slide using the standard MARP `h1` teal header style (no `_class` override needed — default section layout).

**Top section — lineage and context (2 bullets):**
- Positron is a fork of VS Code, built by Posit — the team behind RStudio
- Supports Python and R in the same environment; familiar to RStudio users, familiar to VS Code users

**Middle section — 2×2 panel grid (4 cards using existing `.callout`-style boxes or inline CSS grid):**

| Panel | Description |
|-------|-------------|
| Variable Explorer | Browse all live objects in memory — names, types, values |
| Data Viewer | Inspect DataFrames visually without printing them |
| Integrated Console | Run code interactively, line-by-line, outside the notebook |
| Plots Pane | Inline chart output, persisted across runs |

**Bottom — callout box:**
> "If you've used RStudio, this layout will feel immediately familiar. If you've used VS Code, your extensions and keybindings carry over."

### Style notes

- Use existing `.cols` / `.col` two-column grid for top bullets if space is tight; otherwise inline `<ul>`
- Panel grid uses `display: grid; grid-template-columns: 1fr 1fr` with the existing `--gray-bg` background and `--yale-blue` heading color
- No new CSS classes needed — compose from existing primitives in the MARP style block

---

## 2. Notebook Section: "Your Development Environment"

### Placement

New markdown cell inserted **after the welcome cell** (`## Welcome to Python 2!`) and **before** `# Part 0: Setup Verification`. This appears at the top of the notebook when learners first open it.

### Content

```markdown
## Your Development Environment: Positron

Positron is a **data science IDE** built by [Posit](https://posit.co/) — the team behind RStudio. It is a fork of VS Code, which means your VS Code extensions, themes, and keybindings all carry over.

If you've used **RStudio**, Positron will feel familiar — it follows the same panel philosophy: editor top-left, console bottom-left, environment/variables top-right, plots bottom-right.

**Four panels to know during this workshop:**

- **Variable Explorer** — shows every object currently in memory (name, type, value). Replaces the habit of calling `print(df)` just to check something exists.
- **Data Viewer** — click any DataFrame in the Variable Explorer to open a spreadsheet-style view. No code required.
- **Integrated Console** — an interactive Python session running alongside your notebook. Useful for quick experiments without cluttering the notebook.
- **Plots Pane** — seaborn and matplotlib output renders here inline and persists between runs.
```

### Tone

Concise — learners are skimming before setup. No subsections, no code cells, no links beyond the Posit homepage. The goal is "this is what you're looking at" not "here is a tutorial on Positron."

---

## Out of Scope

- Keyboard shortcuts reference (not needed for this audience at this stage)
- Screenshots or embedded images of the Positron UI
- Detailed virtual environment or terminal panel explanation (covered in the setup section that follows)
- Any changes to existing slides other than inserting the new one

---

## Files to Change

| File | Change |
|------|--------|
| `docs/python2_workshop_slides.md` | Insert new slide after the Colab → Positron slide |
| `python2_workshop.ipynb` | Insert new markdown cell after welcome cell, before Part 0 |
| `docs/python2_workshop_slides.html` | Regenerated via `npx marp ... --allow-local-files` |
| `docs/python2_workshop_slides.pptx` | Regenerated via `npx marp ... --allow-local-files` |
