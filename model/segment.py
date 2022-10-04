
from model.chunk import Chunk
from model.parity import Parity
import util.tools as tools

class Segment():
    def __init__(self) -> None:
        self.sid = ""
        self.chunks = []
        self.parities = []
    
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