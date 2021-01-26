import sqlite3

CONN = sqlite3.connect('northwind_small.sqlite3')


def run_queries():
    """Run and print out from queries for sprint challenge questions."""
    # No joins
    expensive_items = 'SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
    avg_hire_age = 'SELECT AVG(HireDate - BirthDate) FROM Employee;'
    age_by_city = ('SELECT City, AVG(HireDate - BirthDate) FROM Employee '
                   'GROUP BY City;')

    # Joins
    item_suppliers = ('SELECT p.ProductName, p.UnitPrice, s.CompanyName '
                      'FROM Product p, Supplier s WHERE p.SupplierId = s.Id '
                      'ORDER BY p.UnitPrice DESC LIMIT 10;')
    largest_category = ('SELECT c. CategoryName, COUNT(DISTINCT p.Id) '
                        'FROM Category c, Product p WHERE c.Id = p.CategoryId '
                        'GROUP BY 1 ORDER BY 2 DESC LIMIT 1;')
    employee = ('SELECT e.Id, e.FirstName, e.LastName, COUNT(DISTINCT t.Id) '
                'FROM Territory t, Employee e, EmployeeTerritory et '
                'WHERE e.Id = et.EmployeeId AND t.id = et.TerritoryId '
                'GROUP BY 1, 2, 3 ORDER BY 4 DESC LIMIT 1;')
    # Put them all together, run them, print the results
    queries = (expensive_items, avg_hire_age, age_by_city,
               item_suppliers, largest_category, employee)
    curs = CONN.cursor()
    for query in queries:
        print(curs.execute(query).fetchall())


if __name__ == "__main__":
    run_queries()
