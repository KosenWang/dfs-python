from typing import List, Tuple
import grpc
import dfs_pb2 as pb2
import dfs_pb2_grpc as pb2_grpc

from model.segment import Segment
from model.stripe import Stripe
import util.chunk_server_command as chunk_cmd


def add_stripe(stripe:Stripe, data_blocks:List[bytes], parity_blocks:List[List[bytes]]) -> None:
    segments = stripe.get_segments()
    for segment in segments:
            master = find_master(segment)
            add_segment(segment, data_blocks, parity_blocks, master)


def add_segment(segment:Segment, data_blocks:List[bytes], parity_blocks:List[List[bytes]], master:str) -> None:
    # add one segment to one orgnization
    # k: chunk number in one segment
    k = segment.get_chunk_number()
    chunks = segment.get_chunks()
    parities = segment.get_parities()
    sid = segment.get_sid()
    peers = get_peers(k, master)
    # add each chunk to chunk server
    index = 0
    for chunk in chunks:
        chunk_cmd.add_chunk(chunk.get_cid(), data_blocks[chunk.get_index()], peers[index])
        index += 1
    for parity in parities:
        chunk_cmd.add_chunk(parity.get_cid(), parity_blocks[parity.get_group()][parity.get_index()], peers[index])
        index += 1
    # add segment info to master server
    with grpc.insecure_channel(master) as channel:
        stub = pb2_grpc.MasterServerStub(channel)
        stub.AddSegment(pb2.SegmentRequest(sid=sid, 
                                           chunks=segment.flatten_to_str(), 
                                           locations=peers))


def get_stripe(stripe:Stripe) -> List[List[bytes]]:
    segments = stripe.get_segments()
    # [[data of original and local parity chunks],...,[data of global parity chunks]]
    raw_data = []
    for segment in segments:
        raw_data.append(get_segment(segment))
    return raw_data


def get_segment(segment:Segment) -> List[bytes]:
    locations = get_locations(segment)
    all_chunks = segment.flatten()
    # add data to a list, ready to decode
    blocks = []
    for i in range(len(all_chunks)):
        data = chunk_cmd.get_chunk(all_chunks[i].get_cid(), locations[i])
        blocks.append(data)
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
    return response.locations


def find_master(segment:Segment) -> str:
    # find master based on segment id
    return "localhost:8080"