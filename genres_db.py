import sqlalchemy

from db import DB

metadata = sqlalchemy.MetaData()
genres = sqlalchemy.Table(
    "genres",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INT, primary_key=True, autoincrement=False),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR),
)


class GenresDb(DB):
    def __init__(self):
        super().__init__()
        self.genres: sqlalchemy.Table = genres

    def insert(self, values: dict) -> None:
        row = self.genres.insert().values(**values)
        self.conn.execute(row)

    def update(self, values: dict, id: int) -> None:
        row = self.genres.update().where(self.genres.c.id == id).values(**values)
        self.conn.execute(row)

    def select(self, id: int) -> bool:
        item = self.genres.select().where(self.genres.c.id == id)
        result = self.conn.execute(item).first()
        # return True if result else False
        # Return the value of result (True or False)
        return result is not None


def write_db(data: list[dict]):
    db = GenresDb()
    for item in data:
        if db.select(id=item["id"]):
            id = item.pop("id")
            db.update(values=item, id=id)
        else:
            db.insert(values=item)
