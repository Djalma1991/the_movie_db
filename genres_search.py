import json
from os import environ

import httpx


def genres():
    uri = "https://api.themoviedb.org/3/genre/movie/list"
    query = {"api_key": environ["API_KEY"], "language": "en-US", "page": 1}
    results = []
    resp = httpx.get(url=uri, params=query)
    data = resp.json()
    results.extend(data["genres"])

    return results
