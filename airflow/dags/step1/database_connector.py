import psycopg2 as postgree


class DatabaseConnector:
    '''Class to manage the database connection'''

    @classmethod
    def connect(cls):
        '''Start database connection

            Args:
                None.

            Return:
                var: Connection to connect to database . '''

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
    def close(cls) -> None:
        '''Close database connection

            Args:
                None.

            Return:
                None. '''

        if cls.connection is not None:
            cls.connection.close()
            print("Database connection closed.")
