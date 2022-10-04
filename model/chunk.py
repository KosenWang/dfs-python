class Chunk():
    def __init__(self, cid:str, index:int) -> None:
        self.cid = cid
        self.index = index # index in chunk list

    def get_index(self):
        return self.index

    def get_cid(self) -> str:
        return self.cid