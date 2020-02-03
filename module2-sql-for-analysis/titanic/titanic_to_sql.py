import os
import pandas as pd
import sqlite3
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

# First load and explore csv file in pandas
df = pd.read_csv('titanic.csv')
# print(df)
df.index.rename("id", inplace=True) # assigns a column label "id" for the index column
df.index += 1 # starts ids at 1 instead of 0
print(df.head())

# # Prepare for the df to sql transfer
connection = sqlite3.connect('titanic_db.sqlite3')
curs = connection.cursor()
table_name = 'titanic_review'

df.to_sql(table_name, con=connection, if_exists = 'replace')
# if_exist helps to rerun the .py several times without the
# need to create a new table_name every time.

# Count how many rows you have - it should be 887 rows x 8 columns!
# execute and print SQL query
curs.execute(f"SELECT count(distinct id) as review_count FROM {table_name};")
results = curs.fetchone()
print(results, "RECORDS")

# How many survived from with different values
query = '''
SELECT COUNT('Survived')
FROM titanic_review
WHERE Fare <= 15
AND Pclass >= 2;
'''

results = curs.execute(query).fetchall()
print('Survived with Fare price <=15 from 2nd or 3rd class', results[0][0])

query = '''
SELECT COUNT('Survived')
FROM titanic_review
WHERE Fare >= 15
AND Pclass == 1;
'''

results = curs.execute(query).fetchall()
print('Survived with Fare price >=15 from 1st class', results[0][0])