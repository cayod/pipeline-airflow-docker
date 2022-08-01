import sqlalchemy

connection_string = "mysql://{user}:{password}@{host}:{port}/{database}"


class DatabaseConnector:

    def __init__(self):
        self.database = "finaldb"
        self.user = "root"
        self.password = "finaldb"
        self.host = "mysqldb"
        self.port = "3306"

    def engine(self):
        print('Creating engine...')
        engine = sqlalchemy.create_engine(connection_string.format(user=self.user,
                                                                   password=self.password,
                                                                   host=self.host,
                                                                   port=self.port,
                                                                   database=self.database))
        self.engine = engine
        return self.engine
