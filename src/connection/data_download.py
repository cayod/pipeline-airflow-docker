import psycopg2 as postgree
from database_connector import DatabaseConnector
import os
import datetime
from pandas import pandas as pd
from pathlib import Path


LOCAL_TABLES_DIRECTORY = os.getcwd() + "/data"
DATE_STRING: str = datetime.date.today().strftime("%Y-%m-%d")


class DatabaseDownload():

    @classmethod
    def download_tables(cls):

        QUERY_TABLE = """SELECT table_name 
                            FROM information_schema.tables 
                            WHERE table_schema = 'public'"""

        database_connection = DatabaseConnector.connect()
        cursor = database_connection.cursor()

        print("Quering database")

        cursor.execute(QUERY_TABLE)

        query_result = cursor.fetchall()

        print(f"Tables found {query_result}")

        for table_data in query_result:
            table = table_data[0]
            select = """SELECT * 
                        FROM {}""".format(table)
            df = pd.read_sql(select, DatabaseConnector.connection)
            database_directory = (
                f"{LOCAL_TABLES_DIRECTORY}/postgre/{DATE_STRING}")
            os.makedirs(database_directory, exist_ok=True)
            df.to_csv(f"{database_directory}/{table}.csv")

        print("Save files in the directory...")

        DatabaseConnector.close()

        return print("All the tables downloaded.")


if __name__ == "__main__":
    step1 = DatabaseDownload
    step1.download_tables()


print(LOCAL_TABLES_DIRECTORY)
