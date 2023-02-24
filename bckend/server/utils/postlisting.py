from typing import Dict


class PostListing:
    def __init__(self, doc_id: int, score: float, data: Dict):
        self.doc_id = doc_id
        self.score = score
        self.data = data
