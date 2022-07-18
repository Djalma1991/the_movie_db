from http_generic import ApiCall


class GenresAPI(ApiCall):
    def __init__(self, path="/genre/movie/list") -> None:
        super().__init__(path)

    def get(self) -> None:
        ...
