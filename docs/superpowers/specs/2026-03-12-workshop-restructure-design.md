# Python 2 Workshop Restructure — Design Spec

**Date:** 2026-03-12
**Repo:** CWML/python2
**Status:** Approved

---

## Problem

The current workshop materials interleave slides and notebook work, requiring 4-5 context switches between a presentation deck and Positron during a 2-hour session. This disrupts flow, creates window management overhead, and undermines the core pedagogical goal: showing students how to work in a local Python environment.

Additionally, the workshop uses a notebook exclusively. While notebooks are excellent for teaching, the course's purpose is to graduate students from browser-based tools (Google Colab) to local Python development. A notebook-only class doesn't fully deliver on that promise.

## Approach

**Front-loaded slides → Positron for the rest.** One clean transition from presentation to IDE. Slides handle conceptual framing (~20 min), then everything else happens inside Positron: live environment setup, notebook-based exploration, and a script demo at the end.

### Rejected alternatives

- **Back-and-forth slides/notebook (current):** Too many context switches during coding.
- **Notebook only, no slides:** Loses the polished CWML-branded opening and conceptual scaffolding that benefits from a presentation format.

---

## Workshop Flow

### Phase 1 — Slides (~20 min)

| Time  | Content |
|-------|---------|
| 0:00  | Title, agenda, learning objectives |
| 0:05  | "From Colab → Positron" — why local matters |
| 0:08  | What is data cleaning vs. transformation (3 slides) |
| 0:12  | What is pandas, DataFrame vs. Series |
| 0:15  | OASIS-1 dataset introduction, research question |
| 0:18  | Transition slide: "Let's Set Up Your Environment" |

Close slides. Everything after this happens in Positron.

### Phase 2 — Positron: Live Setup (~15 min)

| Time  | Activity |
|-------|----------|
| 0:20  | Terminal: `python3 -m venv .venv`, activate, `pip install -r requirements.txt` |
| 0:28  | Open notebook, select `.venv` kernel |
| 0:32  | Run setup verification cell |
| 0:35  | Checkpoint: "Everyone seeing a version number?" |

### Phase 3 — Positron: Notebook (~70 min)

| Time  | Notebook Section |
|-------|-----------------|
| 0:35  | Part 1: Loading & inspecting data |
| 0:55  | Part 2: Selecting data (bracket notation, `.loc[]`, boolean filters) |
| 1:10  | Part 3: Data cleaning (missing data, drop, dropna, rename, astype) |
| 1:35  | Part 4: Groupby & research question |
| 1:45  | Part 5: Seaborn visualization (time permitting) |

### Phase 4 — Positron: Script Demo (~12 min)

| Time  | Activity |
|-------|----------|
| 1:45  | Open `analysis.py` in Positron editor |
| 1:48  | Walk through the script (or live-build it) |
| 1:52  | Run `python analysis.py` in terminal |
| 1:54  | "Notebooks explore, scripts reproduce" |

Note: Phase 4 starts at 1:45 if seaborn is skipped, or later if seaborn runs. The script demo flexes to fill remaining time.

### Wrap-up (3 min)

| Time  | Activity |
|-------|----------|
| 1:57  | Recap |
| 2:00  | Resources, contact, thank you |

---

## File Changes

### New files

#### `requirements.txt`

```
pandas
seaborn
matplotlib
```

#### `analysis.py`

Standalone script that reproduces the full notebook analysis: load → clean → explore → analyze → visualize → save. Runs with `python analysis.py` in the terminal. Outputs a boxplot PNG to `outputs/` and saves cleaned data to `data/oasis_cleaned.csv`.

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

#### `outputs/.gitkeep`

Empty file to ensure the directory exists in git.

### Edited files

#### `python2_workshop.ipynb`

Note: All cell numbers below refer to the current notebook before edits. Inserting the new Part 0 cell (step 3) will shift subsequent cell indices by one.

1. **Cell 1 (overview):** Update time allocations to reflect in-notebook flow (setup is separate).
2. **Cell 2 (welcome):** Change "VS Code (or Positron)" to "Positron".
3. **New cell after Cell 2:** Part 0 — Setup verification code cell:
   ```python
   import pandas as pd
   import seaborn as sns
   print(f"pandas {pd.__version__}")
   print(f"seaborn {sns.__version__}")
   print("Setup complete!")
   ```
