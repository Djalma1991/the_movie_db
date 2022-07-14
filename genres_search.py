from http_generic import ApiCall


def genres():
    call = ApiCall(path="/genre/movie/list")
    r = call.get({"language": "en-US"})
    results = []
    data = r.json()
    results.extend(data["genres"])

    return results
