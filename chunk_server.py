import os
import sys

import grpc
import dfs_pb2 as pb2
import dfs_pb2_grpc as pb2_grpc
from concurrent import futures

import util.tools as tools


path = os.path.join('data', sys.argv[2])
address = 'localhost:' + sys.argv[1]


class ChunkServer(pb2_grpc.ChunkServerServicer):
    
    def __init__(self) -> None:
        self.datastore = set()

        ls = os.listdir(path)
        for cid in ls:
            self.datastore.add(cid)
        localtime = tools.get_localtime()
        print(localtime, "Synced datastore.")
        print()
        print("--------------------Current Datastore--------------------")
        print(self.datastore)
        print("---------------------------------------------------------")
        print()
        # TODO: register to master server


    def Write(self, request, context) -> pb2.Empty:
        data:bytes = request.data
        cid:str = request.cid
        # write data to a file
        dir = os.path.join(path, cid)
        with open(dir, 'wb') as f:
            f.write(data)
        # sync local datastore
        self.datastore.add(cid)
        localtime = tools.get_localtime()
        print(localtime, f"added chunk {cid} to datastore.")
        print()
        print("--------------------Current Datastore--------------------")
        print(self.datastore)
        print("---------------------------------------------------------")
        print()
        return pb2.Empty()


    def GetChunks(self, request, context):
        chunks = []
        for cid in self.datastore:
            chunks.append(cid)
        return pb2.StringList(strs=chunks)


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    pb2_grpc.add_ChunkServerServicer_to_server(ChunkServer(), server)
    server.add_insecure_port(address)
    print("Chunk Server is Running")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":
    run()