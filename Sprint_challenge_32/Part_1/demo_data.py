import sqlite3

connection = sqlite3.connect("demo_data.sqlite3")
# connection.row_factory = sqlite3.Row
curs = connection.cursor()
table_name = 'demo'

# 1). Drop if exist, Create a table
create_query = """
DROP TABLE IF EXISTS demo;
"""
curs.execute(create_query)
connection.commit()

create_query = """
CREATE TABLE IF NOT EXISTS demo (
    s VARCHAR(1),
    x INT,
    y INT
);
"""
print(create_query)
curs.execute(create_query)
connection.commit()

# 2). Insert Values
insertion_query = """
INSERT INTO demo (s, x, y) VALUES
('g', 3, 9),
('v', 5, 7),
('f', 8, 7);
"""
print(insertion_query)
curs.execute(insertion_query)
connection.commit()

# You can insert them one by one as well.

# insertion_query = """
# INSERT INTO demo (s, x, y) VALUES ('v', 5, 7);
# """
# print(insertion_query)
# curs.execute(insertion_query)
# connection.commit()

# insertion_query = """
# INSERT INTO demo (s, x, y) VALUES ('f', 8, 7);
# """
# print(insertion_query)
# curs.execute(insertion_query)
# connection.commit()

# 3). Count how many rows you have - it should be 3!
curs.execute(f"SELECT COUNT() FROM {table_name};")
results = curs.fetchall()
print(results[0][0], "ROWS")

# 4). How many rows are there where both `x` and `y` are at least 5?
create_query = """
SELECT
COUNT(*)
FROM demo
WHERE x >= 5
AND y >=5
"""
curs.execute(create_query)
results = curs.fetchall()
print(results[0][0], "ROWS")

# 5). How many unique values of `y` are there
# (hint - `COUNT()` can accept a keyword `DISTINCT`)?

create_query = """
SELECT
COUNT(DISTINCT y)
FROM demo
"""
curs.execute(create_query)
results = curs.fetchall()
print(results[0][0], "unique values")
