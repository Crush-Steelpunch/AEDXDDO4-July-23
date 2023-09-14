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
#arti
sqlqueryvar = 'SELECT first_name, post_code FROM salesperson where post_code not in (\'\')'

#Ashley

sqlqueryvar = "SELECT emp_no, count(order_date) FROM sale WHERE order_date BETWEEN '2000-04-01' AND '2000-06-30' GROUP BY emp_no"

# the ; charactor is like an end-of-statement or line end

sqlqueryvar = "DECLARE @minLivingWage AS DECIMAL = 13.000 ; SELECT emp_no, first_name, salary FROM salesperson WHERE county in ('surrey','london') and salary <= @minLivingWage"

# Claire

sqlqueryvar = "select sp.first_name, sp.last_name, sp.salary, sp.sales_target, s.order_no, s.order_value, s.order_date from  [salesperson] sp   inner join [sale] s  on sp.emp_no = s.emp_no order by sp.first_name, sp.last_name, s.order_date, s.order_value desc"

resultvar = sql_query(sqlqueryvar)

for row in resultvar:
    print(row)