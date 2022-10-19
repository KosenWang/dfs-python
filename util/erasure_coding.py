from typing import List
import zfec

from model.chunk import Chunk
from model.segment import Segment
from model.stripe import Stripe

import util.tools as tools

def encode(m:int, r:int, stripe:List[bytes]) -> List[List[bytes]]:
    # k: the number of data chunks
    # n : divide k data chunks into n groups; each group has 1 local parity chunk
    # r : the number of global parity chunks
    # m : each group has m original blocks
    # return data blocks [[block list of chunks]
    k = len(stripe)
    n = k // m
    segs:List[List[bytes]]= []
    # calculate local parity chunks
    index = 0
    for i in range(n):
        local_seg:List[bytes] = zfec.Encoder(m, m + 1).encode(stripe[index: index+m])
        segs.append(local_seg)
        index += m
    # calculate global parity chunks
    global_seg:List[bytes] = zfec.Encoder(k, k + r).encode(stripe[0: k]) 
    segs.append(global_seg[k: k+r])
    return segs


def decode(blocks:List[bytes]) -> bytes:
    data = bytes()
    for block in blocks:
            data += block.rstrip(b'\x01')
    return data


def local_decode(blocks:List[bytes], indexes:List[int]) -> List[bytes]:
    k = len(blocks)
    # ec decode using local parity chunk
    decode_blocks = zfec.Decoder(k, k + 1).decode(blocks, indexes)
    return decode_blocks
    

def global_decode(blocks:List[bytes], indexes:List[int], r:int) -> List[bytes]:
    k = len(blocks)
    # ec decode using global parity chunk
    decode_blocks = zfec.Decoder(k, k + r).decode(blocks, indexes)
    return decode_blocks
    