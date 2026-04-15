import os
import urllib
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


def get_engine():
    server   = os.getenv("DB_SERVER",   "TIRED")           # fallback pro valor original
    database = os.getenv("DB_DATABASE", "ContosoRetailDW") # fallback pro valor original

    params = urllib.parse.quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
    )

    engine = create_engine(
        f"mssql+pyodbc:///?odbc_connect={params}",
        pool_pre_ping=True,  # detecta conexões mortas automaticamente
        pool_size=5
    )

    return engine