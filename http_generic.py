from os import environ

import httpx


class ApiCall:
    def __init__(self, path: str) -> None:
        self.uri = "https://api.themoviedb.org/3" + path
        self.http = httpx.Client()
        self.query = {"api_key": environ["API_KEY"]}

    def get(self, params: dict) -> list[dict]:
        self.query.update(params)
        resp = httpx.get(self.uri, params=self.query)
        return resp.json()


class Authenticator(ApiCall):
    def get_authentication(self) -> str:
        ...


class SessionCreater(ApiCall):
    def post_session_id(self, refresh_token: dict) -> str:
        params = self.query
        post = httpx.post(url=self.uri, params=params, json=refresh_token)
        result = post.status_code
        session_id = post
        return result
