import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("mutualfunds.db")
conn.execute("PRAGMA foreign_keys = ON;")  # enforce FK constraints
cursor = conn.cursor()

# Load schema
with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

# Example: load CSV into table
df = pd.read_csv("cleaned_nav_history.csv")
df.to_sql("fact_nav", conn, if_exists="append", index=False)

conn.commit()
conn.close()
