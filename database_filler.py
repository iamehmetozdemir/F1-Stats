import sqlite3
import pyodbc
import pandas as pd
# SQLite veritabanına bağlan
sqlite_conn = sqlite3.connect('./Source/Formula1.sqlite')

# SQLite veritabanındaki tüm tablo isimlerini al

cursor = sqlite_conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
tables = [table[0] for table in tables]


mssql_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=IAMEHMETOZDEMIR\\SQLEXPRESS;' 
    'DATABASE=Formula;'
    'UID=sa;'
    'PWD=iamehmetozdemir'
)


for table in tables:
    if table == 'sqlite_master':
        continue
    print(f"Reading {table} table from SQLite...")
    sqlite_cursor = sqlite_conn.cursor()
    sqlite_cursor.execute(f"SELECT * FROM {table};")
    data = sqlite_cursor.fetchall()
    columns = [desc[0] for desc in sqlite_cursor.description]
    
    print(f"Writing {table} table to MSSQL Server...")
    mssql_cursor = mssql_conn.cursor()
    for row in data:
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ("
        for i, value in enumerate(row):
            
            if type(value) == str:
                query += f"'{value}'"
            else:
                query += str(value)
            if i != len(row) - 1:
                query += ", "
        query += ");"
        print(query)
        try:
            mssql_cursor.execute(query)
        except Exception as e:
            with open("errors.txt", "a") as f:
                query = query.encode("ascii", "ignore").decode("ascii")
                f.write(query + "\n")
    mssql_conn.commit()
print("All tables are written to MSSQL Server.") 

# BUNU ÇÖZCEM SONRA gotunu sikim olmuo sqlite orsbuevladı hic bulasmicaktik farkli bi kaggle