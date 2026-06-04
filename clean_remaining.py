import pandas as pd

files = [
    "01_fund_master",
    "03_aum_by_fund_house",
    "04_monthly_sip_inflows",
    "05_category_inflows",
    "06_industry_folio_count",
    "09_portfolio_holdings",
    "10_benchmark_indices"
]

for file in files:
    print(f"Cleaning {file}...")

    df = pd.read_csv(f"data/raw/{file}.csv")

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Save cleaned file
    df.to_csv(
        f"data/processed/{file}_clean.csv",
        index=False
    )

    print(f"{file}_clean.csv saved successfully")

print("\nAll remaining datasets cleaned successfully!")