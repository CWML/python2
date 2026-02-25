# Python 2: Data Analysis with pandas

**Cushing/Whitney Medical Library — Yale University**

A 2-hour live-coding workshop for researchers, library staff, and graduate students. This course builds directly on [Python 1](https://github.com/CWML/python1) and introduces local Python development, pandas for data analysis, and seaborn for visualization — using a real neuroscience dataset.

---

## What We Cover

| Time | Topic |
|------|-------|
| 10 min | Environment orientation & dataset introduction |
| 35 min | Intro to pandas: loading, inspecting, selecting |
| 40 min | Data cleaning & transformation |
| 20 min | Grouping & aggregation with `.groupby()` |
| 10 min | Bonus: seaborn visualization |
| 5 min  | Wrap-up & resources |

**Research question we answer:** *Does normalized brain volume differ by dementia rating in the OASIS-1 dataset?*

---

## Prerequisites

- Completion of Python 1 (or equivalent familiarity with Python basics, loops, functions, NumPy, and matplotlib)
- A local Python environment — see setup instructions below

---

## Setup (Before the Workshop)

### 1. Install Positron

Download and install [Positron](https://github.com/posit-dev/positron/releases) — a data science IDE built on VS Code.

### 2. Clone this repository

```bash
git clone https://github.com/CWML/python2.git
cd python2
```

### 3. Create a virtual environment

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install pandas seaborn matplotlib jupyter
```

### 5. Open the notebook

Open `python2_workshop.ipynb` in Positron and select your `venv` kernel.

---

## Repository Contents

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

---

## Dataset

**OASIS-1: Open Access Series of Imaging Studies**
Cross-sectional MRI data and demographics for 436 subjects (ages 18–96), including nondemented and demented older adults.

> Marcus, D.S., Wang, T.H., Parker, J., Csernansky, J.G., Morris, J.C., Buckner, R.L. (2007). Open Access Series of Imaging Studies (OASIS): Cross-Sectional MRI Data in Young, Middle Aged, Nondemented and Demented Older Adults. *Journal of Cognitive Neuroscience*, 19(9), 1498–1507.

- [OASIS Brains](https://sites.wustl.edu/oasisbrains/)
- [Download via Kaggle](https://www.kaggle.com/datasets/jboysen/mri-and-alzheimers)

---

## Slides

The slide deck is available as:
- **HTML** — open `docs/python2_workshop_slides.html` in any browser (recommended for presenting)
- **PPTX** — open `docs/python2_workshop_slides.pptx` in PowerPoint or Google Slides

To regenerate slides from the Markdown source after edits:
```bash
npm install          # first time only
npx marp docs/python2_workshop_slides.md --html --pptx
```

---

## Resources

### pandas
- [pandas documentation](https://pandas.pydata.org/docs/)
- [pandas 10-minute intro](https://pandas.pydata.org/docs/user_guide/10min.html)
- [pandas cheat sheet (DataCamp)](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python)

### seaborn
- [seaborn tutorial](https://seaborn.pydata.org/tutorial.html)

### Data Cleaning
- [Data Organization in Spreadsheets — Broman & Woo (2018)](https://doi.org/10.1080/00031305.2017.1375989)

### Yale
- [CWML: Learn to Work with Data](https://library.medicine.yale.edu/research-data/learn-work-data)
- [Python Data Science Handbook (free)](https://jakevdp.github.io/PythonDataScienceHandbook/)

---

## Contact

Cushing/Whitney Medical Library Data Services
[library.medicine.yale.edu/research-data](https://library.medicine.yale.edu/research-data)
