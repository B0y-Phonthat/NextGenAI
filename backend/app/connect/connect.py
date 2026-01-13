import  sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import urllib

# CONFIGURATION
serverName = ""
Database = ""
userName = ""
password = ""
driver = "ODBC Driver 17 for SQL Server"  

# CONFIGURATION STRING
try:
    if userName and password:
        # SQL Server Authen
        connection_str =  (
            f"DRIVER={driver};"
            f"SERVER={serverName};"
            f"DATABASE={Database};"
            f"UID={userName};"
            f"PWD={password};"
        )
    else:
        # Window Authen
        connection_str = (
            f"DRIVER={driver};"
            f"SERVER={serverName};"
            f"DATABASE={Database};"
            "Trusted_Connection=yes"
        )
    # Encode connection
    params = urllib.parse.quote_plus(connection_str)
    # SQLAlchemy Engine
    engine = create_engine(f"mssql+pyodbc://?odbc_connect={params}")

    with engine.connect() as conn:
        result = conn.execute(text("SELECT @@VERSION AS version"))
        row = result.fetchone()
        print(f"Connected sucessfully! SQL version {row.version}")
except SQLAlchemyError as e:
    print("Database connect failed.")
    print(f"Error detailed: {e}")
except Exception as ex:
    print("Unexpected error occured.")
    print(f"Error detailed: {ex}")