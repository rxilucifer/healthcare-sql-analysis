"""Runs a .sql file against hospital.db and prints the result."""
import sqlite3
import sys
import pandas as pd

if len(sys.argv) < 2:
    print("Usage: python run_query.py queries/your_file.sql")
    sys.exit()

with open(sys.argv[1]) as f:
    query = f.read()

conn = sqlite3.connect("hospital.db")
print(pd.read_sql_query(query, conn).to_string(index=False))
conn.close()