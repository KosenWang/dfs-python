from typing import List, Tuple
import grpc
import dfs_pb2 as pb2
import dfs_pb2_grpc as pb2_grpc

from model.segment import Segment
from model.stripe import Stripe
import util.chunk_server_command as chunk_cmd
import util.tools as tools
import util.erasure_coding as ec


def add_stripe(stripe:Stripe, data_blocks:List[bytes]) -> None:
    segments = stripe.get_segments()
    for segment in segments:
            master = find_master(segment)
            add_segment(segment, data_blocks, master)


def add_segment(segment:Segment, data_blocks:List[List[bytes]], master:str) -> None:
    # add one segment to one orgnization
    # k: chunk number in one segment
    chunks = segment.get_chunks()
    sid = segment.get_sid()
    # add segment info to master server
    with grpc.insecure_channel(master) as channel:
        stub = pb2_grpc.MasterServerStub(channel)
        response = stub.AddSegment(pb2.SegmentRequest(sid=sid, 
                                           chunks=segment.flatten_to_str()))
    peers:List[str] = response.strs
    # add each chunk to chunk server
    index = 0
    for chunk in chunks:
        chunk_cmd.add_chunk(chunk.get_cid(), data_blocks[chunk.get_seg_index()][chunk.get_chunk_index()], peers[index])
        index += 1
    

def get_stripe(stripe:Stripe) -> bytes:
    segments = stripe.get_segments()
    n = len(segments)
    k = stripe.get_chunk_number()
    # [[data of original and local parity chunks],...,[data of global parity chunks]]
    raw_data:List[bytes] = []
    index = 0
    indexes:List[int] = []
    # get each data in each segment
    for i in range(n - 1):
        blocks = get_segment(segments[i])
        for j in range(len(blocks)):   
            raw_data.append(blocks[j])
            indexes.append(index + j)
        index += segments[i].get_chunk_number() - 1
    # local decode failed
    if len(raw_data) != k:
        # how many original chunks are missing
        diff = k - len(raw_data)
        # get global parity chunks
        global_seg = segments[-1]
        # r : the number of global parity chunks 
        r = global_seg.get_chunk_number()
        chunks = global_seg.get_chunks()
        locations = get_locations(global_seg)
        for j in range(r):
            if diff == 0:
                break
            data = chunk_cmd.get_chunk(chunks[j].get_cid(), locations[j])
            if tools.get_hash_value(data) == chunks[j].get_cid():
                raw_data.append(data)
                indexes.append(index)
                diff -= 1
            index += 1
        raw_data = ec.global_decode(raw_data, indexes, r)
    return ec.decode(raw_data)


def get_segment(segment:Segment) -> List[bytes]:
    locations = get_locations(segment)
    chunks = segment.get_chunks()
    k = segment.get_chunk_number()
    # add data to a list, ready to decode
    blocks:List[bytes] = []
    indexes:List[int] = []
    # get original data
    for i in range(k - 1):
        data = chunk_cmd.get_chunk(chunks[i].get_cid(), locations[i])
        if tools.get_hash_value(data) == chunks[i].get_cid():
            blocks.append(data)
            indexes.append(i)
    # need local ec or not
    if len(blocks) == k - 2:
        local_parity = chunk_cmd.get_chunk(chunks[k-1].get_cid(), locations[k-1])
        if tools.get_hash_value(local_parity) == chunks[k-1].get_cid():
            blocks.append(local_parity)
            indexes.append(k-1)
            blocks = ec.local_decode(blocks, indexes)
    return blocks


def delete_stripe(stripe:Stripe) -> None:
    segments = stripe.get_segments()
    for segment in segments:
        delete_segment(segment)


def delete_segment(segment:Segment) -> None:
    master = find_master(segment)
    sid = segment.get_sid()
    with grpc.insecure_channel(master) as channel:
        stub = pb2_grpc.MasterServerStub(channel)
        stub.DeleteSegment(pb2.String(str=sid))


def get_locations(segment:Segment) -> List[str]:
    # get locations of all chunks in one segment
    master = find_master(segment)
    sid = segment.get_sid()
    with grpc.insecure_channel(master) as channel:
        stub = pb2_grpc.MasterServerStub(channel)
        response = stub.GetLocations(pb2.String(str=sid))
    return response.strs


def find_master(segment:Segment) -> str:
    # TODO: find master based on segment id
    k = segment.get_chunk_number()
    i = k % 2
    masters:List[str] = [ "localhost:9090", "localhost:8080"]
    return masters[i]