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
