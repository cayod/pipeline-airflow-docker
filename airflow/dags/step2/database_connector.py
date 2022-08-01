import sqlalchemy

connection_string = "mysql://{user}:{password}@{host}:{port}/{database}"


class DatabaseConnector:

    def __init__(self):
        self.database = "finaldb"
        self.user = "root"
        self.password = "123456"
        self.host = "127.0.0.1"
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
