import sqlalchemy

from db_connection import create_connection

conn = create_connection()

metadata = sqlalchemy.MetaData()
movies = sqlalchemy.Table(
    "movies",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INT, primary_key=True, autoincrement=False),
    sqlalchemy.Column("adult", sqlalchemy.VARCHAR),
    sqlalchemy.Column("backdrop_path", sqlalchemy.VARCHAR),
    sqlalchemy.Column("genre_ids", sqlalchemy.VARCHAR),
    sqlalchemy.Column("original_language", sqlalchemy.VARCHAR),
    sqlalchemy.Column("original_title", sqlalchemy.VARCHAR),
    sqlalchemy.Column("overview", sqlalchemy.VARCHAR),
    sqlalchemy.Column("popularity", sqlalchemy.DECIMAL(17, 3)),
    sqlalchemy.Column("poster_path", sqlalchemy.VARCHAR),
    sqlalchemy.Column("release_date", sqlalchemy.DATE),
    sqlalchemy.Column("title", sqlalchemy.VARCHAR),
    sqlalchemy.Column("video", sqlalchemy.BOOLEAN),
    sqlalchemy.Column("vote_average", sqlalchemy.DECIMAL(10, 2)),
    sqlalchemy.Column("vote_count", sqlalchemy.BIGINT),
)


def write_db(data):
    for item in data:
        item["release_date"] = item["release_date"] if item.get("release_date") else None
        row = movies.insert().values(**item)
        conn.execute(row)
