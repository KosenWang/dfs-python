
class Chunk():
    def __init__(self, cid:str, i:int, j:int) -> None:
        self.cid = cid
        self.seg_index = i # index in seg list
        self.chunk_index = j # index in chunk list

    def get_cid(self) -> str:
        return self.cid

    def get_seg_index(self) -> int:
        return self.seg_index

    def get_chunk_index(self) -> int:
        return self.chunk_index