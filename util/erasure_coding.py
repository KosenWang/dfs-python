from typing import List
import zfec

from model.chunk import Chunk
from model.stripe import Stripe

def encode(m:int, r:int, stripe:Stripe, blocks:List[bytes]) -> List[bytes]:
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