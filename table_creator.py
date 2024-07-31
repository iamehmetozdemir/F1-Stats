import sqlite3
import pyodbc

# SQLite veritabanına bağlan
sqlite_conn = sqlite3.connect('./Source/Formula1.sqlite')

# SQLite veritabanındaki tüm tablo isimlerini al
cursor = sqlite_conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
tables = [table[0] for table in tables]

# Get column names and data types for each table
for table in tables:
    cursor.execute(f"PRAGMA table_info({table});")
    table_info = cursor.fetchall()
    print(f"{table} table schema:")
    for col in table_info:
        print(col)
    print("\n")

# MSSQL Server'a bağlan
mssql_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=IAMEHMETOZDEMIR\\SQLEXPRESS;' 
    'DATABASE=Formula;'
    'UID=sa;'
    'PWD=iamehmetozdemir'
)


# Create tables on MSSQL Server using SQLite table schemas
for table in tables:
    print(f"Creating {table} table on MSSQL Server...")
    cursor = sqlite_conn.cursor()
    cursor.execute(f"PRAGMA table_info({table});")
    table_info = cursor.fetchall()
    
    table_name = table
    columns = []
    for col in table_info:
        if col[1] == '':
            continue
        if col[2] == '':
            columns.append(f"{col[1]} VARCHAR")
        else:
            columns.append(f"{col[1]} {col[2]}")
    columns = ", ".join(columns)
    
    
    cursor = mssql_conn.cursor()
    
    
    columns = columns.replace("VARCH", "VARCHAR").replace("INTEG", "INTEGER")
    columns = columns.replace("ARAR", "AR").replace("ERER", "ER")
    
    columns = columns.replace("VARCHAR", "VARCHAR(255)")
    
    print(columns)
    
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    print(f"CREATE TABLE {table_name} ({columns});")
    cursor.execute(f"CREATE TABLE {table_name} ({columns});")
    mssql_conn.commit()
# Her tabloyu pandas DataFrame olarak oku ve MSSQL Server'a yaz


# Bağlantıları kapat
sqlite_conn.close() 
mssql_conn.close() 