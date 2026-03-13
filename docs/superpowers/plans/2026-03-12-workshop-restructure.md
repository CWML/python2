# Workshop Restructure Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure the Python 2 workshop so slides are front-loaded (~20 min), then all remaining work happens inside Positron (setup, notebook, script demo) with no switching back to slides.

**Architecture:** Create three new files (`requirements.txt`, `analysis.py`, `outputs/.gitkeep`), edit four existing files (notebook, slides, README, .gitignore). The slides are reordered so conceptual content comes first and code-reference slides move to a labeled reference section. The notebook gets Part headers and a setup verification cell. A standalone `analysis.py` script is added as the end-of-class demo.

**Tech Stack:** MARP (slides), Jupyter notebook (`.ipynb` JSON), Python 3, pandas, seaborn, matplotlib

**Spec:** `docs/superpowers/specs/2026-03-12-workshop-restructure-design.md`

---

## Chunk 1: New Files

### Task 1: Create `requirements.txt`

**Files:**
- Create: `requirements.txt`

- [ ] **Step 1: Create the file**

```
pandas
seaborn
matplotlib
```

- [ ] **Step 2: Verify**

Run: `cat requirements.txt`
Expected: Three lines — `pandas`, `seaborn`, `matplotlib`

- [ ] **Step 3: Commit**

```bash
git add requirements.txt
git commit -m "Add requirements.txt for workshop dependencies"
```

---

### Task 2: Create `outputs/` directory and `.gitkeep`

**Files:**
- Create: `outputs/.gitkeep`

- [ ] **Step 1: Create the directory and placeholder**

```bash
mkdir -p outputs
touch outputs/.gitkeep
```

- [ ] **Step 2: Verify**

Run: `ls -la outputs/`
Expected: `.gitkeep` file exists

- [ ] **Step 3: Commit**

```bash
git add outputs/.gitkeep
git commit -m "Add outputs directory for script artifacts"
```

---

### Task 3: Create `analysis.py`

**Files:**
- Create: `analysis.py`

- [ ] **Step 1: Create the file**

Write the following to `analysis.py`:

```python
"""
OASIS-1 Dementia Analysis
Python 2 Workshop — Cushing/Whitney Medical Library, Yale University

This script reproduces the full analysis from the workshop notebook
as a standalone, reproducible Python script.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Load ---
df = pd.read_csv("data/oasis_cross-sectional.csv")
print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# --- Clean ---
df = df.drop(columns=["Hand", "Delay"])
df = df.dropna()
df = df.rename(columns={"M/F": "Gender", "nWBV": "BrainVolume"})
df["CDR"] = df["CDR"].astype(str)
print(f"After cleaning: {df.shape[0]} rows")

# --- Explore ---
print("\nDementia rating distribution:")
print(df["CDR"].value_counts())

# --- Analyze ---
print("\nMean brain volume by dementia rating:")
print(df.groupby("CDR")["BrainVolume"].agg(["mean", "count"]))

# --- Visualize ---
sns.boxplot(data=df, x="CDR", y="BrainVolume", order=["0.0", "0.5", "1.0", "2.0"])
plt.title("Brain Volume by Dementia Rating")
plt.savefig("outputs/brain_volume_by_cdr.png")
print("\nPlot saved to outputs/brain_volume_by_cdr.png")

# --- Save ---
df.to_csv("data/oasis_cleaned.csv", index=False)
print("Cleaned data saved to data/oasis_cleaned.csv")
```

- [ ] **Step 2: Verify the script runs**

Run: `cd /Users/justin/Documents/GitHub/CWML-python2 && python3 analysis.py`

Expected output (approximately):
```
Loaded: 436 rows, 12 columns
After cleaning: 216 rows

Dementia rating distribution:
CDR
0.0    133
0.5     57
1.0     24
2.0      2
Name: count, dtype: int64

Mean brain volume by dementia rating:
         mean  count
CDR
0.0  0.769188    133
0.5  0.728175     57
1.0  0.705500     24
2.0  0.684000      2

Plot saved to outputs/brain_volume_by_cdr.png
Cleaned data saved to data/oasis_cleaned.csv
```

