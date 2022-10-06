class Chunk():
    def __init__(self, cid:str, index:int) -> None:
        self.cid = cid
        self.index = index # index in chunk list

    def get_index(self):
        return self.index

    def get_cid(self) -> str:
        return self.cid

class Parity(Chunk):
    def __init__(self, cid:str, index:int, group:int) -> None:
        super().__init__(cid, index)
        self.group = group # 0 is local, 1 is global

    def get_group(self) -> int:
        return self.group