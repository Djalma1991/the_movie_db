import json
from os import environ

import httpx

from http_generic import ApiCall


class MovieAPI(ApiCall):
    def __init__(self, path="/search/movie") -> None:
        super().__init__(path)

    def get(self, params: dict) -> list[dict]:

        results = []
        while True:
            self.query.update(params)
            resp = httpx.get(url=self.uri, params=self.query)
            data = resp.json()
            results.extend(data["results"])
            params["page"] = params["page"] + 1
            if not data["results"]:
                break

        return results
