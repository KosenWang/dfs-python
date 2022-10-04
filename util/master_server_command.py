from typing import List

from model.segment import Segment


def add_segment(segment:Segment, blocks:List[bytes], parities:List[List[bytes]]) -> None:
    # add one segment to one orgnization
    # k: chunk number in one segment
    k = segment.get_chunk_number()
    pass