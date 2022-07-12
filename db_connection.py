import sqlalchemy


def create_connection():
    uri = "postgresql://postgres:postgrespw@localhost:49156/postgres"
    engine = sqlalchemy.create_engine(uri)
    conn = engine.connect()
    conn.execution_options(isolation_level="AUTOCOMMIT", autocommit=True)
    return conn
