from typing import List

from model.chunk import Chunk
from model.segment import Segment

import util.tools as tools

class Stripe():
    def __init__(self) -> None:
        self.sid = ""
        self.chunks:List[Chunk] = []
        self.segments:List[Segment] = []

    def add_chunk(self, chunk:Chunk) -> None:
        self.chunks.append(chunk)

    def get_chunks(self) -> List[Chunk]:
        return self.chunks

    def get_chunk_number(self) -> int:
        return len(self.chunks)

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

    def flatten(self) -> List[Chunk]:
        # get all original chunks and global parity chunks
        all_chunks = self.chunks
        global_seg = self.segments[-1]
        for parity in global_seg.get_parities():
            all_chunks.append(parity)
        return all_chunks