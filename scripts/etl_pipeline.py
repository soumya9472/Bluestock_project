import os

print("Starting ETL Pipeline...")

os.system("python load_data.py")
os.system("python clean_nav.py")
os.system("python clean_transactions.py")
os.system("python clean_performance.py")

print("ETL Pipeline Completed Successfully")