Also verify: `ls outputs/brain_volume_by_cdr.png` — file should exist.

- [ ] **Step 3: Commit**

```bash
git add analysis.py
git commit -m "Add analysis.py standalone script for end-of-class demo"
```

---

### Task 4: Update `.gitignore`

**Files:**
- Modify: `.gitignore`

- [ ] **Step 1: Add `outputs/*.png` to `.gitignore`**

Append the following line to `.gitignore`:

```
outputs/*.png
```

Do NOT add `.venv/` — it is already present on line 3.

- [ ] **Step 2: Verify**

Run: `cat .gitignore`
Expected: `outputs/*.png` appears at the end. `.venv/` appears only once (line 3).

- [ ] **Step 3: Commit**

```bash
git add .gitignore
git commit -m "Add outputs/*.png to gitignore"
```

---

## Chunk 2: Notebook Edits

### Task 5: Edit notebook — Cell 1 (overview) and Cell 2 (welcome)

**Files:**
- Modify: `python2_workshop.ipynb`

Note: The notebook is a JSON file. Cell IDs are 0-indexed (cell-0, cell-1, ...). Use the NotebookEdit tool or edit the JSON directly.

- [ ] **Step 1: Update Cell 1 time allocations**

Cell 1 (cell-1) is a markdown cell with the workshop outline. Replace **only the bullet list** (preserve the `## Workshop Notebook` heading and `Python 2 for Data Analysis:` line above it):

Replace:

```
- 10 minutes — Environment orientation, dataset introduction
- 35 minutes — Introduction to pandas: loading data, inspecting, selecting
- 40 minutes — Data cleaning & transformation
- 20 minutes — Grouping, aggregation & research questions
- 10 minutes — Bonus: seaborn visualization
- 5 minutes — Wrap-up & resources
```

With:

```
- Part 0 — Setup verification
- Part 1 — Introduction to pandas: loading data, inspecting, selecting
- Part 2 — Data cleaning & transformation
- Part 3 — Grouping, aggregation & research questions
- Part 4 — Visualization with seaborn (time permitting)
```

Note: "Wrap-up & resources" is intentionally removed from the notebook outline — wrap-up happens verbally after the notebook.

- [ ] **Step 2: Update Cell 2 — change "VS Code (or Positron)" to "Positron"**

Cell 2 (cell-2) is a markdown cell. Find and replace:

`You're using VS Code (or Positron) with a local Python installation and a virtual environment.`

With:

`You're using Positron with a local Python installation and a virtual environment.`

- [ ] **Step 3: Verify changes**

Read cell-1 and cell-2 to confirm the edits are correct.

---

### Task 6: Edit notebook — Insert Part 0 setup verification cell

**Files:**
- Modify: `python2_workshop.ipynb`

- [ ] **Step 1: Insert a new code cell after cell-2**

This becomes the new cell-3 (all subsequent cells shift by 1). Cell content:

```python
# Verify your environment is working
import pandas as pd
import seaborn as sns
print(f"pandas {pd.__version__}")
print(f"seaborn {sns.__version__}")
print("Setup complete!")
```

- [ ] **Step 2: Insert a Part 0 markdown header cell before the new code cell**

Insert a markdown cell after cell-2 and before the verification code cell:

```markdown
# Part 0: Setup Verification
```

This means two cells are inserted after cell-2: a markdown header, then the code cell.

- [ ] **Step 3: Verify**

Read the notebook cells around positions 2-5 to confirm:
- cell-2: Welcome markdown (unchanged)
- cell-3 (new): `# Part 0: Setup Verification` markdown
- cell-4 (new): Setup verification code cell
- cell-5 (was cell-3): `# Introduction to pandas` markdown

---

### Task 7: Edit notebook — Rename section heading cells

**Files:**
- Modify: `python2_workshop.ipynb`

Note: After Task 6, cell indices have shifted by 2. The original cell numbers from the spec are pre-edit. Use the heading text to locate cells, not index numbers.

- [ ] **Step 1: Rename the "Introduction to pandas" heading**

Find the markdown cell containing `# Introduction to pandas` and change it to:

