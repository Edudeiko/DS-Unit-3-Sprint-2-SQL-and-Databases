import sqlite3
# import pandas as pd
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_uri)
db = client.rpg_db

conn = sqlite3.connect("rpg_db.sqlite3")
cursor = conn.cursor()
cursor.execute('SELECT name from sqlite_master where type= "table"')
tables = cursor.fetchall()
total_rows = 0
for table in tables:
    table = table[0]
    query = f"SELECT COUNT() FROM {table}"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    total_rows += count
    query = f"SELECT * FROM {table}"""
    db = client.rpg_db
    cursor.execute(query)
    collection = eval(f'db.{table}')
    for ii in range(len(cursor.fetchall())):
        cursor.execute(query)
        row = cursor.fetchall()[ii]
        keys = [description[0] for description in cursor.description]
        row_dict = dict()
        for jj in range(len(keys)):
            row_dict[keys[jj]] = row[jj]
        collection.insert_one(row_dict)
