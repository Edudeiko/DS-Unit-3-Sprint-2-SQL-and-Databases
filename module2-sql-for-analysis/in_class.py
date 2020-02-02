import psycopg2
import os

DB_NAME = os.getenv("DB_NAME", default='OOPS')
DB_USER = os.getenv("DB_USER", default='OOPS')
DB_PASSWORD = os.getenv("DB_PASSWORD", default='OOPS')
DB_HOST = os.getenv("DB_HOST", default='OOPS')


### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname='hdhbjtze',
                        user='hdhbjtze',
                        password='EqrtQgw_dfugoOsxD3YG1ANSeC-WTsbW',
                        host='rajje.db.elephantsql.com')
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
cur.fetchone()

# conda create -n db-env python=3.7
# conda activate db-env
# pip install psycopg2 python-dotenv pandas
# pip install python-dotenv

