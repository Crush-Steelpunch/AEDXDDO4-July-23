import pyodbc  # we're using the pydobc module

# help(pyodbc)

connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'


conn = pyodbc.connect(connectionString)  # the object that we can use to send commands to the Database

# help(conn)  

cur = conn.cursor()   # This manages the command that we want to send

help(cur)

result = cur.execute('SELECT * FROM company').fetchall()

for row in result:
    print(row)


tablesvar = cur.tables().fetchall()
type(tablesvar)

print(tablesvar)

columnsvar = cur.columns('dept')
for  colvar in columnsvar:
    print(colvar)

conn.close()