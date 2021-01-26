import os
import pandas as pd
import sqlite3
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)

# First load and explore csv file in pandas
df = pd.read_csv('buddymove_holidayiq.csv')
# print(df)
df.index.rename("id", inplace=True)  # assigns a column label "id" for the index column
df.index += 1  # starts ids at 1 instead of 0
print(df.head())

# Prepare for the df to sql transfer
connection = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = connection.cursor()
table_name = 'Review_321'

df.to_sql(table_name, con=connection, if_exists='replace')
# if_exist helps to rerun the .py several times without the
# need to create a new table_name every time.

# Count how many rows you have - it should be 249!
# execute and print SQL query
curs.execute(f"SELECT count(distinct id) as review_count FROM {table_name};")
results = curs.fetchone()
print(results, "RECORDS")

# How many users who reviewed at least 100 Nature in the category
# also reviewed at least 100 in the Shopping category?
query = '''
SELECT COUNT('User Id')
FROM Review_321
WHERE Nature >= 100
AND Shopping >= 100;
'''

results = curs.execute(query).fetchall()
print('Users who reviewed 100 or more Nature and Shopping category:', results[0][0])
