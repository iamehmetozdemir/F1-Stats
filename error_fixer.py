import pyodbc

mssql_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=IAMEHMETOZDEMIR\\SQLEXPRESS;' 
    'DATABASE=Formula;'
    'UID=sa;'
    'PWD=iamehmetozdemir'
)

cursor = mssql_conn.cursor()
success = []
with open("errors.txt", "r") as f:
    queries = f.readlines()
    for query in queries:
        print(query)
        try:
            cursor.execute(query)
            mssql_conn.commit()
            success.append(query)
        except Exception as e:
            print(e)
            break
        
with open("errors.txt", "w") as f:
    for query in queries:
        if query not in success:
            f.write(query)