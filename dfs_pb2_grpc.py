# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dfs_pb2 as dfs__pb2


class ChunkServerStub(object):
    """The chunk server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Read = channel.unary_unary(
                '/dfs.ChunkServer/Read',
                request_serializer=dfs__pb2.ChunkId.SerializeToString,
                response_deserializer=dfs__pb2.Bytes.FromString,
                )
        self.Write = channel.unary_unary(
                '/dfs.ChunkServer/Write',
                request_serializer=dfs__pb2.WriteRequest.SerializeToString,
                response_deserializer=dfs__pb2.Empty.FromString,
                )
        self.Delete = channel.unary_unary(
                '/dfs.ChunkServer/Delete',
                request_serializer=dfs__pb2.ChunkId.SerializeToString,
                response_deserializer=dfs__pb2.Empty.FromString,
                )
        self.GetChunks = channel.unary_unary(
                '/dfs.ChunkServer/GetChunks',
                request_serializer=dfs__pb2.Empty.SerializeToString,
                response_deserializer=dfs__pb2.StringList.FromString,
                )


class ChunkServerServicer(object):
    """The chunk server
    """

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChunks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChunkServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=dfs__pb2.ChunkId.FromString,
                    response_serializer=dfs__pb2.Bytes.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=dfs__pb2.WriteRequest.FromString,
                    response_serializer=dfs__pb2.Empty.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=dfs__pb2.ChunkId.FromString,
                    response_serializer=dfs__pb2.Empty.SerializeToString,
            ),
            'GetChunks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChunks,
                    request_deserializer=dfs__pb2.Empty.FromString,
                    response_serializer=dfs__pb2.StringList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dfs.ChunkServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChunkServer(object):
    """The chunk server
    """

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.ChunkServer/Read',
            dfs__pb2.ChunkId.SerializeToString,
            dfs__pb2.Bytes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.ChunkServer/Write',
            dfs__pb2.WriteRequest.SerializeToString,
            dfs__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.ChunkServer/Delete',
            dfs__pb2.ChunkId.SerializeToString,
            dfs__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChunks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.ChunkServer/GetChunks',
            dfs__pb2.Empty.SerializeToString,
            dfs__pb2.StringList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MasterServerStub(object):
    """master server
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterPeer = channel.unary_unary(
                '/dfs.MasterServer/RegisterPeer',
                request_serializer=dfs__pb2.RegisterRequest.SerializeToString,
                response_deserializer=dfs__pb2.Empty.FromString,
                )
        self.CheckChunks = channel.unary_unary(
                '/dfs.MasterServer/CheckChunks',
                request_serializer=dfs__pb2.Empty.SerializeToString,
                response_deserializer=dfs__pb2.Empty.FromString,
                )
        self.GetFile = channel.unary_unary(
                '/dfs.MasterServer/GetFile',
                request_serializer=dfs__pb2.String.SerializeToString,
                response_deserializer=dfs__pb2.ChunkList.FromString,
                )
        self.DeleteFile = channel.unary_unary(
                '/dfs.MasterServer/DeleteFile',
                request_serializer=dfs__pb2.String.SerializeToString,
                response_deserializer=dfs__pb2.String.FromString,
                )
        self.GetPeers = channel.unary_unary(
                '/dfs.MasterServer/GetPeers',
                request_serializer=dfs__pb2.Number.SerializeToString,
                response_deserializer=dfs__pb2.StringList.FromString,
                )
        self.NameSpace = channel.unary_unary(
                '/dfs.MasterServer/NameSpace',
                request_serializer=dfs__pb2.NameRequest.SerializeToString,
                response_deserializer=dfs__pb2.Empty.FromString,
                )


class MasterServerServicer(object):
    """master server
    """

    def RegisterPeer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckChunks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NameSpace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MasterServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterPeer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPeer,
                    request_deserializer=dfs__pb2.RegisterRequest.FromString,
                    response_serializer=dfs__pb2.Empty.SerializeToString,
            ),
            'CheckChunks': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckChunks,
                    request_deserializer=dfs__pb2.Empty.FromString,
                    response_serializer=dfs__pb2.Empty.SerializeToString,
            ),
            'GetFile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFile,
                    request_deserializer=dfs__pb2.String.FromString,
                    response_serializer=dfs__pb2.ChunkList.SerializeToString,
            ),
            'DeleteFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFile,
                    request_deserializer=dfs__pb2.String.FromString,
                    response_serializer=dfs__pb2.String.SerializeToString,
            ),
            'GetPeers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeers,
                    request_deserializer=dfs__pb2.Number.FromString,
                    response_serializer=dfs__pb2.StringList.SerializeToString,
            ),
            'NameSpace': grpc.unary_unary_rpc_method_handler(
                    servicer.NameSpace,
                    request_deserializer=dfs__pb2.NameRequest.FromString,
                    response_serializer=dfs__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dfs.MasterServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MasterServer(object):
    """master server
    """

    @staticmethod
    def RegisterPeer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.MasterServer/RegisterPeer',
            dfs__pb2.RegisterRequest.SerializeToString,
            dfs__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckChunks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.MasterServer/CheckChunks',
            dfs__pb2.Empty.SerializeToString,
            dfs__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.MasterServer/GetFile',
            dfs__pb2.String.SerializeToString,
            dfs__pb2.ChunkList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.MasterServer/DeleteFile',
            dfs__pb2.String.SerializeToString,
            dfs__pb2.String.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPeers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.MasterServer/GetPeers',
            dfs__pb2.Number.SerializeToString,
            dfs__pb2.StringList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NameSpace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.MasterServer/NameSpace',
            dfs__pb2.NameRequest.SerializeToString,
            dfs__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
