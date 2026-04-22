# Positron Slide + Notebook Orientation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a "What Is Positron?" slide to the deck and a brief Positron orientation cell to the notebook.

**Architecture:** Two independent content edits — one to the MARP markdown slide source, one to the Jupyter notebook JSON — followed by rebuilding the HTML and PPTX outputs from the slide source.

**Tech Stack:** MARP CLI (`npx marp --allow-local-files`), Jupyter notebook JSON (`.ipynb`), HTML/CSS within MARP's inline style block.

---

## File Map

| File | Change |
|------|--------|
| `docs/python2_workshop_slides.md` | Insert new slide after line 380 (after the Colab → Positron slide's closing `---`) |
| `python2_workshop.ipynb` | Insert new markdown cell between the `## Welcome to Python 2!` cell and `# Part 0: Setup Verification` |
| `docs/python2_workshop_slides.html` | Regenerated output — do not edit directly |
| `docs/python2_workshop_slides.pptx` | Regenerated output — do not edit directly |

---

## Task 1: Add the Positron slide to the slide deck

**Files:**
- Modify: `docs/python2_workshop_slides.md` — insert after the closing `---` of the Colab → Positron slide (after the `<div class="callout">` block that ends with `</div>\n\n---\n\n# Today's Dataset`)

- [ ] **Step 1: Insert the new slide**

Open `docs/python2_workshop_slides.md`. Find this exact block (around line 376–382):

```
<div class="callout">
<strong>Virtual environment:</strong> an isolated Python installation for this project only. Keeps dependencies clean and reproducible.
</div>

---

# Today's Dataset: OASIS-1
```

Replace it with:

```
<div class="callout">
<strong>Virtual environment:</strong> an isolated Python installation for this project only. Keeps dependencies clean and reproducible.
</div>

---

# What Is Positron?

**A data science IDE built by [Posit](https://posit.co/) — the team behind RStudio**

- Fork of **VS Code** — extensions, themes, and keybindings all carry over
- Supports Python **and** R in the same environment

<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px;">
<div style="background:var(--gray-bg);border-radius:6px;padding:12px 16px;">
<strong style="color:var(--yale-blue);">Variable Explorer</strong><br>
Browse every live object in memory — name, type, value
</div>
<div style="background:var(--gray-bg);border-radius:6px;padding:12px 16px;">
<strong style="color:var(--yale-blue);">Data Viewer</strong><br>
Inspect DataFrames visually — no <code>print()</code> needed
</div>
<div style="background:var(--gray-bg);border-radius:6px;padding:12px 16px;">
<strong style="color:var(--yale-blue);">Integrated Console</strong><br>
Run code interactively, line-by-line, alongside the notebook
</div>
<div style="background:var(--gray-bg);border-radius:6px;padding:12px 16px;">
<strong style="color:var(--yale-blue);">Plots Pane</strong><br>
Inline chart output, persisted across runs
</div>
</div>

<div class="callout" style="margin-top:16px;">
If you've used <strong>RStudio</strong>, this layout will feel immediately familiar. If you've used <strong>VS Code</strong>, your extensions and keybindings carry over.
</div>

---

# Today's Dataset: OASIS-1
```

- [ ] **Step 2: Rebuild slide outputs and verify**

```bash
npx marp docs/python2_workshop_slides.md --html --pptx --allow-local-files
```

Expected output:
```
[  INFO ] Converting 1 markdown...
[  INFO ] docs/python2_workshop_slides.md => docs/python2_workshop_slides.html
[  INFO ] docs/python2_workshop_slides.md => docs/python2_workshop_slides.pptx
```

Then open `docs/python2_workshop_slides.html` in a browser. Confirm:
- The new "What Is Positron?" slide appears between the Colab → Positron slide and the OASIS-1 dataset slide
- The 2×2 panel grid renders correctly with teal headings and gray-bg cards
- The callout box at the bottom renders in the standard teal-left-border style
- No layout overflow (all content fits within the slide boundaries)

- [ ] **Step 3: Commit**

```bash
git add docs/python2_workshop_slides.md docs/python2_workshop_slides.html docs/python2_workshop_slides.pptx
git commit -m "Add What Is Positron? slide after Colab → Positron comparison"
```

---

## Task 2: Add Positron orientation cell to the notebook

**Files:**
- Modify: `python2_workshop.ipynb` — insert new markdown cell between the `## Welcome to Python 2!` cell and the `# Part 0: Setup Verification` cell

- [ ] **Step 1: Insert the orientation markdown cell**

Open `python2_workshop.ipynb`. Find the cell with this source (it is a markdown cell):

```
## Welcome to Python 2!
```

Insert a **new markdown cell immediately after it** (before the `# Part 0: Setup Verification` cell) with this exact source:

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

Use the `NotebookEdit` tool with `insert_after` targeting the `## Welcome to Python 2!` cell, or edit the raw JSON directly. If editing JSON directly, the new cell object is:

```json
{
  "cell_type": "markdown",
  "id": "positron-orientation",
  "metadata": {},
  "source": "## Your Development Environment: Positron\n\nPositron is a **data science IDE** built by [Posit](https://posit.co/) — the team behind RStudio. It is a fork of VS Code, which means your VS Code extensions, themes, and keybindings all carry over.\n\nIf you've used **RStudio**, Positron will feel familiar — it follows the same panel philosophy: editor top-left, console bottom-left, environment/variables top-right, plots bottom-right.\n\n**Four panels to know during this workshop:**\n\n- **Variable Explorer** — shows every object currently in memory (name, type, value). Replaces the habit of calling `print(df)` just to check something exists.\n- **Data Viewer** — click any DataFrame in the Variable Explorer to open a spreadsheet-style view. No code required.\n- **Integrated Console** — an interactive Python session running alongside your notebook. Useful for quick experiments without cluttering the notebook.\n- **Plots Pane** — seaborn and matplotlib output renders here inline and persists between runs."
}
```

- [ ] **Step 2: Verify the notebook structure**

```bash
python3 -c "
import json
nb = json.load(open('python2_workshop.ipynb'))
cells = nb['cells']
for i, c in enumerate(cells):
    src = c['source'] if isinstance(c['source'], str) else ''.join(c['source'])
    if 'Welcome to Python 2' in src or 'Positron' in src[:40] or 'Part 0' in src:
        print(f'Cell {i} [{c[\"cell_type\"]}]: {src[:60].strip()}')
"
```

Expected output (order matters):
```
Cell 2 [markdown]: ## Welcome to Python 2!
Cell 3 [markdown]: ## Your Development Environment: Positron
Cell 4 [markdown]: # Part 0: Setup Verification
```

- [ ] **Step 3: Commit**

```bash
git add python2_workshop.ipynb
git commit -m "Add Positron orientation cell to notebook after welcome section"
```
