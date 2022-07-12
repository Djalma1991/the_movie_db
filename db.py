from os import environ

import sqlalchemy


class DB:
    def __init__(self):
        self.uri = environ["DB_URI"]
        self.engine = sqlalchemy.create_engine(self.uri)
        self.conn = self.engine.connect()
        self.conn.execution_options(isolation_level="AUTOCOMMIT", autocommit=True)

    def __del__(self):
        if not self.conn.closed:
            self.conn.close()
