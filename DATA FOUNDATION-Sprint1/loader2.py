import sqlite3, pandas as pd

conn = sqlite3.connect("market.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

def load_csv(csv_file, table_name):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"{table_name}: {len(df)} rows loaded")
    return len(df)

audit = []

# 1. Parent table first
audit.append({"file":"companies.csv","rows":load_csv("companies.csv","dim_company")})

# 2. Child fact tables next
audit.append({"file":"pl.csv","rows":load_csv("pl.csv","fact_pl")})
audit.append({"file":"bs.csv","rows":load_csv("bs.csv","fact_bs")})
audit.append({"file":"cf.csv","rows":load_csv("cf.csv","fact_cf")})

# 3. Audit table
pd.DataFrame(audit).to_sql("load_audit", conn, if_exists="append", index=False)

# 4. FK check
cursor.execute("PRAGMA foreign_key_check;")
print(cursor.fetchall())  # should be []