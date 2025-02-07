
import pandas as pd
import pyodbc

from data.pwds import tt_prod_pwd

def get_database_connection():

    # Define the connection string
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=zab-ghs-p-srv-sql.database.windows.net;"
        "DATABASE=LOPAWebDB;"
        "UID=LOPAAnalytics;"
        f"PWD={tt_prod_pwd}"
    )

    # Create a connection to the database
    conn = pyodbc.connect(conn_str)
    return conn

def get_data_table_return_as_dataframe(table):

    conn = get_database_connection()
    
    # Example query to fetch data from a table named 'example_table'
    query = f"SELECT * FROM {table}"

    # Use pandas to read the SQL query into a DataFrame
    df = pd.read_sql(query, conn)

    # Close the connection
    conn.close()

    return df

