import pyodbc

def sql_query(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    result = cur.execute(sqlvar).fetchall()
    cur.close()
    return result

# SQL SELECT
# Reads data from a data

# Basic Form

# SELECT <colum names>  FROM  <tabletame>

sqlqueryvar = 'SELECT * FROM company'  # Select (ALL) FROM (company table)

sqlqueryvar = 'SELECT company_name, county, post_code FROM company'  # Specifiying Columns


# The WHERE clause

# SELECT <colum names>  FROM  <tabletame> WHERE <filter>

# filter is made up of <col_name>  <test_charactor>  <value>

sqlqueryvar = 'SELECT company_name, county, post_code FROM company WHERE company_no > 2000'

sqlqueryvar = 'SELECT company_name, county, post_code FROM company WHERE company_no BETWEEN 1001 AND 3999'

sqlqueryvar = "SELECT company_name, county, post_code FROM company WHERE company_name LIKE '%Inc'"
sqlqueryvar = "SELECT company_name, county, post_code FROM company WHERE county IN ('London','Devon')"

# ORDER BY clause

sqlqueryvar = 'SELECT * FROM company ORDER BY company_no DESC'  # Select (ALL) FROM (company table)

# GROUP BY clause

# SELECT <col_names>,<aggregates(<col_name>)> FROM <tablename> GROUP BY <colum_name>

# Aggregates are one of min(),max(),sum(),avg(),count()

sqlqueryvar = 'SELECT  emp_no, sum(order_value), count(emp_no) FROM  sale GROUP BY emp_no'



resultvar = sql_query(sqlqueryvar)

for row in resultvar:
    print(row)