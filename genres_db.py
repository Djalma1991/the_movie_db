import sqlalchemy

from db import DB

metadata = sqlalchemy.MetaData()
movies = sqlalchemy.Table(
    "movies",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INT, primary_key=True, autoincrement=False),
    sqlalchemy.Column("name", sqlalchemy.VARCHAR),
)


class Movie(DB):
    def __init__(self):
        super().__init__()
        self.movie: sqlalchemy.Table = movies

    def insert(self, values: dict) -> None:
        row = self.movie.insert().values(**values)
        self.conn.execute(row)

    def update(self, values: dict, id: int) -> None:
        row = self.movie.update().where(self.movie.c.id == id).values(**values)
        self.conn.execute(row)

    def select(self, id: int) -> bool:
        item = self.movie.select().where(self.movie.c.id == id)
        result = self.conn.execute(item).first()
        # return True if result else False
        # Return the value of result (True or False)
        return result is not None


def write_db(data: list[dict]):
    db = Movie()
    for i, item in enumerate(data):
        if db.select(id=item.get("id")):
            id = item.pop("id")
            db.update(values=item, id=id)
        else:
            db.insert(values=item)
