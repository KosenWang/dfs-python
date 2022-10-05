import os
import sys

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
        ip_address = request.ip
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
        sid = request.sid
        chunks = request.chunks
        parities = request.parities
        chunk_location = request.chunk_location
        parity_location = request.parity_location
        # add segment name space
        self.name_space[sid] = (chunks, parities)
        localtime = tools.get_localtime()
        print(localtime, f"Added segment {sid} to name space.")
        print()
        print("--------------------Current Name Space--------------------")
        print(self.name_space)
        print("----------------------------------------------------------")
        print()
        # add each chunk's location
        for i in range(len(chunks)):
            self.chunk_table[chunks[i]] = chunk_location[i]
        for j in range(len(parities)):
            self.chunk_table[parities[j]] = parity_location[j]
        localtime = tools.get_localtime()
        print(localtime, "Checked current chunk table.")
        print()
        print("--------------------Current Chunk Table--------------------")
        print(self.chunk_table)
        print("-----------------------------------------------------------")
        print()
        return pb2.Empty()


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    pb2_grpc.add_MasterServerServicer_to_server(MasterServer(), server)
    server.add_insecure_port(address)
    print("Master Server is Running")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":
    run()