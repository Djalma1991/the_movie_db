from genres_db import write_db as write_genres
from genres_search import GenresAPI
from movies_db import write_db as write_movies
from movies_search import MovieAPI

options = {"1": MovieAPI, "2": GenresAPI}


def run():
    print(
        """
        1 - search and write
        2 - genres"""
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
        data = func()
        results = data.get(params=params)
        write_movies(results)
    elif int(method) == 2:
        data = func()
        results = data.get(params={"language": "en-US"})
        write_genres(results)


if __name__ == "__main__":
    run()
