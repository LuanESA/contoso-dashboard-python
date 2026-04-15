# database.py
from sqlalchemy import create_engine
import urllib

def get_engine():
    params = urllib.parse.quote_plus(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=TIRED;"
        "DATABASE=ContosoRetailDW;"
        "Trusted_Connection=yes;"
    )

    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

    return engine
