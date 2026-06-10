import pandas as pd

perf = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

metrics = perf[
    [
        "scheme_name",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "sharpe_ratio",
        "sortino_ratio",
        "expense_ratio_pct"
    ]
]

print(metrics.head())

metrics.to_csv(
    "data/processed/performance_metrics.csv",
    index=False
)

print("Metrics Computed Successfully")