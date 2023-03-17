from json import JSONEncoder
from typing import Any, Dict


class UniResponse:
    def __init__(self, data: Dict, msg="success", code=200):
        self.code = code
        self.msg = msg
        self.data = data


class Result:
    def __init__(self, doc_id, score, source):
        self.doc_id = doc_id
        self.score = score
        self.source = source

    def __repr__(self):
        return f'Result(id: {self.doc_id}, score: {self.score}, source: {self.source})'


class UniResponseEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__
