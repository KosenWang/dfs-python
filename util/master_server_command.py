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
    k = segment.get_chunk_number()
    chunks = segment.get_chunks()
    sid = segment.get_sid()
    peers = get_peers(k, master)
    # add each chunk to chunk server
    index = 0
    for chunk in chunks:
        chunk_cmd.add_chunk(chunk.get_cid(), data_blocks[chunk.get_seg_index()][chunk.get_chunk_index()], peers[index])
        index += 1
    # add segment info to master server
    with grpc.insecure_channel(master) as channel:
        stub = pb2_grpc.MasterServerStub(channel)
        stub.AddSegment(pb2.SegmentRequest(sid=sid, 
                                           chunks=segment.flatten_to_str(), 
                                           locations=peers))


def get_stripe(stripe:Stripe, r:int) -> bytes:
    # m : each segment has m original blocks
    # r : the number of global parity chunks 
    segments = stripe.get_segments()
    n = len(segments)
    k = stripe.get_chunk_number()
    # [[data of original and local parity chunks],...,[data of global parity chunks]]
    raw_data = []
    global_parities = []
    index = 0
    indexes = []
    for i in range(n - 1):
        blocks = get_segment(segments[i])
        for j in range(len(blocks)):   
            raw_data.append(blocks[j])
            indexes.append(index + j)
        index += segments[i].get_chunk_number() - 1
    # local decode failed
    if len(raw_data) != k:
        # get global parity chunks
        if len(global_parities) == 0:
            global_seg = segments[-1]
            chunks = global_seg.get_chunks()
            locations = get_locations(global_seg)
            for j in len(chunks):
                global_parities.append(chunk_cmd.get_chunk(chunks[j].get_cid(), locations[j]))
        # add global parity chunk  
        for parity in global_parities:
            raw_data.append(parity)
            indexes.append(index)
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
    if len(blocks) == k - 1:
        return blocks
    else:
        return []


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


def get_peers(k:int, master:str) -> List[str]:
    # get the ip address of peers which are ready for add file and backup
    with grpc.insecure_channel(master) as channel:
        stub = pb2_grpc.MasterServerStub(channel)
        response = stub.GetPeers(pb2.Number(num=k))
    return response.strs


def get_locations(segment:Segment) -> List[str]:
    # get locations of all chunks in one segment
    master = find_master(segment)
    sid = segment.get_sid()
    with grpc.insecure_channel(master) as channel:
        stub = pb2_grpc.MasterServerStub(channel)
        response = stub.GetLocations(pb2.String(str=sid))
    return response.strs


def find_master(segment:Segment) -> str:
    # find master based on segment id
    return "localhost:8080"