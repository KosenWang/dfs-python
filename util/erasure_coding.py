from typing import List
import zfec

from model.chunk import Chunk
from model.segment import Segment
from model.stripe import Stripe

import util.tools as tools

def encode(m:int, r:int, stripe:Stripe, blocks:List[bytes]) -> List[List[bytes]]:
    # k: the number of data chunks
    # n : divide k data chunks into n groups; each group has 1 local parity chunk
    # r : the number of global parity chunks
    # m : each group has m original blocks
    # return data blocks [[block list of local parity], [block list of global parity]]
    k = stripe.get_chunk_number()
    n = k // m
    # get indexes of blocks
    chunks = stripe.get_chunks()
    head:Chunk = chunks[0]
    start = head.get_index()
    # calculate local parity chunks
    parities = [[]]
    index = start
    for i in range(n):
        local_parity:List[bytes] = zfec.Encoder(m, m + 1).encode(blocks[index: index+m])
        parities[0].append(local_parity[-1])
        index += m
    # calculate global parity chunks
    global_parity:List[bytes] = zfec.Encoder(k, k + r).encode(blocks[start: start+k]) 
    parities.append(global_parity[k: k+r])
    return parities


def decode(stripe:Stripe, raw_data:List[List[bytes]]) -> bytes:
    segments = stripe.get_segments()
    m = segments[0].get_chunk_number() - 1
    data = bytes()
    # decode each segment
    try:
        for i in range(len(segments) - 1):
            blocks = raw_data[i]
            data += local_decode(segments[i], blocks)
    except Exception:
        data = global_decode(stripe, raw_data, m)
    return data


def local_decode(segment:Segment, blocks:List[bytes]) -> bytes:
    k = segment.get_chunk_number()
    chunks = segment.get_chunks()
    parities = segment.get_parities()
    # get consist index, remove not consist
    index = []
    # check chunks
    for i in range(k - 1):
        index.append(i)
        if tools.get_hash_value(blocks[i]) != chunks[i].get_cid():
            del blocks[i]
            index.remove(i)
    # decode directly
    data = bytes()
    # if (len(index) == k - 1):
    #     for i in range(k - 1):
    #         data += blocks[i]
    #     return data
    # check parity
    index.append(k - 1)
    if tools.get_hash_value(blocks[k - 1]) != parities[0].get_cid():
        del blocks[k - 1]
        index.remove(k - 1)
    # ec decode using local parity chunk
    decode_blocks = zfec.Decoder(k - 1, k).decode(blocks, index)
    for block in decode_blocks:
            data += block.rstrip(b'\x01')
    return data
    

def global_decode(stripe:Stripe, raw_data:List[List[bytes]], m:int) -> bytes:
    # each segment has m original chunks
    all_chunks = stripe.flatten()
    blocks = []
    index = [] 
    # add original chunks data
    for i in range(len(raw_data) - 1):
        for j in range(m):
            blocks.append(raw_data[i][j])
            index.append(i * m + j)
    # add global parity chunks data
    r = len(raw_data[-1])
    tmp = len(blocks)
    for i in range(r):
        blocks.append(raw_data[-1][i])
        index.append(tmp + i)
    # check consistency   
    for i in range(len(blocks) - 1, -1, -1):
        if tools.get_hash_value(blocks[i]) != all_chunks[i].get_cid():
            del blocks[i]
            index.remove(i)
    # ec decode using global parity chunk
    n = len(all_chunks)
    data = bytes()
    decode_blocks = zfec.Decoder(n - r, n).decode(blocks, index)
    for block in decode_blocks:
            data += block.rstrip(b'\x01')
    return data