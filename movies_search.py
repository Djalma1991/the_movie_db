import json
from os import environ

import httpx


def search_movie_by_name(movie_name):
    uri = "https://api.themoviedb.org/3/search/movie"
    query = {
        "api_key": environ["API_KEY"],
        "language": "en-US",
        "query": movie_name,
        "page": 1,
        "include_adult": True,
    }

    results = []
    while True:
        resp = httpx.get(url=uri, params=query)
        data = resp.json()
        results.extend(data["results"])
        query["page"] = query["page"] + 1
        if not data["results"]:
            break

    return results
