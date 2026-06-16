import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("=" * 50)
print("HOSPITAL PERFORMANCE ANALYTICS")
print("=" * 50)

# Load Dataset
df = pd.read_csv("data/hospital_data.csv")

print("\nDataset Loaded Successfully")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

df.columns = df.columns.str.strip()

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# Save cleaned version
df.to_csv(
    "data/hospital_cleaned.csv",
    index=False
)

print("\nClean Dataset Saved")

# ==========================
# KPI SUMMARY
# ==========================

print("\nKPI SUMMARY")
print("-" * 40)

print("Total Patients:",
      len(df))

print("Average Age:",
      round(df["Age"].mean(), 2))

print("Average Cost:",
      round(df["Cost"].mean(), 2))

print("Average Length of Stay:",
      round(df["Length_of_Stay"].mean(), 2))

print("Readmission Rate:",
      round(
          (df["Readmission"] == "Yes").mean() * 100,
          2
      ),
      "%"
)

# Create images folder
os.makedirs(
    "images",
    exist_ok=True
)

# ==========================
# Gender Distribution
# ==========================

plt.figure(figsize=(6,6))

df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")
plt.ylabel("")

plt.savefig(
    "images/gender_distribution.png"
)

plt.close()

# ==========================
# Condition Distribution
# ==========================

plt.figure(figsize=(10,6))

sns.countplot(
    y=df["Condition"],
    order=df["Condition"].value_counts().index
)

plt.title("Condition Distribution")

plt.tight_layout()

plt.savefig(
    "images/condition_distribution.png"
)

plt.close()

# ==========================
# Procedure Distribution
# ==========================

plt.figure(figsize=(10,6))

sns.countplot(
    y=df["Procedure"],
    order=df["Procedure"].value_counts().index
)

plt.title("Procedure Distribution")

plt.tight_layout()

plt.savefig(
    "images/procedure_distribution.png"
)

plt.close()

# ==========================
# Cost by Condition
# ==========================

cost_by_condition = (
    df.groupby("Condition")["Cost"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))

cost_by_condition.plot(
    kind="bar"
)

plt.title(
    "Average Cost by Condition"
)

plt.tight_layout()

plt.savefig(
    "images/cost_by_condition.png"
)

plt.close()

# ==========================
# Satisfaction Distribution
# ==========================

plt.figure(figsize=(8,5))

sns.countplot(
    x=df["Satisfaction"]
)

plt.title(
    "Patient Satisfaction"
)

plt.tight_layout()

plt.savefig(
    "images/satisfaction.png"
)

plt.close()

# ==========================
# Length of Stay
# ==========================

plt.figure(figsize=(8,5))

sns.histplot(
    df["Length_of_Stay"],
    bins=10
)

plt.title(
    "Length of Stay Distribution"
)

plt.tight_layout()

plt.savefig(
    "images/length_of_stay.png"
)

plt.close()

print("\nAll Charts Saved Successfully")
print("Check images folder")