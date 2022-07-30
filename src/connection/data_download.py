from select import select
import psycopg2 as postgree
from database_connector import DatabaseConnector
import os
import datetime
from pandas import pandas as pd


LOCAL_TABLES_DIRECTORY = os.getcwd() + '/data'
DATE_STRING: str = datetime.date.today().strftime("%Y-%m-%d")


class DatabaseDownload():

    @classmethod
    def download_tables(cls):
        QUERY_TABLE = """SELECT table_name 
                            FROM information_schema.tables 
                            WHERE table_schema = 'public'"""

        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(QUERY_TABLE)
        query_result = cursor.fetchall()
        print("Tables found {}".format(query_result))

        for table in query_result:
            select = """SELECT * FROM {}""".format(table)
            df = pd.read.sql(select, DatabaseConnector.connection)
