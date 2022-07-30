import psycopg2 as postgree
from database_connector import DatabaseConnector
import os
import datetime
from pandas import pandas as pd


LOCAL_TABLES_DIRECTORY = os.getcwd() + "/data"
DATE_STRING: str = datetime.date.today().strftime("%Y-%m-%d")


class DataDownload():

    @classmethod
    def download_tables(cls):
        try:
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
                database_df = pd.read_sql(select, DatabaseConnector.connection)
                database_directory = (
                    f"{LOCAL_TABLES_DIRECTORY}/postgre/{DATE_STRING}")
                os.makedirs(database_directory, exist_ok=True)
                database_df.to_csv(f"{database_directory}/{table}.csv")

            print("Files save in the directory...")
        finally:
            DatabaseConnector.close()

        return print("All the tables downloaded.")

    @classmethod
    def download_csv(cls) -> None:
        path_csv = "data/order_details.csv"
        file_name = os.path.basename(path_csv)
        print("Exporting csv file.")
        csv_df = pd.read_csv("data/order_details.csv")
        csv_directory = (
            f"{LOCAL_TABLES_DIRECTORY}/csv/{DATE_STRING}")
        os.makedirs(csv_directory, exist_ok=True)
        csv_df.to_csv(f"{csv_directory}/{file_name}")
        print("File save in the directory...")


if __name__ == "__main__":
    step1 = DataDownload
    step1.download_csv()


print(LOCAL_TABLES_DIRECTORY)
