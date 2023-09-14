# function for accessing the DB

import pyodbc

def sql_query(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
       result = cur.execute(sqlvar)
    except Exception as e:
        print(e)
        result = None
    conn.commit()
    cur.close()
    return result


# INSERT statement  

# INSERT INTO <tablename> (<colname1>,<colname2>,...) VALUES  (<valforcol1>,<valforcol2>,...)

sqlqueryvar = "INSERT INTO salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes) VALUES   (70, 'Leon','Robinson',2,30000,12,'Gtr Manchester','M1 1MM','0161616161','Amazingly cool and good looking')"

insertresult = sql_query(sqlqueryvar)
print(insertresult)

# UPDATE statement

# UPDATE <tablename> SET <col1name> = <value>, <col2name> = <value>,... WHERE <filter>
# filter is made up of <col_name>  <test_charactor>  <value>

sqlqueryvar = "UPDATE salesperson SET dept_no = 1, salary = 15 WHERE emp_no = 70"

sql_query(sqlqueryvar)


# DELETE Statement
# DELETE FROM table_name WHERE condition; 

sqlqueryvar = "DELETE FROM salesperson WHERE emp_no = 70"

sql_query(sqlqueryvar)