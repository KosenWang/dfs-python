from typing import List

from model.chunk import Chunk
from model.segment import Segment

class Stripe():
    def __init__(self) -> None:
        self.chunks = []
        self.segments = []

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