```markdown
# Part 1: Introduction to pandas
```

- [ ] **Step 2: Rename the "Data Cleaning" heading**

Find the markdown cell containing `# Data Cleaning` (the one that starts the Data Cleaning section, not sub-headings) and change it to:

```markdown
# Part 2: Data Cleaning
```

- [ ] **Step 3: Rename the "Asking Research Questions" heading**

Find the markdown cell containing `# Asking Research Questions with groupby` and change it to:

```markdown
# Part 3: Asking Research Questions with groupby
```

- [ ] **Step 4: Rename the "Bonus: Visualization" heading**

Find the markdown cell containing `# Bonus: Visualization with seaborn` and change it to:

```markdown
# Part 4: Visualization with seaborn
```

- [ ] **Step 5: Verify all Part headings**

Search the notebook for cells starting with `# Part` to confirm all five exist:
- `# Part 0: Setup Verification`
- `# Part 1: Introduction to pandas`
- `# Part 2: Data Cleaning`
- `# Part 3: Asking Research Questions with groupby`
- `# Part 4: Visualization with seaborn`

- [ ] **Step 6: Verify notebook JSON is valid**

Run: `python3 -c "import json; json.load(open('python2_workshop.ipynb')); print('Valid JSON')"`
Expected: `Valid JSON`

- [ ] **Step 7: Commit all notebook changes (Tasks 5-7)**

```bash
git add python2_workshop.ipynb
git commit -m "Add Part headers and setup verification cell to notebook"
```

---

## Chunk 3: Slides Edits

### Task 8: Reorder slides for front-loaded delivery

**Files:**
- Modify: `docs/python2_workshop_slides.md`

This is the most complex edit. The slide deck is a single MARP markdown file where `---` separates slides. The CSS block at the top (lines 1-301) must not be touched.

**Clarifications:**
- The "Part 0" lead slide ("Your New Development Environment") is intentionally kept — it introduces the Colab→Positron narrative that the next slide expands on.
- The spec's Phase 3 timeline uses 5 fine-grained Parts for scheduling purposes. The notebook and slides use 4 Parts (Part 1 combines loading + inspecting + selecting). Follow the notebook's 4-Part structure.

**Current slide order (after CSS):**
1. Title (line 303)
2. Agenda (line 314)
3. Learning Objectives (line 331)
4. Part 0 lead (line 344)
5. Colab → Positron (line 352)
6. OASIS-1 dataset (line 383)
7. Part 1 lead (line 400)
8. Defining Data Cleaning (line 408)
9. Determining What to Clean (line 424)
10. Cleaning vs. Transformation (line 441)
11. Part 2 lead (line 472)
12. What Is pandas (line 480)
13. DataFrame & Series (line 508)
14. `.loc[]` (line 546)
15. `.iloc[]` (line 568)
16. SettingWithCopyWarning (line 586)
17. "Let's Code!" transition (line 609)
18. Part 3 lead (line 619)
19. Split-Apply-Combine (line 627)
20. Bonus lead (line 660)
21. Seaborn (line 668)
22. Wrap-up lead (line 696)
23. Today We (line 704)
24. AI Pair Programmer (line 717)
25. Resources (line 753)
26. Thank You (line 780)

**Target slide order:**

**Live presentation slides (1-10):**
1. Title (no change)
2. Agenda (update timings)
3. Learning Objectives (no change)
4. Part 0 lead — "Your New Development Environment" (no change)
5. Colab → Positron (no change)
6. OASIS-1 dataset (no change)
7. Defining Data Cleaning (no change)
8. Determining What to Clean (no change)
9. Cleaning vs. Transformation (no change)
10. What Is pandas (no change)
11. **NEW: "Let's Set Up Your Environment" transition slide**

**Reference section (after a divider):**
12. **NEW: "Reference Slides" divider**
13. DataFrame & Series
14. `.loc[]`
15. `.iloc[]`
16. SettingWithCopyWarning
17. Split-Apply-Combine
18. Seaborn (with fixes)
19. Today We (wrap-up)
20. AI Pair Programmer
21. Resources
22. Thank You

