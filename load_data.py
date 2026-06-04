import pandas as pd
import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

nav = pd.read_csv("data/processed/02_nav_history_clean.csv")
perf = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
trans = pd.read_csv("data/processed/08_investor_transactions_clean.csv")

nav.to_sql("fact_nav", conn, if_exists="replace", index=False)
perf.to_sql("fact_performance", conn, if_exists="replace", index=False)
trans.to_sql("fact_transactions", conn, if_exists="replace", index=False)

print("Data loaded successfully!")

conn.close()