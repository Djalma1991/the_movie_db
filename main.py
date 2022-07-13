from genres_search import genres
from movies_db import write_db
from movies_search import search_movie_by_name

options = {"1": search_movie_by_name, "2": genres}


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
        func(movie_name)
    else:
        func()


if __name__ == "__main__":
    run()