**Slides removed:**
- "Part 1" lead (line 400) — merged into data cleaning sequence
- "Part 2" lead (line 472) — merged into pandas sequence
- "Let's Code!" transition (line 609) — replaced by new transition
- "Part 3" lead (line 619) — not needed in reference section
- "Bonus" lead (line 660) — not needed in reference section
- "Wrap-up" lead (line 696) — not needed in reference section

- [ ] **Step 1: Update the agenda slide timings**

Find the agenda table (currently lines 316-323) and replace it with:

```markdown
| Time | Topic |
|------|-------|
| 20 min | Conceptual overview (slides) |
| 15 min | Live environment setup |
| 70 min | Hands-on notebook: pandas, cleaning, groupby, seaborn |
| 12 min | Script demo: `analysis.py` |
| 3 min  | Wrap-up & resources |
```

- [ ] **Step 2: Reorder the slides**

Restructure the content after the CSS block into the target order listed above. This involves:
- Moving the data cleaning slides (currently slides 7-10) to come before What Is pandas (currently slide 12)
- Removing the Part 1/Part 2/Part 3/Bonus/Wrap-up lead slides
- Removing the "Let's Code!" transition slide
- Adding the new transition slide after "What Is pandas"
- Adding the "Reference Slides" divider
- Moving remaining slides into the reference section

The exact new content order after the CSS block:

```
[Title slide — no change]
---
[Agenda slide — updated timings]
---
[Learning Objectives slide — no change]
---
[Part 0 lead: "Your New Development Environment" — no change]
---
[Colab → Positron slide — no change]
---
[OASIS-1 dataset slide — no change]
---
[Defining Data Cleaning slide — no change]
---
[Determining What to Clean slide — no change]
---
[Cleaning vs. Transformation slide — no change]
---
[What Is pandas slide — no change]
---
<!-- _class: lead -->

# Let's Set Up Your Environment

## Open Positron and follow along

*Terminal → virtual environment → install packages → open notebook*

---

<!-- _class: lead -->

# Reference Slides

## Additional material for self-study

---
[DataFrame & Series slide — no change]
---
[.loc[] slide — no change]
---
[.iloc[] slide — no change]
---
[SettingWithCopyWarning slide — no change]
---
[Split-Apply-Combine slide — no change]
---
[Seaborn slide — WITH FIXES from Step 3]
---
[Today We slide — no change]
---
[AI Pair Programmer slide — no change]
---
[Resources slide — no change]
---
[Thank You slide — no change]
```

- [ ] **Step 3: Fix the seaborn slide**

On the seaborn slide, make two changes:

Change line with `y="nWBV"` on the boxplot:
```python
sns.boxplot(data=df_clinical, x="CDR", y="BrainVolume", palette="Blues")
```

Change lines with `y="nWBV"` and `order=` on the barplot:
```python
sns.barplot(data=df_clinical, x="CDR", y="BrainVolume",
            order=["0.0", "0.5", "1.0", "2.0"], palette="Blues_d")
```

- [ ] **Step 4: Verify the slide structure**

Search the file for `---` separators and count slides. Verify:
- The first slide after CSS is the title
- "Let's Set Up Your Environment" appears before "Reference Slides"
- No "Let's Code!" slide remains
- No orphan Part lead slides remain (Part 1, Part 2, Part 3, Bonus, Wrap-up leads are removed)
- Seaborn slide uses `y="BrainVolume"` and `order=["0.0", ...]`

- [ ] **Step 5: Commit**

```bash
git add docs/python2_workshop_slides.md
git commit -m "Reorder slides for front-loaded delivery with reference section"
```

---

## Chunk 4: README and .gitignore

### Task 9: Update README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Standardize venv name to `.venv`**

In the "Create a virtual environment" section, replace:

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

With:

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

- [ ] **Step 2: Replace manual pip install with requirements.txt**

Replace:

```bash
pip install pandas seaborn matplotlib jupyter
```

With:

```bash
pip install -r requirements.txt
```

- [ ] **Step 3: Update repository contents tree**

Replace the current file tree:

