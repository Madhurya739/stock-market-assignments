import pandas as pd
import sqlite3

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect(r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\market.db")

# --- Helper function to clean CSVs ---
def clean_and_load(file_path, table_name, keep_cols):
    # Skip metadata row if present
    df = pd.read_csv(file_path, skiprows=1)

    # Drop blank/Unnamed columns
    df = df.loc[:, df.columns.notnull()]
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Keep only required columns
    df = df[keep_cols]

    # Load into SQLite
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"Loaded {len(df)} rows into {table_name}")

# --- Load dimension table ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\companies.csv",
    "dim_company",
    ["ticker", "company_name", "year"]
)

# --- Load fact tables ---
clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_pl.csv",
    "fact_pl",
    ["ticker", "year", "revenue", "expenses", "profit"]
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_bs.csv",
    "fact_bs",
    ["ticker", "year", "assets", "liabilities", "equity"]
)

clean_and_load(
    r"C:\Users\srisa\Desktop\Week_2 Stock Market\project\fact_cf.csv",
    "fact_cf",
    ["ticker", "year", "operating_cf", "investing_cf", "financing_cf"]
)

# --- Audit ---
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dim_company;")
print("dim_company rows:", cur.fetchone()[0])

cur.execute("PRAGMA foreign_key_check;")
print("Foreign key check:", cur.fetchall())

conn.close()
