import sqlite3
import pandas as pd

conn = sqlite3.connect('database.db')

df = pd.read_csv('../final_project_data/csv_result-1year.csv')
df.to_sql("testTable", conn, if_exists='replace', index=False)

conn.commit()
conn.close()
