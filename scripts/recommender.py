import pandas as pd

perf = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

recommended = perf.sort_values(
    by="return_5yr_pct",
    ascending=False
).head(5)

print("Top Recommended Funds")

print(
    recommended[
        [
            "scheme_name",
            "return_5yr_pct",
            "sharpe_ratio"
        ]
    ]
)