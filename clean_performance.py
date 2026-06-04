import pandas as pd
import os

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Remove duplicates
df = df.drop_duplicates()

# Expense ratio validation
df = df[(df["expense_ratio_pct"] >= 0) &
        (df["expense_ratio_pct"] <= 2.5)]

# Return columns numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with missing returns
df = df.dropna(subset=return_cols)

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Scheme performance cleaned successfully")
print(df.shape)