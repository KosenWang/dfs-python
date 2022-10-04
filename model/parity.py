
class Parity():
    def __init__(self, cid:str, group:int, index:int) -> None:
        self.cid = cid
        self.group = group # 0 is local, 1 is global
        self.index = index # index in parity block list

    def get_index(self) -> int:
        return self.index

    def get_group(self) -> int:
        return self.group

    def get_cid(self) -> str:
        return self.cid