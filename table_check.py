import sqlite3
import pyodbc

# MSSQL veritabanına bağlan
mssql_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=IAMEHMETOZDEMIR\\SQLEXPRESS;' 
    'DATABASE=Formula;'
    'UID=sa;'
    'PWD=iamehmetozdemir'
)

#remove duplicates from laptimes according to driverId, raceId and lap
cursor = mssql_conn.cursor()

cursor.execute("WITH CTE AS (SELECT *, ROW_NUMBER() OVER " +
               "(PARTITION BY resultId ORDER BY resultId) " +
               "AS rn FROM results) DELETE FROM CTE WHERE rn > 1")

mssql_conn.commit()