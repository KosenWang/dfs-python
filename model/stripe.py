from typing import List

from model.chunk import Chunk
from model.segment import Segment

import util.tools as tools

class Stripe():
    def __init__(self) -> None:
        self.sid = ""
        self.segments:List[Segment] = []

    def add_segment(self, segment:Segment) -> None:
        self.segments.append(segment)

    def get_segments(self) -> List[Segment]:
        return self.segments

    def get_sid(self) -> str:
        if len(self.sid) == 0:
            tmp = ""
            for segment in self.segments:
                tmp += segment.get_sid()
            self.sid = tools.get_hash_value(tmp.encode('utf-8'))
        return self.sid

    def get_chunk_number(self) -> int:
        n = 0
        for i in range(len(self.segments) - 1):
            n += self.segments[i].get_chunk_number() - 1
        return n