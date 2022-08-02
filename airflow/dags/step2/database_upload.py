import os
from pandas import pandas as pd
from database_connector import DatabaseConnector
import re

LOCAL_TABLES_DIRECTORY: str = os.getcwd() + "/raw_data"
CSV_REGEX: str = '^\w+\.csv$'


class DatabaseUpload():
    '''Export the files in to the database'''

    @classmethod
    def upload_tables(cls) -> None:
        '''Export csv files to database

            Args:
                None.

            Return:
                str: All tables have been exported.  '''

        database_engine = DatabaseConnector()
        engine = database_engine.engine()
        for root, dirs, files in os.walk(LOCAL_TABLES_DIRECTORY, topdown=False):
            for file in files:
                if re.fullmatch(CSV_REGEX, file) is not None:
                    df = pd.read_csv(f"{root}/{file}")
                    print(file)
                    table_name = file.split('.')[0]
                    print(f"Inserindo table {table_name}")
                    df.to_sql(table_name,
                              engine,
                              if_exists='replace',
                              index=False)
        return print("All tables have been exported.")


if __name__ == "__main__":
    step2 = DatabaseUpload()
    step2.upload_tables()
