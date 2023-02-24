from json import JSONEncoder
from typing import Any, List


class UniResponse:
    def __init__(self, data: List, msg="success", code=200):
        self.code = code
        self.msg = msg
        self.data = data


class Result:
    def __init__(self, url):
        self.url = url
        # something else


class UniResponseEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__
