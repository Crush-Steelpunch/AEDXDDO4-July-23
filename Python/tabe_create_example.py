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


# DROP TABLE statement

#DROP TABLE table_name; 

droptablequery = "DROP TABLE gametable"
sql_query(droptablequery)

# CREATE TABLE statement

# CREATE TABLE table_name (
#    column1 datatype constraint,
#    column2 datatype constraint,
#    column3 datatype constraint,
#   ....
#); 



createtablequery = "CREATE TABLE gametable ( ID int PRIMARY KEY, gamename varchar(40) NOT NULL, boardgame bit, num_of_players int, notes varchar(255) )"

sql_query(createtablequery)


insertrows = ["INSERT INTO gametable (ID, gamename,boardgame,num_of_players,notes) VALUES (1,'shogi',1,2,'like chess')",
             "INSERT INTO gametable (ID, gamename,boardgame,num_of_players,notes) VALUES (2,'Mahjong',1,4,'like poker')",
             "INSERT INTO gametable (ID, gamename,boardgame,num_of_players,notes) VALUES (3,'Quake 2',0,1,'like Doom')",
             "INSERT INTO gametable (ID, gamename,boardgame,num_of_players,notes) VALUES (4,NULL,0,1,'like Null')",
             "INSERT INTO gametable (ID, gamename,boardgame,num_of_players,notes) VALUES (4,'test',0,1,'like test')"]

for i in insertrows:
    sql_query(i)


