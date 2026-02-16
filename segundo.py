import pyodbc
import pandas as pd

server = 'TIRED'
database = 'ContosoRetailDW'

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

query = """
SELECT TOP 100 *
FROM DimCustomer
"""

df = pd.read_sql(query, conn)

print(df.head())

conn.close()