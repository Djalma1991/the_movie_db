import json
from os import environ

import httpx

from http_generic import ApiCall


class MovieAPI(ApiCall):
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

    def post(self, params: dict, json: dict) -> bool:
        self.query.update(params)
        post = httpx.post(url=self.uri, params=self.query, json=json)
        result = post.status_code()
        return True if result == 201 else False
