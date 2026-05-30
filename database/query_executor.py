import pandas as pd
from database.db_connection import get_connection

def execute_query(query):
    conn = get_connection()

    try:
        df = pd.read_sql(query, conn)
        return df

    finally:
        conn.close()