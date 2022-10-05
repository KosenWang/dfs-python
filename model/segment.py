
from typing import List
from model.chunk import Chunk
from model.parity import Parity
import util.tools as tools

class Segment():
    def __init__(self) -> None:
        self.sid = ""
        self.chunks:List[Chunk] = []
        self.parities:List[Parity] = []
    
    def add_chunk(self, chunk:Chunk) -> None:
        self.chunks.append(chunk)

    def add_parity(self, parity:Parity) -> None:
        self.parities.append(parity)

    def get_sid(self) -> str:
        tmp = ""
        for chunk in self.chunks:
            tmp += chunk.get_cid()
        for parity in self.parities:
            tmp += parity.get_cid()
        self.sid = tools.get_hash_value(tmp.encode('utf-8'))
        return self.sid

    def get_chunk_number(self) -> int:
        return len(self.chunks) + len(self.parities)

    def get_chunks(self) -> List[Chunk]:
        return self.chunks

    def get_parities(self) -> List[Parity]:
        return self.parities

    def chunks_to_str(self) -> List[str]:
        return [chunk.get_cid() for chunk in self.chunks]

    def parities_to_str(self) -> List[str]:
        return [parity.get_cid() for parity in self.parities]