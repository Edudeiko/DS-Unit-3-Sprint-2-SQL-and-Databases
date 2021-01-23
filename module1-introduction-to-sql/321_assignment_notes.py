
import os
import pandas as pd
import sqlite3

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.csv")
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.db")

connection = sqlite3.connect(DB_FILEPATH)
table_name = "reviews2"

df = pd.read_csv(CSV_FILEPATH)

# assigns a column label "id" for the index column
df.index.rename("id", inplace=True)
df.index += 1  # starts ids at 1 instead of 0

print(df.head())

df.to_sql(table_name, con=connection)

cursor = connection.cursor()
cursor.execute(f"SELECT count(distinct id) as review_count FROM {table_name};")
results = cursor.fetchone()

print(results, "RECORDS")

# Other approach

# conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
# data.to_sql('review', conn, if_exists = 'replace')
# curs = conn.cursor()
# query = "SELECT * FROM review"
# results = curs.execute(query).fetchall()
# print("There are", len(results), "rows")

# ----------------------------------------

# (Stretch) What are the average number of reviews for each category?
conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
curs = conn.cursor()
categories = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']
query = "SELECT * FROM review"
length = len(curs.execute(query).fetchall())
for item in categories:
    query = f"SELECT SUM({item}) FROM review"
    results = curs.execute(query).fetchall()
    print(f'Average number of reviews for {item} column:', round(results[0][0]/length))
