import sqlalchemy

CONNECTION_STRING: str = "mysql://{user}:{password}@{host}:{port}/{database}"


class DatabaseConnector:
    '''Sqlalchemy database to connection'''

    def __init__(self) -> None:
        self.database = "finaldb"
        self.user = "root"
        self.password = "finaldb"
        self.host = "mysqldb"
        self.port = "3306"

    def engine(self):
        '''Start database connection

            Args:
                None.

            Return:
                Method: Engine to access database. '''

        print('Creating engine...')
        engine = sqlalchemy.create_engine(CONNECTION_STRING.format(user=self.user,
                                                                   password=self.password,
                                                                   host=self.host,
                                                                   port=self.port,
                                                                   database=self.database))
        self.engine = engine
        return self.engine
