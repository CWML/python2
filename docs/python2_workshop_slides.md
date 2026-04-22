---
marp: true
theme: default
paginate: true
style: |
  /* ══════════════════════════════════════════════
     CWML / Yale Brand — Design Assets v2026
     Primary:   Teal       #00a0ab
     Accent:    Green      #b8df72  (decorative only — no text)
     Secondary: Yale Blue  #00356b
     Link/Lab:  Lt Blue    #286dc0
     Body text: Dark Gray  #4a4a4a
     Deep gray: #222222
     Headings:  Georgia, serif
     Body:      Verdana, sans-serif
  ══════════════════════════════════════════════ */

  :root {
    --cwml-teal:    #00a0ab;
    --cwml-teal-sm: #00828b;   /* accessible teal at small sizes */
    --cwml-green:   #b8df72;   /* accent only — never for text */
    --yale-blue:    #00356b;
    --yale-ltblue:  #286dc0;
    --gray-body:    #4a4a4a;
    --gray-deep:    #222222;
    --gray-bg:      #F2F8F8;   /* faint teal-tinted background */
    --white:        #FFFFFF;
  }

  /* ── Base slide ── */
  section {
    background: var(--white);
    color: var(--gray-body);
    font-family: 'Verdana', 'Segoe UI', sans-serif;
    font-size: 21px;
    padding: 52px 60px 44px 60px;
  }

  /* ── Header bar behind every h1 ── */
  section h1 {
    font-family: 'Georgia', 'YaleNew', serif;
    color: var(--white);
    background: var(--cwml-teal);
    font-size: 1.6em;
    padding: 10px 24px;
    margin: -52px -60px 28px -60px;
    border-bottom: 5px solid var(--cwml-green);
    letter-spacing: 0.01em;
  }

  /* ── h2 / h3 on regular slides ── */
  section h2 {
    font-family: 'Georgia', 'YaleNew', serif;
    color: var(--cwml-teal-sm);
    font-size: 1.1em;
    margin-top: 0.3em;
  }
  section h3 {
    font-family: 'Georgia', 'YaleNew', serif;
    color: var(--yale-blue);
    font-size: 0.95em;
  }

  /* ── Tables ── */
  section table {
    border-collapse: collapse;
    width: 100%;
    font-size: 0.88em;
    margin-top: 10px;
  }
  section table th {
    background: var(--cwml-teal);
    color: var(--white);
    font-family: 'Georgia', serif;
    padding: 7px 12px;
    text-align: left;
  }
  section table td {
    padding: 6px 12px;
    border-bottom: 1px solid #d0e8ea;
    color: var(--gray-body);
  }
  section table tr:nth-child(even) td { background: var(--gray-bg); }

  /* ── Bullet tweaks ── */
  section ul { padding-left: 1.4em; }
  section ul li { margin-bottom: 0.35em; line-height: 1.5; }
  section ul ul { font-size: 0.88em; color: #666; }
  section ul ul li { margin-bottom: 0.12em; }

  /* ── Inline code ── */
  section code {
    background: #E6F6F7;
    color: var(--cwml-teal-sm);
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 0.88em;
  }

  /* ── Code blocks ── */
  section pre {
    background: #1e3a3c;
    border-left: 5px solid var(--cwml-green);
    border-radius: 6px;
    padding: 18px 24px;
    font-size: 0.9em;
    line-height: 1.85;
    margin-top: 12px;
  }
  section pre code {
    background: transparent;
    color: #e8f5e9;
    padding: 0;
  }

  /* ── Syntax highlight token overrides (brighter for TV) ── */
  /* strings: bright sky blue */
  section pre .hljs-string { color: #7dd3fc; }
  /* numbers, literals, variables, constants: vivid cyan */
  section pre .hljs-number,
  section pre .hljs-literal,
  section pre .hljs-variable,
  section pre .hljs-attr { color: #67e8f9; }
  /* keywords: soft violet */
  section pre .hljs-keyword,
  section pre .hljs-type { color: #c4b5fd; }
  /* built-ins: warm amber */
  section pre .hljs-built_in,
  section pre .hljs-title.function_ { color: #fcd34d; }
  /* comments: medium gray-green — readable but de-emphasised */
  section pre .hljs-comment { color: #86efac; font-style: italic; }

  /* ── Classroom/TV: extra-large code ── */
  section.classroom pre {
    background: #22474a;
    font-size: 1.05em;
    line-height: 2.0;
    padding: 22px 28px;
    margin-top: 18px;
  }
  section.classroom pre code {
    font-size: 1em;
    color: #f0faf0;
  }
  section.classroom p,
  section.classroom ul { font-size: 0.92em; }

  /* ── Blockquotes ── */
  section blockquote {
    border-left: 4px solid var(--cwml-green);
    background: var(--gray-bg);
    margin: 12px 0 0 0;
    padding: 8px 16px;
    border-radius: 0 6px 6px 0;
    font-size: 0.88em;
    color: var(--gray-body);
  }

  /* ── Footer / pagination ── */
  section::after {
    font-size: 12px;
    color: #aaa;
    font-family: Verdana, sans-serif;
    content: 'Python 2 · CWML Yale · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
  }

  /* ═══════════════════════════════════════
     LEAD slides — full-teal section breaks
  ═══════════════════════════════════════ */
  section.lead {
    background: var(--cwml-teal);
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.lead h1 {
    font-family: 'Georgia', 'YaleNew', serif;
    background: none;
    border: none;
    margin: 0;
    padding: 0;
    font-size: 2.4em;
    color: var(--white);
    letter-spacing: 0.02em;
  }
  section.lead h2 {
    font-family: Verdana, sans-serif;
    color: var(--cwml-green);
    font-size: 1.25em;
    font-weight: 400;
    margin-top: 0.5em;
  }
  section.lead p {
    color: rgba(255,255,255,0.75);
    font-size: 0.88em;
    margin-top: 1.2em;
  }
  section.lead::after { color: rgba(255,255,255,0.3); }

  /* ═══════════════════════════════════
     TITLE slide
  ═══════════════════════════════════ */
  section.title {
    background: linear-gradient(160deg, var(--yale-blue) 0%, var(--cwml-teal) 100%);
    color: var(--white);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.title h1 {
    font-family: 'Georgia', 'YaleNew', serif;
    background: none;
    border: none;
    margin: 0 0 0.25em 0;
    padding: 0;
    font-size: 2.0em;
    color: var(--white);
    line-height: 1.25;
  }
  section.title h2 {
    font-family: Verdana, sans-serif;
    color: var(--cwml-green);
    font-size: 1.1em;
    font-weight: 400;
    margin: 0;
  }
  section.title p {
    color: rgba(255,255,255,0.72);
    font-size: 0.86em;
    margin-top: 1.8em;
    border-top: 1px solid rgba(255,255,255,0.25);
    padding-top: 1em;
  }
  section.title::after { color: rgba(0,0,0,0); }

  /* ── Two-column helper ── */
  .cols {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 28px;
    margin-top: 10px;
  }
  .col { padding: 0; }
  .col-label {
    font-family: 'Georgia', serif;
    font-size: 0.82em;
    font-weight: 700;
    color: var(--white);
    background: var(--cwml-teal);
    text-transform: uppercase;
    letter-spacing: 0.07em;
    padding: 4px 10px;
    border-radius: 3px;
    margin-bottom: 10px;
    display: block;
  }
  .col ul { padding-left: 1.2em; font-size: 0.9em; }

  /* ── Callout box ── */
  .callout {
    background: #E6F6F7;
    border-left: 5px solid var(--cwml-teal);
    padding: 9px 15px;
    border-radius: 0 6px 6px 0;
    margin-top: 16px;
    font-size: 0.86em;
    color: var(--gray-deep);
  }
  .callout strong { color: var(--cwml-teal-sm); }

  /* ── Warning box ── */
  .warning {
    background: #f5faed;
    border-left: 5px solid var(--cwml-green);
    padding: 9px 15px;
    border-radius: 0 6px 6px 0;
    margin-top: 16px;
    font-size: 0.86em;
    color: var(--gray-deep);
  }
  .warning strong { color: #4a6a00; }

  /* ── Image placeholder boxes ── */
  .img-placeholder {
    border: 2px dashed #00a0ab55;
    background: var(--gray-bg);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--cwml-teal-sm);
    font-size: 0.8em;
    text-align: center;
    padding: 14px;
  }
---

<!-- _class: title -->

# Python 2: Data Analysis with pandas

## Cleaning, Transforming, and Analyzing Real Data

Cushing/Whitney Medical Library · Yale University
*Building on Python 1 — moving from Google Colab to Positron on your local machine*

---

# Today's Agenda

| Time | Topic |
|------|-------|
| 20 min | Conceptual overview (slides) |
| 15 min | Live environment setup |
| 70 min | Hands-on notebook: pandas, cleaning, groupby, seaborn |
| 12 min | Script demo: `analysis.py` |
| 3 min  | Wrap-up & resources |

<div class="callout">
<strong>Note:</strong> All code and this notebook will be shared after class. You don't need to keep up perfectly — focus on understanding the concepts.
</div>

---

# Learning Objectives

By the end of today, you will be able to:

- **Run** Python in a local environment using Positron and a virtual environment
- **Load** tabular data with pandas and inspect it with `.info()`, `.head()`, `.describe()`
- **Select and filter** rows and columns using bracket notation, `.loc[]`, and boolean indexing
- **Clean** a dataset: handle missing values, drop columns, rename fields, convert types
- **Aggregate** data with `.groupby()` to answer a research question
- **Visualize** results with seaborn

---

<!-- _class: lead -->

# Part 0

## Your New Development Environment

---

# From Google Colab → Positron (Local Development)

<div class="cols">
<div class="col">
<div class="col-label">🌐 Python 1 — Google Colab</div>
<ul>
  <li>Browser-based, zero installation</li>
  <li>Google manages your packages</li>
  <li>Files live in the cloud</li>
  <li>Runtime resets between sessions</li>
  <li>Great for getting started — less realistic for real work</li>
</ul>
</div>
<div class="col">
<div class="col-label">💻 Python 2 — Positron + venv</div>
<ul>
  <li>Runs entirely on your machine</li>
  <li>You manage a <strong>virtual environment</strong></li>
  <li>Files are local — you own them</li>
  <li>Environment persists across sessions</li>
  <li>How researchers and data scientists actually work</li>
</ul>
</div>
</div>

<div class="callout">
<strong>Virtual environment:</strong> an isolated Python installation for this project only. Keeps dependencies clean and reproducible.
</div>

---

# Today's Dataset: OASIS-1

**Open Access Series of Imaging Studies** (`oasis_cross-sectional.csv`)

- **436 subjects** — ages 18–96, right-handed, mix of males and females
- MRI-derived brain measurements + demographics
- Subjects classified as nondemented, mildly demented, or moderately demented
- Key variables: `Age`, `M/F`, `CDR` (Clinical Dementia Rating), `nWBV` (normalized whole-brain volume)

<div class="callout">
<strong>Our research question:</strong> Does normalized brain volume (nWBV) differ by dementia rating (CDR)?
</div>

> **Citation:** Marcus et al. (2007). Open Access Series of Imaging Studies. *Journal of Cognitive Neuroscience*, 19(9), 1498–1507.

---

# Defining Data Cleaning

Data cleaning involves **identifying and correcting** dataset values that are:

- **Malformed** — inconsistent, incorrect, incomplete, or poorly formatted
  - *e.g., `"Male"` and `"M"` and `"male"` all in the same column*
- **Duplicated** — identical rows that inflate your results
- **Missing** — `NaN`, blank cells, placeholder values like `999` or `"N/A"`
- **Outliers / irrelevant** — entries outside your analytic scope

<div class="callout">
<strong>Goal:</strong> Prepare data for reliable analysis — not to alter its meaning. Document every decision.
</div>

---

# Determining What to Clean

Ask these before touching a single value:

| Question | pandas tool |
|----------|-------------|
| Do the data contain errors? | `.info()`, `.describe()`, `.value_counts()` |
| What is missing, and why? | `.isnull().sum()` |
| What are my analysis constraints? | Domain knowledge |
| What is my analysis plan? | — only clean what you need |

<div class="warning">
⚠️ <strong>Never clean blindly.</strong> Missing data can be informative — understand <em>why</em> it's missing before dropping it.
</div>

---

# Data Cleaning vs. Data Transformation

<div class="cols">
<div class="col">
<div class="col-label">🧹 Data Cleaning</div>
<ul>
  <li>Fix errors in existing values</li>
  <li>Handle missing data</li>
  <li>Remove duplicates</li>
  <li>Standardize formats</li>
  <li><strong>Result:</strong> same structure, better quality</li>
</ul>
</div>
<div class="col">
<div class="col-label">🔄 Data Transformation</div>
<ul>
  <li>Change the structure or shape</li>
  <li>Rename or reorder columns</li>
  <li>Convert types (str → numeric)</li>
  <li>Reshape: wide ↔ long format</li>
  <li><em>Also called: wrangling, munging, manipulation</em></li>
</ul>
</div>
</div>

<div class="callout">
In practice, you do both in the same workflow — often in the same function call.
</div>

---

# What Is pandas?

- Open-source Python library, first released **2009**
- Built on top of **NumPy** — handles mixed data types (numbers, text, dates, categories)
- Think: *Python's version of a spreadsheet, but programmable and far more powerful*
- Standard import convention: `import pandas as pd`

<div class="cols">
<div class="col">
<div class="col-label">In Python 1 we used</div>
<ul>
  <li>NumPy arrays — purely numeric</li>
  <li><code>np.loadtxt()</code> — required specifying everything</li>
  <li>Inflammation data — clean, uniform</li>
</ul>
</div>
<div class="col">
<div class="col-label">In Python 2 we use</div>
<ul>
  <li>pandas DataFrames — mixed types</li>
  <li><code>pd.read_csv()</code> — handles nearly everything</li>
  <li>OASIS data — messy, real-world</li>
</ul>
</div>
</div>

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

<!-- _class: classroom -->

# Key Data Structures: DataFrame and Series

<div class="cols">
<div class="col">
<div class="col-label">DataFrame</div>

```python
df = pd.read_csv("oasis_cross-sectional.csv")
type(df)  # pandas.core.frame.DataFrame
```

- **Two-dimensional** tabular structure
- Rows and named columns
- Like a spreadsheet or SQL table
- Internally: a **dict of Series**
- Usually abbreviated `df`

</div>
<div class="col">
<div class="col-label">Series</div>

```python
df["Age"]
type(df["Age"])  # pandas.core.series.Series
```

- **One-dimensional** labeled array
- Like a single column in a spreadsheet
- Every DataFrame column is a Series
- Dict-like: index → value

</div>
</div>

---

<!-- _class: classroom -->

# Indexing by Label: `.loc[]`

Select rows and columns **by name**:

```python
# Select a single value
df.loc[0, "Age"]                  # row label 0, column "Age"

# Filter rows with a condition
df.loc[df["CDR"] == 0.5]          # all rows where CDR is 0.5

# Select a range of rows, specific column
df.loc[0:4, "Age"]                # rows 0–4, "Age" column
```

<div class="callout"><strong>Tip:</strong> Use <code>.loc[]</code> whenever you're selecting by column name — it's safer and more readable than bracket chaining.</div>

---

<!-- _class: classroom -->

# Indexing by Position: `.iloc[]`

Select rows and columns **by integer position**:

```python
# Select a single value by position
df.iloc[0, 2]                     # first row, third column

# Select a slice
df.iloc[0:5, :]                   # first 5 rows, all columns
df.iloc[:, 0:3]                   # all rows, first 3 columns
```

<div class="callout"><strong>Remember:</strong> <code>.iloc[]</code> uses Python-style slicing — the end index is <em>excluded</em>. <code>.loc[]</code> includes the end label.</div>

---

<!-- _class: classroom -->

# A Warning You Will Encounter

## `SettingWithCopyWarning`

Triggered by **chained indexing**:
```python
# ⚠️  Do NOT do this
df["CDR"][df["CDR"] > 0] = 0.5  # chained — may silently fail

# ✅  Do this instead
df.loc[df["CDR"] > 0, "CDR"] = 0.5  # safe and explicit
```

<div class="warning">
⚠️ pandas cannot tell if you are modifying the <strong>original</strong> DataFrame or a <strong>copy</strong>. Your assignment may silently do nothing. This is not an error — but it can produce wrong results without warning.
</div>

> You will see chained indexing on StackOverflow and in AI-generated code. Recognize it. Fix it.

---

<!-- _class: classroom -->

# Split-Apply-Combine with `.groupby()`

A core strategy in data analysis (Wickham, 2011):

```python
# Full pattern
df.groupby("CDR")["nWBV"].mean()

# Step by step:
groups = df.groupby("CDR")     # SPLIT  — divide by CDR value
result = groups["nWBV"].mean() # APPLY  — compute mean per group
                               # COMBINE — collect into a new Series
```

<div class="cols">
<div class="col">
<div class="col-label">SPLIT</div>
<p>Divide DataFrame into groups based on a key column</p>
</div>
<div class="col">
<div class="col-label">APPLY</div>
<p><code>.mean()</code> &nbsp; <code>.sum()</code> &nbsp; <code>.count()</code> &nbsp; <code>.agg()</code></p>
</div>
</div>

<div class="callout">
<strong>This answers our research question:</strong> Does normalized brain volume differ by dementia rating?
</div>

---

<!-- _class: classroom -->

# Visualizing Results with seaborn

seaborn = statistical visualization built on matplotlib, designed for DataFrames:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Box plot: distribution of brain volume by CDR group
sns.boxplot(data=df_clinical, x="CDR", y="BrainVolume", palette="Blues")
plt.title("Normalized Brain Volume by Dementia Rating (CDR)")
plt.show()

# Bar plot with confidence interval
sns.barplot(data=df_clinical, x="CDR", y="BrainVolume",
            order=["0.0", "0.5", "1.0", "2.0"], palette="Blues_d")
```

| Chart | Use when |
|-------|----------|
| `boxplot` | Show distribution + outliers per group |
| `barplot` | Show mean ± confidence interval per group |
| `scatterplot` / `lmplot` | Relationship between two numeric variables |

---

# Today We:

1. 🖥️ **Graduated** from Google Colab to a local Positron + venv environment
2. 📂 **Loaded** real neuroscience data (OASIS-1) with `pd.read_csv()`
3. 🔍 **Inspected** the data with `.info()`, `.head()`, `.describe()`
4. 🎯 **Selected** data with bracket notation, `.loc[]`, and boolean filters
5. 🧹 **Cleaned** the data: dropped columns, handled missing values, converted types
6. 📊 **Answered a research question** with `.groupby()`:
   > *Brain volume (nWBV) decreases as CDR (dementia rating) increases*
7. 📈 **Visualized** findings with seaborn

---

<!-- _class: classroom -->

# AI as a Pair Programmer

Tools like **GitHub Copilot** and **Claude** can help with pandas code.

**Example prompt:**
> *"I have a pandas DataFrame with Age, CDR, and nWBV. Show mean brain volume by CDR group."*

```python
# AI-generated output:
summary = df_clinical.groupby("CDR")["nWBV"].mean()
print(summary)
```

<div class="cols">
<div class="col">
<div class="col-label">✅ When AI helps</div>
<ul>
  <li>Learning a new function</li>
  <li>Decoding error messages</li>
  <li>Exploring unfamiliar syntax</li>
</ul>
</div>
<div class="col">
<div class="col-label">⚠️ Be cautious when</div>
<ul>
  <li>AI doesn't know your data</li>
  <li>Code looks right but isn't</li>
  <li>You can't explain every line</li>
</ul>
</div>
</div>

---

# Resources for Continued Learning

<div class="cols">
<div class="col">
<div class="col-label">pandas & seaborn</div>
<ul>
  <li><a href="https://pandas.pydata.org/docs/">pandas documentation</a></li>
  <li><a href="https://pandas.pydata.org/docs/user_guide/10min.html">pandas 10-minute intro</a></li>
  <li><a href="https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python">pandas cheat sheet (DataCamp)</a></li>
  <li><a href="https://seaborn.pydata.org/tutorial.html">seaborn tutorial</a></li>
  <li><a href="https://seaborn.pydata.org/tutorial/color_palettes.html">seaborn color palettes</a></li>
</ul>
</div>
<div class="col">
<div class="col-label">Python & Yale</div>
<ul>
  <li><a href="https://python.org">python.org</a> — official docs</li>
  <li><a href="https://www.pythoncheatsheet.org">Python Cheatsheet</a></li>
  <li><a href="https://jakevdp.github.io/PythonDataScienceHandbook/">Python Data Science Handbook</a> — free</li>
  <li><a href="https://github.com/CWML/Python1">Python 1 materials</a> (GitHub)</li>
  <li><a href="https://library.medicine.yale.edu/research-data/learn-work-data">CWML: Learn to Work with Data</a></li>
</ul>
</div>
</div>

---

<!-- _class: lead -->

# Thank You

## Questions?

Cushing/Whitney Medical Library · Yale University
`library.medicine.yale.edu/research-data`

![w:180 h:180](qr_code.png)
