import pandas as pd
import os

raw_path = "data/raw"

print("Checking all datasets...")

for file in os.listdir(raw_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(raw_path, file))

        print("\n" + "="*50)
        print("File:", file)
        print("Shape:", df.shape)
        print("Columns:", list(df.columns))