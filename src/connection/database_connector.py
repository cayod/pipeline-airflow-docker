import psycopg2 as postgree


class DatabaseConnector:

    @classmethod
    def connect(cls):
        connection = None
        print('Connecting to the PostgreSQL database...')
        database_connection = postgree.connect(
            database="northwind",
            user='northwind_user',
            password='thewindisblowing',
            host='127.0.0.1',
            port='5432',
        )
        cls.connection = database_connection
        return cls.connection

    @classmethod
    def close(cls):
        if cls.connection is not None:
            cls.connection.close()
            print("Database connection closed.")
