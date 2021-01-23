import sqlite3

connection = sqlite3.connect("northwind_small.sqlite3")
# connection.row_factory = sqlite3.Row
curs = connection.cursor()

# In particular note that the *primary* key is `Id`, and not `CustomerId`. On
# other tables (where it is a *foreign* key) it will be `CustomerId`. Also note -
# the `Order` table conflicts with the `ORDER` keyword! We'll just avoid that
# particular table, but it's a good lesson in the danger of keyword conflicts.

# 1). What are the ten most expensive items (per unit price) in the database?
query = """
SELECT * 
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""
results = curs.execute(query).fetchall()
for ii in range(len(results)):
    print('$', results[ii][0], 'cost', results[ii][1])


# 2). What is the average age of an employee at the time of their hiring? (Hint: a
# lot of arithmetic works with dates.)
query = """
SELECT
AVG(HireDate) - AVG(BirthDate) as avg_age
FROM Employee
WHERE BirthDate IS NOT NULL
"""
curs.execute(query)
results = curs.fetchall()
print(round(results[0][0], 0), "is the average age of an employee at the time of hiring")

# PART 3

# 1). What are the ten most expensive items (per unit price) in the database *and*
# their suppliers?
query = """
SELECT UnitPrice FROM Product, Supplier
WHERE Product.Id=Supplier.Id
GROUP BY UnitPrice
LIMIT 10
"""
results = curs.execute(query).fetchall()
for ii in range(len(results)):
    print('$', results[ii][0], 'ten the most expensive items')


# 2). What is the largest category (by number of unique products in it)
query = """
SELECT CategoryName,
COUNT(DISTINCT CategoryName)
FROM Category
"""
curs.execute(query)
results = curs.fetchall()
print('Category', results[0][0], "is the largest by unique products in it")

# Part 4 - Questions (and your Answers)


# 1). In the Northwind database, what is the type of relationship between the
# `Employee` and `Territory` tables?
# --- Many-to-many relationship

# 2). What is a situation where a document store (like MongoDB) is appropriate, and
# what is a situation where it is not appropriate?
# --- MongoDB is a NOSQL database, it is appropriate only for a BIG data. It is not 
# appropriate for if you need to update more than one document or collection per user request.

# 3). What is "NewSQL", and what is it trying to achieve?
# --- is a new approach to relational databases that wants to combine
# transactional ACID (atomicity, consistency, isolation, durability)
# guarantees of good ol’ RDBMSs and the horizontal scalability of NoSQL.