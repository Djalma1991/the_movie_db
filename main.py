from genres_db import write_db as write_genres
from genres_search import GenresAPI
from movies_db import write_db as write_movies
from movies_search import search_movie_by_name

options = {"1": search_movie_by_name, "2": GenresAPI}


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
        data = func(movie_name)
        write_movies(data)
    elif int(method) == 2:
        data = func()
        results = data.get(params={"language": "en-US"})
        write_genres(results)


if __name__ == "__main__":
    run()
