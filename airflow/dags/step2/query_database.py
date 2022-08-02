import pandas as pd
from database_connector import DatabaseConnector
import os

QUERY: str = """ SELECT *
            FROM orders
            JOIN order_details
            WHERE orders.order_id = order_details.order_id
"""
QUERYS_RESULTS_DIRECTORY: str = os.getcwd() + "/query_result.csv"


def database_query(query):
    '''Download a table queryed.

        Args:
            str: Query for search in database.

        Return:
            None.  '''

    database_engine = DatabaseConnector()
    engine = database_engine.engine()
    df = pd.read_sql_query(query, engine)
    df.to_csv(QUERYS_RESULTS_DIRECTORY)
    print(df)


if __name__ == "__main__":
    database_query(QUERY)
