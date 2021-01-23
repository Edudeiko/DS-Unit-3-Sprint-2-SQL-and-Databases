import sqlite3

CONN = sqlite3.connect('demo_data2.sqlite3')
DATA = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]
# 2 helper functions:
# 1).


def make_db():
    """Make and populate the demo database."""
    curs = CONN.cursor()
    curs.execute('CREATE TABLE demo (s char(1), x int, y int);')
    for datum in DATA:
        curs.execute('INSERT INTO demo (s, x, y) VALUES' + str(datum))
    curs.close()
    CONN.commit()


#  2).
def run_queries():
    """Run and print output from queries for sprint challenge questions."""
    curs = CONN.cursor()
    print(curs.execute('SELECT COUNT(*) FROM demo;').fetchall())
    print(curs.execute('SELECT COUNT(*) FROM demo WHERE x >=5 AND y >=5;').fetchall())
    print(curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall())


if __name__ == "__main__":
    make_db()
    run_queries()
