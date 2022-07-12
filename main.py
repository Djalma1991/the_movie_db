from movies_db import write_db
from movies_search import search_movie_by_name


def search_and_write():
    movie = input("Type the name of movie that you want to search informations: ")

    search_movie = search_movie_by_name(movie)
    write_db(search_movie)


if __name__ == "__main__":
    search_and_write()
