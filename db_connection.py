from os import environ

import sqlalchemy


def create_connection():
    uri = environ["DB_URI"]
    engine = sqlalchemy.create_engine(uri)
    conn = engine.connect()
    # conn.execution_options(isolation_level="AUTOCOMMIT", autocommit=True)
    return conn
