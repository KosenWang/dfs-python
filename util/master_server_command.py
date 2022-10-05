from typing import List
import grpc
import dfs_pb2 as pb2
import dfs_pb2_grpc as pb2_grpc

from model.segment import Segment
import util.chunk_server_command as chunk_cmd

def add_segment(segment:Segment, data_blocks:List[bytes], parity_blocks:List[List[bytes]], master:str) -> str:
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
    chunk_location = peers[0:index]
    parity_location = peers[index:]
    for parity in parities:
        chunk_cmd.add_chunk(parity.get_cid(), parity_blocks[parity.get_group()][parity.get_index()], peers[index])
        index += 1
    # add segment info to master server
    with grpc.insecure_channel(master) as channel:
        stub = pb2_grpc.MasterServerStub(channel)
        stub.AddSegment(pb2.SegmentRequest(sid=sid, 
                                           chunks=segment.chunks_to_str(), 
                                           parities=segment.parities_to_str(), 
                                           chunk_location=chunk_location, 
                                           parity_location=parity_location))
    return sid

def get_peers(k:int, master:str) -> List[str]:
    # get the ip address of peers which are ready for add file and backup
    with grpc.insecure_channel(master) as channel:
        stub = pb2_grpc.MasterServerStub(channel)
        response = stub.GetPeers(pb2.Number(num=k))
    return response.strs