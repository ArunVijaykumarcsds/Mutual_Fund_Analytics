import pandas as pd
import sqlite3

conn = sqlite3.connect("data/db/bluestock_mf.db")

files = {
    "fund_master": "data/raw/01_fund_master.csv",
    "nav_history": "data/raw/02_nav_history.csv",
    "aum_by_fund_house": "data/raw/03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "data/raw/04_monthly_sip_inflows.csv",
    "category_inflows": "data/raw/05_category_inflows.csv",
    "industry_folio_count": "data/raw/06_industry_folio_count.csv",
    "scheme_performance": "data/raw/07_scheme_performance.csv",
    "investor_transactions": "data/raw/08_investor_transactions.csv",
    "portfolio_holdings": "data/raw/09_portfolio_holdings.csv",
    "benchmark_indices": "data/raw/10_benchmark_indices.csv"
}

for table_name, file_path in files.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {table_name}")

conn.close()

print("Database created successfully!")