import os
from typing import List

from config.global_config import CHUNK_SIZE
from model.chunk import Chunk, Parity
from model.segment import Segment
from model.stripe import Stripe
from model.file import File

import util.tools as tools
import util.erasure_coding as ec
import util.master_server_command as master_cmd


path = os.path.join('data', 'client')


def file_to_blocks(filename:str) -> List[bytes]:
    # split file to small blocks, the block size is pre-defined.
    # return list of chunks
    dir = os.path.join(path, filename)
    # read file
    with open(dir, 'rb') as f:
        data = f.read()
    # split data
    blocks = []
    while True:
        block = data[0: CHUNK_SIZE]
        # is block empty
        if not block:
            break
        block = bytes(block).ljust(CHUNK_SIZE, b'\x01')
        blocks.append(block)
        data = data[CHUNK_SIZE:]
    
    return blocks


def blocks_to_stripes(blocks:list, count:int) -> List[Stripe]:
    # combine each m blocks to a fix-sized stripe
    # ready to EC backup
    stripes = []
    index = 0
    n = len(blocks)
    while index < n:
        # each stripe has m blocks
        stripe = Stripe()
        for i in range(count):
            if index + i >= n:
                break
            cid = tools.get_hash_value(blocks[index + i])
            stripe.add_chunk(Chunk(cid, index + i))
        stripes.append(stripe)
        index += count
    return stripes


def add_file(filename:str, count:int, m:int, r:int):
    # count: each stripe has count original blocks
    # m : each segment has m original blocks
    # r : the number of global parity chunks 
    blocks = file_to_blocks(filename)
    stripes = blocks_to_stripes(blocks, count)
    file = File()
    for stripe in stripes:
        # data blocks [[block list of local parity], [block list of global parity]]
        parities = ec.encode(m, r, stripe, blocks)
        chunks = stripe.get_chunks()
        # m blocks and 1 local parity is one segment
        for i in range(len(parities[0])):
            segment = Segment()
            # add original chunks
            for j in range(m):
                segment.add_chunk(chunks[i * m + j])
            # add parity chunks
            cid = tools.get_hash_value(parities[0][i])
            segment.add_parity(Parity(cid, i, 0))
            stripe.add_segment(segment)
        # r global parities is also one segment
        segment = Segment()
        for j in range(len(parities[1])):
            cid = tools.get_hash_value(parities[1][j])
            segment.add_parity(Parity(cid, j, 1))
        stripe.add_segment(segment)
        file.add_stripe(stripe)
        # add each segment to master server and chunks in each segment to chunk server
        master_cmd.add_stripe(stripe, blocks, parities)
    print(f'added {file.get_fid()} {filename}')
    return file


def get_file(file:File) -> bytes:
    stripes = file.get_stripes()
    data = bytes()
    try:
        for stripe in stripes:
            raw_data = master_cmd.get_stripe(stripe)
            data += ec.decode(stripe, raw_data)
        print(data)
    except Exception:
        print("Get file failed")


def delete_file(file:File) -> str:
    stripes = file.get_stripes()
    for stripe in stripes:
        master_cmd.delete_stripe(stripe)
    print("Delete file successfully")



if __name__ == "__main__":
    filename = "hello.txt"
    new_file = add_file(filename, 2, 2, 2)
    get_file(new_file)
    delete_file(new_file)