4. **Rename existing section heading cells** to include Part numbers (do not add new cells — modify the existing headings to avoid redundancy):
   - Cell 3: `# Introduction to pandas` → `# Part 1: Introduction to pandas`
   - Cell 33: `# Data Cleaning` → `# Part 2: Data Cleaning`
   - Cell 58: `# Asking Research Questions with groupby` → `# Part 3: Asking Research Questions with groupby`
   - Cell 68: `# Bonus: Visualization with seaborn` → `# Part 4: Visualization with seaborn`
5. No content is deleted. Existing cells, markdown, and outputs all remain.

#### `docs/python2_workshop_slides.md`

1. **Reorder for front-loaded delivery.** First ~8 slides are the live presentation:
   - Title → Agenda (updated timings) → Objectives → Colab vs. Positron → OASIS-1 dataset → Data cleaning concepts (3 slides) → What is pandas → **New transition slide: "Let's Set Up Your Environment"**
2. **Everything after the transition slide becomes a "Reference" section:** DataFrame/Series, `.loc[]`, `.iloc[]`, SettingWithCopyWarning, Split-Apply-Combine, Seaborn, AI Pair Programmer, Wrap-up/Resources/Thank You.
3. **Fix seaborn slide:** Change `y="nWBV"` to `y="BrainVolume"` on both the boxplot and barplot examples. Change `order=[0, 0.5, 1, 2]` to `order=["0.0", "0.5", "1.0", "2.0"]` on the barplot (the boxplot does not currently have an `order` parameter).
4. **Remove the existing "Let's Code!" transition slide** (lines 609-616) — it is replaced by the new "Let's Set Up Your Environment" transition slide.
5. **Add a "Reference Slides" divider** (`<!-- _class: lead -->` slide) before the reference section to clearly separate presented slides from reference material.
6. **New transition slide markup:**
   ```markdown
   <!-- _class: lead -->

   # Let's Set Up Your Environment

   ## Open Positron and follow along

   *Terminal → virtual environment → install packages → open notebook*
   ```
7. **Update agenda slide** with the two-phase structure:

   | Time | Topic |
   |------|-------|
   | 20 min | Conceptual overview (slides) |
   | 15 min | Live environment setup |
   | 70 min | Hands-on notebook: pandas, cleaning, groupby, seaborn |
   | 12 min | Script demo: `analysis.py` |
   | 3 min  | Wrap-up & resources |

#### `README.md`

1. **Setup step 3:** Standardize venv name from `venv` to `.venv` (Positron auto-detects `.venv`).
2. **Setup step 4:** Replace `pip install pandas seaborn matplotlib jupyter` with `pip install -r requirements.txt`.
3. **Repository contents:** Add `analysis.py`, `requirements.txt`, and `outputs/` to the file tree.

#### `.gitignore`

Add `outputs/*.png`. Note: `.venv/` is already present in the current `.gitignore` — do not duplicate it.

---

## What does NOT change

- The notebook's pedagogical content (all 76 existing cells remain)
- The slide deck's visual design (CWML/Yale branding, CSS)
- The dataset (`data/oasis_cross-sectional.csv`)
- The learning objectives (already in both README and slides)
- The AI pair programming appendix in the notebook

---

## Clarifications

- **`jupyter` intentionally dropped from dependencies.** Positron handles notebook kernels natively; the `jupyter` package is not required. If a student needs a fallback, they can install it manually.
- **`data/oasis_cleaned.csv` is kept.** It ships as a pre-built reference. Both the notebook and `analysis.py` overwrite it during execution — this is expected.
- **Phase timing is flexible.** Seaborn (Part 5) is "time permitting." If skipped, Phase 4 (script demo) starts at 1:45 and gets more time. If seaborn runs, the script demo compresses. The 2-minute buffer between Phase 1 (ends 0:18) and Phase 2 (starts 0:20) accounts for closing slides and switching to Positron.
