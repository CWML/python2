# Cleaning and Summarizing Data with pandas (Python 2)

Move beyond the basics and start analyzing real-world research data.

This 2-hour, hands-on workshop is designed for researchers, students, and faculty who have a basic grasp of Python and are ready to tackle the "messy" side of data science. Transitioning from basic scripts & notebooks to a professional local development workflow, we will use Positron—the new data science IDE from the creators of RStudio—to manage a complete analysis pipeline.

Using the OASIS-1 neuroscience dataset, we will work through the practical steps of transforming raw MRI demographics into research insights. By the end of the session, we will answer a specific clinical question: Does normalized brain volume differ by dementia rating?

---

## Learning Objectives

By the end of this session, learners will be able to:

1. **Establish** a reproducible research workflow by setting up a local environment with Positron and virtual environments.
2. **Load** tabular data into a pandas DataFrame and inspect its structure using `info()`, `head()`, `describe()`, and related methods
3. **Select** specific rows, columns, and subsets of data using bracket notation and `.loc[]`
4. **Clean** a real-world dataset by handling missing values (`dropna()`, `fillna()`), renaming columns, dropping unnecessary columns, and converting data types
5. **Summarize** data by grouping and aggregating with `groupby()` to answer a specific research question
6. **Visualize** data distributions and relationships using seaborn (if time permits)

---

## What We Cover

| Time | Topic |
|------|-------|
| 20 min | Conceptual overview (slides) |
| 15 min | Live environment setup |
| 70 min | Hands-on notebook: pandas, cleaning, groupby, seaborn |
| 12 min | Script demo: `analysis.py` |
| 3 min  | Wrap-up & resources |

**Research question we answer:** *Does normalized brain volume differ by dementia rating in the OASIS-1 dataset?*

---

## Prerequisites

- Completion of [Python 1](https://github.com/CWML/Python1) (or equivalent familiarity with Python basics, loops, functions, NumPy, and matplotlib)
- A local Python environment — see setup instructions below

---

## Setup (Before the Workshop)

---

### macOS

#### 1. Install Xcode Command Line Tools

Open **Terminal** and run:

```bash
xcode-select --install
```

A dialog will appear — click **Install** and wait for it to complete. This provides Git and other command-line utilities required for the steps below.

#### 2. Install Python 3

First, check whether Python 3 is already installed by running this in Terminal:

```bash
python3 --version
```

If you see a version number (e.g., `Python 3.11.4`), you can skip to step 3. If not, download and install Python 3 from [python.org/downloads](https://www.python.org/downloads/) and follow the prompts.

#### 3. Install Positron

Download and install [Positron](https://github.com/posit-dev/positron/releases) — a data science IDE built on VS Code.

#### 4. Clone this repository

```bash
git clone https://github.com/CWML/python2.git
cd python2
```

#### 5. Create a virtual environment

A virtual environment is an isolated Python installation just for this project. This keeps the packages you install here from interfering with other Python projects on your computer.

```bash
python3 -m venv .CWMLPython2
source .CWMLPython2/bin/activate
```

- `python3 -m venv .CWMLPython2` creates the virtual environment in a folder called `.CWMLPython2`
- The `.` prefix makes it a hidden folder — it won't appear in Finder by default, which keeps your project directory tidy. You can still see it with `ls -la` in the terminal.
- `source .CWMLPython2/bin/activate` activates it — your terminal prompt will change to show `(.CWMLPython2)`, confirming it's active. You'll need to run this activation command each time you open a new terminal session.

#### 6. Install dependencies

With your virtual environment active, this installs all the Python packages this workshop requires (as listed in `requirements.txt`):

```bash
pip install -r requirements.txt
```

#### 7. Open the notebook

Open `python2_workshop.ipynb` in Positron and select your `.CWMLPython2` kernel. Then run the **Part 0** cells to verify your environment — the output should show `.CWMLPython2` in the executable path.

---

### Windows

#### 1. Install Python 3

First, check whether Python 3 is already installed by running this in Command Prompt or PowerShell:

```powershell
python --version
```

If you see a version number (e.g., `Python 3.11.4`), you can skip to step 2. If not, download and install Python 3 from [python.org/downloads](https://www.python.org/downloads/). During installation, **check the box that says "Add Python to PATH"**.

#### 2. Install Git

Download and install Git from [git-scm.com](https://git-scm.com/downloads). Use the default options during installation.

#### 3. Install Positron

Download and install [Positron](https://github.com/posit-dev/positron/releases) — a data science IDE built on VS Code.

#### 4. Clone this repository

Open **Command Prompt** or **PowerShell** and run:

```powershell
git clone https://github.com/CWML/python2.git
cd python2
```

#### 5. Create a virtual environment

```powershell
python -m venv .CWMLPython2
.CWMLPython2\Scripts\activate
```

- The `.` prefix makes it a hidden folder — it won't appear in File Explorer by default, which keeps your project directory tidy. You can still see it with `dir /a` in the command prompt.

#### 6. Install dependencies

```powershell
pip install -r requirements.txt
```

#### 7. Open the notebook

Open `python2_workshop.ipynb` in Positron and select your `.CWMLPython2` kernel. Then run the **Part 0** cells to verify your environment — the output should show `.CWMLPython2` in the executable path.

---

## Repository Contents

```
python2/
├── python2_workshop.ipynb        # Main workshop notebook
├── analysis.py                   # Standalone script for end-of-class demo
├── requirements.txt              # Python dependencies
├── data/
│   ├── oasis_cross-sectional.csv # Raw OASIS-1 dataset
│   └── oasis_cleaned.csv         # Cleaned dataset (produced during workshop)
├── outputs/                      # Script output directory (PNG plots)
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

---

## Resources

### General Python Documentation
- Official Python docs: https://python.org 
- Beginner guide: https://wiki.python.org/moin/BeginnersGuide
- Python PEP8 style guide: https://peps.python.org/pep-0008/
- Python Cheatsheet: https://www.pythoncheatsheet.org
- [ A Whirlwind tour of Python](https://colab.research.google.com/github/jakevdp/WhirlwindTourOfPython/blob/master/Index.ipynb)
    - A Whirlwind Tour of Python is a fast-paced introduction to essential components of the Python language for researchers and developers who are already familiar with programming in another language.
### pandas
- [pandas documentation](https://pandas.pydata.org/docs/)
- [pandas 10-minute intro](https://pandas.pydata.org/docs/user_guide/10min.html)
- [pandas cheat sheet (DataCamp)](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python)

### seaborn
- [seaborn tutorial](https://seaborn.pydata.org/tutorial.html)
- Seaborn Color Palettes - [PyData Tutorial](https://seaborn.pydata.org/tutorial/color_palettes.html)

### Yale
- [Getting Started with Data Analysis & Visualization: Introduction to Python(Python 1)](https://github.com/CWML/Python1)
- [CWML: Learn to Work with Data](https://library.medicine.yale.edu/research-data/learn-work-data)
- [Python Data Science Handbook (free)](https://jakevdp.github.io/PythonDataScienceHandbook/)

---

## Contact

Cushing/Whitney Medical Library Data Services
[library.medicine.yale.edu/research-data](https://library.medicine.yale.edu/research-data)
