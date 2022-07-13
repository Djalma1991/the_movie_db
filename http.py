from os import environ

import httpx


class HTTP:
    def __init__(self, path: str) -> None:
        self.uri = "https://api.themoviedb.org/3" + path
        self.http = httpx.Client()
        self.query = {"api_key": environ["API_KEY"]}

    def get(self, params: dict) -> list[dict]:
        self.query.update(params)
