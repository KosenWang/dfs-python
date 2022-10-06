import os
import sys
from typing import List

import grpc
import dfs_pb2 as pb2
import dfs_pb2_grpc as pb2_grpc
from concurrent import futures

import util.tools as tools

address = 'localhost:' + sys.argv[1]

class MasterServer(pb2_grpc.MasterServerServicer):

    def __init__(self) -> None:
        self.peer_table = set()
        self.chunk_table = {}
        self.name_space = {}


    def RegisterPeer(self, request, context):
        ip_address:str = request.str
        self.peer_table.add(ip_address)
        localtime = tools.get_localtime()
        print(localtime, f"{ip_address} registered to master server.")
        print()
        print("--------------------Current Peer Table--------------------")
        print(self.peer_table)
        print("----------------------------------------------------------")
        print()
        return pb2.Empty()


    def GetPeers(self, request, context):
        num = request.num
        peers = []
        count = 0
        for peer in self.peer_table:
            peers.append(peer)
            count += 1
            if count == num:
                break
        return pb2.StringList(strs=peers)

    
    def AddSegment(self, request, context):
        sid:str = request.sid
        chunks:List[str] = request.chunks
        locations:List[str] = request.locations
        # add segment name space
        self.name_space[sid] = chunks
        localtime = tools.get_localtime()
        print(localtime, f"Added segment {sid} to name space.")
        print()
        print("--------------------Current Name Space--------------------")
        print(self.name_space)
        print("----------------------------------------------------------")
        print()
        # add each chunk's location
        for i in range(len(chunks)):
            cid = chunks[i]
            # if cid in self.chunk_table:
            #     self.delete_chunk(cid, self.chunk_table.get(cid))
            self.chunk_table[cid] = locations[i]
        localtime = tools.get_localtime()
        print(localtime, "Checked current chunk table.")
        print()
        print("--------------------Current Chunk Table--------------------")
        print(self.chunk_table)
        print("-----------------------------------------------------------")
        print()
        return pb2.Empty()


    def GetLocations(self, request, context):
        sid:str = request.str
        chunks:List[str] = self.name_space.get(sid, [])
        locations = []
        for cid in chunks:
            locations.append(self.chunk_table.get(cid))
        return pb2.Locations(locations=locations)


    def DeleteSegment(self, request, context):
        sid:str = request.str
        chunks:List[str] = self.name_space.get(sid, tuple())
        for cid in chunks:
            if cid in self.chunk_table:
                self.delete_chunk(cid, self.chunk_table.get(cid))
                self.chunk_table.pop(cid, "Not found")
        self.name_space.pop(sid, "Not found")
        localtime = tools.get_localtime()
        print(localtime, f"Deleted segment {sid} from system.")
        print()
        print("--------------------Current Name Space--------------------")
        print(self.name_space)
        print("----------------------------------------------------------")
        print()
        print("-------------------Current Chunk Table--------------------")
        print(self.chunk_table)
        print("----------------------------------------------------------")
        print()
        return pb2.Empty()


    def delete_chunk(self, cid:str, location:str) -> None:
        with grpc.insecure_channel(location) as channel:
            stub = pb2_grpc.ChunkServerStub(channel)
            stub.Delete(pb2.String(str=cid))

def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    pb2_grpc.add_MasterServerServicer_to_server(MasterServer(), server)
    server.add_insecure_port(address)
    print("Master Server is Running")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":
    run()