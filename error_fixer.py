import pyodbc

mssql_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=IAMEHMETOZDEMIR\\SQLEXPRESS;' 
    'DATABASE=Formula;'
    'UID=sa;'
    'PWD=iamehmetozdemir'
)

cursor = mssql_conn.cursor()

with open("errors.txt", "r") as f:
    queries = f.readlines()
    for query in queries:
        print(query)
        cursor.execute(query)
    mssql_conn.commit()