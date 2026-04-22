"""
OASIS-1 Dementia Analysis
Python 2 Workshop — Cushing/Whitney Medical Library, Yale University

This script reproduces the full analysis from the workshop notebook
as a standalone, reproducible Python script.
"""

# pandas: data loading and manipulation
import pandas as pd
# seaborn: statistical plotting built on matplotlib
import seaborn as sns
# pyplot: save and display figures
import matplotlib.pyplot as plt

# --- Load ---
# read the CSV file into a DataFrame
df = pd.read_csv("data/oasis_cross-sectional.csv")
# print row and column counts to confirm the load
print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# --- Clean ---
# remove columns we won't use in the analysis
df = df.drop(columns=["Hand", "Delay"])
# save cleaned rows to df_clinical, preserving df with all rows intact
df_clinical = df.dropna()
# give columns more readable names
df_clinical = df_clinical.rename(columns={"M/F": "Gender", "nWBV": "BrainVolume"})
# convert CDR (dementia rating) to string so it plots as discrete categories
df_clinical["CDR"] = df_clinical["CDR"].astype(str)
# print row count after dropping rows with missing data
print(f"After cleaning: {df_clinical.shape[0]} rows")

# --- Explore ---
print("\nDementia rating distribution:")
# count how many participants fall into each dementia rating group
print(df_clinical["CDR"].value_counts())

# --- Analyze ---
print("\nMean brain volume and sample size by dementia rating:")
# compute mean brain volume and sample size for each CDR group
print(df_clinical.groupby("CDR")["BrainVolume"].agg(["mean", "count"]))

# --- Visualize ---
# box plot comparing brain volume across dementia ratings, ordered from none to severe
sns.boxplot(data=df_clinical, x="CDR", y="BrainVolume", order=["0.0", "0.5", "1.0", "2.0"])
# add a descriptive title to the plot
plt.title("Brain Volume by Dementia Rating")
# write the figure to a PNG file in the outputs folder
plt.savefig("outputs/brain_volume_by_cdr.png")
# confirm the file was saved
print("\nPlot saved to outputs/brain_volume_by_cdr.png")

# --- Save ---
# write the cleaned DataFrame to a new CSV (index=False omits the row numbers)
df_clinical.to_csv("data/oasis_cleaned.csv", index=False)
# confirm the file was saved
print("Cleaned data saved to data/oasis_cleaned.csv")
