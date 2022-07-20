import json

from genres_db import write_db as write_genres
from genres_search import GenresAPI
from http_generic import Authenticator, SessionCreater
from movies_db import write_db as write_movies
from movies_search import MovieAPI

options = {"1": MovieAPI, "2": GenresAPI, "3": MovieAPI}


def run():
    print(
        """
        1 - search and write
        2 - genres
        3 - post movie rate
        """
    )
    method = input("Select the function that you want to run: ")
    func = options.get(method)
    if not func:
        raise ValueError("Invalid option")
    if int(method) == 1:
        movie_name = input("Type the name of movie that you're looking for: ")
        params = {
            "language": "en-US",
            "query": movie_name,
            "page": 1,
            "include_adult": True,
        }
        data = func(path="/search/movie")
        results = data.get(params=params)
        write_movies(results)
    elif int(method) == 2:
        data = func()
        results = data.get(params={"language": "en-US"})
        write_genres(results)
    elif int(method) == 3:
        auth = Authenticator(path="/authentication/token/new")
        token = auth.get(params={})
        request_token = {"request_token": token["request_token"]}
        session = SessionCreater("/authentication/session/new")
        session_id = session.post_session_id(request_token)
        movie_id = input("Type the movie id: ")
        path = f"/movie/{movie_id}/rating"
        data = func(path)
        params = {"language": "en-US"}
        rating = input("Type the rating for the movie: ")
        json = {"value": float(rating)}
        results = data.post(params=params, json=json)


if __name__ == "__main__":
    run()
