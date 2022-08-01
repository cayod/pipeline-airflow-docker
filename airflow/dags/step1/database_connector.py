import psycopg2 as postgree


class DatabaseConnector:

    @classmethod
    def connect(cls):

        print('Connecting to the PostgreSQL database...')
        database_connection = postgree.connect(
            database="northwind",
            user='northwind_user',
            password='thewindisblowing',
            host='postgresdb',
            port='5432'
        )
        cls.connection = database_connection
        return cls.connection

    @classmethod
    def close(cls):
        if cls.connection is not None:
            cls.connection.close()
            print("Database connection closed.")
