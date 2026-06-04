import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Date convert
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove invalid NAV
df = df[df["nav"] > 0]

# Save cleaned file
df.to_csv("data/processed/02_nav_history_clean.csv", index=False)

print("NAV history cleaned successfully")
print(df.shape)