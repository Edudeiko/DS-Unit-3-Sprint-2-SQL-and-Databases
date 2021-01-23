import json
import os
from dotenv import load_dotenv
import pandas as pd
import sqlite3
import psycopg2
from psycopg2.extras import execute_values

load_dotenv()  # looks inside the .env file for some env vars

# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

DB_FILEPATH = "titanic_db.sqlite3"


class StorageService():
    def __init__(self):
        self.sqlite_connection = sqlite3.connect(DB_FILEPATH)
        self.sqlite_cursor = self.sqlite_connection.cursor()
        self.pg_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        self.pg_cursor = self.pg_connection.cursor()

# 1). Get table
    def get_summary_table(self):
        return self.sqlite_connection.execute("SELECT * FROM titanic_review;").fetchall()

# 2). Create table
# remember DROP TABLE IF EXISTS
# VARCHAR any value from 0 to 255
    def create_summary_table(self):
        create_query = """
        DROP TABLE IF EXISTS summary;
        CREATE TABLE IF NOT EXISTS summary (
            id SERIAL PRIMARY KEY,
            Survived INT,
            Pclass INT,
            Name VARCHAR(210),
            Sex VARCHAR(7),
            Age INT,
            SiblingsSpousesAboard INT,
            ParentsChildrenAboard INT,
            Fare MONEY
        );
        """
        self.pg_cursor.execute(create_query)
        self.pg_connection.commit()

# 3). Insert table
    def insert_summary_table(self, summary):
        insertion_query = "INSERT INTO summary (id, Survived, Pclass, Name, Sex, Age, SiblingsSpousesAboard, ParentsChildrenAboard, Fare) VALUES %s"
        list_of_tuples = summary
        execute_values(self.pg_cursor, insertion_query, list_of_tuples)
        self.pg_connection.commit()


if __name__ == "__main__":

    service = StorageService()

    #
    # EXTRACT AND TRANSFORM
    #

    summary = service.get_summary_table()
    print(type(summary), len(summary))
    print(summary[0])
    #
    # LOAD
    #

    service.create_summary_table()
    service.insert_summary_table(summary)
