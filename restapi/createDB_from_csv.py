import sqlite3
import pandas as pd

conn = sqlite3.connect('database.db')

df = pd.read_csv('../dataset_django.csv')
df.to_sql("Companies", conn, if_exists='replace', index=False)

conn.commit()
conn.close()
