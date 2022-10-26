import grpc
import dfs_pb2 as pb2
import dfs_pb2_grpc as pb2_grpc

def add_chunk(cid:str, data:bytes, location:str) -> None:
    while True:
        # add one chunk to chunk server
        with grpc.insecure_channel(location) as channel:
            stub = pb2_grpc.ChunkServerStub(channel)
            response = stub.Write(pb2.WriteRequest(cid=cid, data=data))
        if response.verify:
            break

def get_chunk(cid:str, location:str) -> bytes:
    # get chunk data from chunk server
    with grpc.insecure_channel(location) as channel:
        stub = pb2_grpc.ChunkServerStub(channel)
        response = stub.Read(pb2.String(str=cid))
    return response.data