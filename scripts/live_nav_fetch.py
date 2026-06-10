import pandas as pd

nav = pd.read_csv("data/processed/02_nav_history_clean.csv")

latest_nav = nav.tail(10)

print("Latest NAV Records")

print(latest_nav)