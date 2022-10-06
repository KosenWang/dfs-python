
from typing import List
from model.stripe import Stripe
import util.tools as tools

class File():
    def __init__(self) -> None:
        self.fid = ""
        self.stripes:List[Stripe] = []

    def add_stripe(self, stripe:Stripe) -> None:
        self.stripes.append(stripe)

    def get_fid(self) -> str:
        if len(self.fid) == 0:
            tmp = ""
            for stripe in self.stripes:
                tmp += stripe.get_sid()
            self.fid = tools.get_hash_value(tmp.encode('utf-8'))
        return self.fid

    def get_stripes(self) -> List[Stripe]:
        return self.stripes