```
python2/
├── python2_workshop.ipynb        # Main workshop notebook
├── data/
│   ├── oasis_cross-sectional.csv # Raw OASIS-1 dataset
│   └── oasis_cleaned.csv         # Cleaned dataset (produced during workshop)
└── docs/
    ├── python2_workshop_slides.html  # Slide deck (open in any browser)
    ├── python2_workshop_slides.pptx  # PowerPoint version
    └── python2_workshop_slides.md    # MARP source (editable)
```

With:

```
python2/
├── python2_workshop.ipynb           # Main workshop notebook
├── analysis.py                      # Standalone script (end-of-class demo)
├── requirements.txt                 # Python dependencies
├── data/
│   ├── oasis_cross-sectional.csv    # Raw OASIS-1 dataset
│   └── oasis_cleaned.csv            # Cleaned dataset (produced during workshop)
├── outputs/                         # Script output (plots)
└── docs/
    ├── python2_workshop_slides.html # Slide deck (open in any browser)
    ├── python2_workshop_slides.pptx # PowerPoint version
    └── python2_workshop_slides.md   # MARP source (editable)
```

- [ ] **Step 4: Update the "What We Cover" table**

Replace the current table:

```markdown
| Time | Topic |
|------|-------|
| 10 min | Environment orientation & dataset introduction |
| 35 min | Intro to pandas: loading, inspecting, selecting |
| 40 min | Data cleaning & transformation |
| 20 min | Grouping & aggregation with `.groupby()` |
| 10 min | Bonus: seaborn visualization |
| 5 min  | Wrap-up & resources |
```

With:

```markdown
| Time | Topic |
|------|-------|
| 20 min | Conceptual overview (slides) |
| 15 min | Live environment setup |
| 70 min | Hands-on notebook: pandas, cleaning, groupby, seaborn |
| 12 min | Script demo: `analysis.py` |
| 3 min  | Wrap-up & resources |
```

- [ ] **Step 5: Verify**

Read `README.md` and confirm:
- `.venv` appears in setup steps (not `venv`)
- `pip install -r requirements.txt` appears (not manual package list)
- File tree includes `analysis.py`, `requirements.txt`, and `outputs/`
- "What We Cover" table matches new timings

- [ ] **Step 6: Commit**

```bash
git add README.md
git commit -m "Update README: .venv, requirements.txt, updated file tree"
```

---

## Chunk 5: Regenerate Slides and Final Verification

### Task 10: Regenerate slide outputs

**Files:**
- Regenerate: `docs/python2_workshop_slides.html`
- Regenerate: `docs/python2_workshop_slides.pptx`

- [ ] **Step 1: Install MARP dependencies (if needed)**

```bash
cd /Users/justin/Documents/GitHub/CWML-python2
npm install
```

- [ ] **Step 2: Regenerate HTML and PPTX from the edited markdown**

```bash
npx marp docs/python2_workshop_slides.md --html --output docs/python2_workshop_slides.html
npx marp docs/python2_workshop_slides.md --pptx --output docs/python2_workshop_slides.pptx
```

- [ ] **Step 3: Verify outputs exist**

```bash
ls -la docs/python2_workshop_slides.html docs/python2_workshop_slides.pptx
```

Both files should exist with recent timestamps.

- [ ] **Step 4: Commit regenerated slides**

```bash
git add docs/python2_workshop_slides.html docs/python2_workshop_slides.pptx
git commit -m "Regenerate HTML and PPTX slides from updated markdown"
```

---

### Task 11: Final verification and push

- [ ] **Step 1: Run `analysis.py` to confirm it still works end-to-end**

```bash
cd /Users/justin/Documents/GitHub/CWML-python2
python3 analysis.py
```

Expected: Clean output with no errors, plot saved to `outputs/`, cleaned CSV saved to `data/`.

- [ ] **Step 2: Verify git status is clean**

```bash
git status
```

Expected: `nothing to commit, working tree clean`

- [ ] **Step 3: Review commit history**

```bash
git log --oneline -10
```

Expected: 6-7 new commits covering requirements.txt, outputs dir, analysis.py, gitignore, notebook edits, slides reorder, README update, and slide regeneration.

- [ ] **Step 4: Push to origin**

```bash
git push
```
