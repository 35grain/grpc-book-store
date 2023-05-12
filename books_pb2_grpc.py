# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import books_pb2 as books__pb2


class BookStoreStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateBook = channel.unary_unary(
                '/BookStore/UpdateBook',
                request_serializer=books__pb2.UpdateBookRequest.SerializeToString,
                response_deserializer=books__pb2.UpdateBookResponse.FromString,
                )
        self.CreateStorePS = channel.unary_unary(
                '/BookStore/CreateStorePS',
                request_serializer=books__pb2.CreateStorePSRequest.SerializeToString,
                response_deserializer=books__pb2.CreateStorePSResponse.FromString,
                )
        self.CreateChain = channel.unary_unary(
                '/BookStore/CreateChain',
                request_serializer=books__pb2.CreateChainRequest.SerializeToString,
                response_deserializer=books__pb2.CreateChainResponse.FromString,
                )
        self.GetProcesses = channel.unary_unary(
                '/BookStore/GetProcesses',
                request_serializer=books__pb2.GetProcessesRequest.SerializeToString,
                response_deserializer=books__pb2.GetProcessesResponse.FromString,
                )
        self.ListChain = channel.unary_unary(
                '/BookStore/ListChain',
                request_serializer=books__pb2.ListChainRequest.SerializeToString,
                response_deserializer=books__pb2.ListChainResponse.FromString,
                )
        self.ListBooks = channel.unary_unary(
                '/BookStore/ListBooks',
                request_serializer=books__pb2.ListBooksRequest.SerializeToString,
                response_deserializer=books__pb2.ListBooksResponse.FromString,
                )
        self.PropagateChain = channel.unary_unary(
                '/BookStore/PropagateChain',
                request_serializer=books__pb2.PropagateChainRequest.SerializeToString,
                response_deserializer=books__pb2.PropagateChainResponse.FromString,
                )
        self.WriteOperation = channel.unary_unary(
                '/BookStore/WriteOperation',
                request_serializer=books__pb2.WriteOperationRequest.SerializeToString,
                response_deserializer=books__pb2.WriteOperationResponse.FromString,
                )
        self.ReadOperation = channel.unary_unary(
                '/BookStore/ReadOperation',
                request_serializer=books__pb2.ReadOperationRequest.SerializeToString,
                response_deserializer=books__pb2.ReadOperationResponse.FromString,
                )
        self.DataStatus = channel.unary_unary(
                '/BookStore/DataStatus',
                request_serializer=books__pb2.DataStatusRequest.SerializeToString,
                response_deserializer=books__pb2.DataStatusResponse.FromString,
                )
        self.RemoveHead = channel.unary_unary(
                '/BookStore/RemoveHead',
                request_serializer=books__pb2.RemoveHeadRequest.SerializeToString,
                response_deserializer=books__pb2.RemoveHeadResponse.FromString,
                )
        self.RestoreHead = channel.unary_unary(
                '/BookStore/RestoreHead',
                request_serializer=books__pb2.RestoreHeadRequest.SerializeToString,
                response_deserializer=books__pb2.RestoreHeadResponse.FromString,
                )
        self.SetTimeout = channel.unary_unary(
                '/BookStore/SetTimeout',
                request_serializer=books__pb2.SetTimeoutRequest.SerializeToString,
                response_deserializer=books__pb2.SetTimeoutResponse.FromString,
                )
        self.PropagateTimeout = channel.unary_unary(
                '/BookStore/PropagateTimeout',
                request_serializer=books__pb2.SetTimeoutRequest.SerializeToString,
                response_deserializer=books__pb2.PropagateTimeoutResponse.FromString,
                )
        self.SetClean = channel.unary_unary(
                '/BookStore/SetClean',
                request_serializer=books__pb2.SetCleanRequest.SerializeToString,
                response_deserializer=books__pb2.SetCleanResponse.FromString,
                )


class BookStoreServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpdateBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateStorePS(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateChain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProcesses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListChain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBooks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PropagateChain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteOperation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadOperation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DataStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveHead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RestoreHead(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTimeout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PropagateTimeout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetClean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBook,
                    request_deserializer=books__pb2.UpdateBookRequest.FromString,
                    response_serializer=books__pb2.UpdateBookResponse.SerializeToString,
            ),
            'CreateStorePS': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStorePS,
                    request_deserializer=books__pb2.CreateStorePSRequest.FromString,
                    response_serializer=books__pb2.CreateStorePSResponse.SerializeToString,
            ),
            'CreateChain': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateChain,
                    request_deserializer=books__pb2.CreateChainRequest.FromString,
                    response_serializer=books__pb2.CreateChainResponse.SerializeToString,
            ),
            'GetProcesses': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProcesses,
                    request_deserializer=books__pb2.GetProcessesRequest.FromString,
                    response_serializer=books__pb2.GetProcessesResponse.SerializeToString,
            ),
            'ListChain': grpc.unary_unary_rpc_method_handler(
                    servicer.ListChain,
                    request_deserializer=books__pb2.ListChainRequest.FromString,
                    response_serializer=books__pb2.ListChainResponse.SerializeToString,
            ),
            'ListBooks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBooks,
                    request_deserializer=books__pb2.ListBooksRequest.FromString,
                    response_serializer=books__pb2.ListBooksResponse.SerializeToString,
            ),
            'PropagateChain': grpc.unary_unary_rpc_method_handler(
                    servicer.PropagateChain,
                    request_deserializer=books__pb2.PropagateChainRequest.FromString,
                    response_serializer=books__pb2.PropagateChainResponse.SerializeToString,
            ),
            'WriteOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteOperation,
                    request_deserializer=books__pb2.WriteOperationRequest.FromString,
                    response_serializer=books__pb2.WriteOperationResponse.SerializeToString,
            ),
            'ReadOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadOperation,
                    request_deserializer=books__pb2.ReadOperationRequest.FromString,
                    response_serializer=books__pb2.ReadOperationResponse.SerializeToString,
            ),
            'DataStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.DataStatus,
                    request_deserializer=books__pb2.DataStatusRequest.FromString,
                    response_serializer=books__pb2.DataStatusResponse.SerializeToString,
            ),
            'RemoveHead': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveHead,
                    request_deserializer=books__pb2.RemoveHeadRequest.FromString,
                    response_serializer=books__pb2.RemoveHeadResponse.SerializeToString,
            ),
            'RestoreHead': grpc.unary_unary_rpc_method_handler(
                    servicer.RestoreHead,
                    request_deserializer=books__pb2.RestoreHeadRequest.FromString,
                    response_serializer=books__pb2.RestoreHeadResponse.SerializeToString,
            ),
            'SetTimeout': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTimeout,
                    request_deserializer=books__pb2.SetTimeoutRequest.FromString,
                    response_serializer=books__pb2.SetTimeoutResponse.SerializeToString,
            ),
            'PropagateTimeout': grpc.unary_unary_rpc_method_handler(
                    servicer.PropagateTimeout,
                    request_deserializer=books__pb2.SetTimeoutRequest.FromString,
                    response_serializer=books__pb2.PropagateTimeoutResponse.SerializeToString,
            ),
            'SetClean': grpc.unary_unary_rpc_method_handler(
                    servicer.SetClean,
                    request_deserializer=books__pb2.SetCleanRequest.FromString,
                    response_serializer=books__pb2.SetCleanResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BookStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookStore(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpdateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/UpdateBook',
            books__pb2.UpdateBookRequest.SerializeToString,
            books__pb2.UpdateBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateStorePS(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/CreateStorePS',
            books__pb2.CreateStorePSRequest.SerializeToString,
            books__pb2.CreateStorePSResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateChain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/CreateChain',
            books__pb2.CreateChainRequest.SerializeToString,
            books__pb2.CreateChainResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProcesses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/GetProcesses',
            books__pb2.GetProcessesRequest.SerializeToString,
            books__pb2.GetProcessesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListChain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/ListChain',
            books__pb2.ListChainRequest.SerializeToString,
            books__pb2.ListChainResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBooks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/ListBooks',
            books__pb2.ListBooksRequest.SerializeToString,
            books__pb2.ListBooksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PropagateChain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/PropagateChain',
            books__pb2.PropagateChainRequest.SerializeToString,
            books__pb2.PropagateChainResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/WriteOperation',
            books__pb2.WriteOperationRequest.SerializeToString,
            books__pb2.WriteOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/ReadOperation',
            books__pb2.ReadOperationRequest.SerializeToString,
            books__pb2.ReadOperationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DataStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/DataStatus',
            books__pb2.DataStatusRequest.SerializeToString,
            books__pb2.DataStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveHead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/RemoveHead',
            books__pb2.RemoveHeadRequest.SerializeToString,
            books__pb2.RemoveHeadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RestoreHead(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/RestoreHead',
            books__pb2.RestoreHeadRequest.SerializeToString,
            books__pb2.RestoreHeadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetTimeout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/SetTimeout',
            books__pb2.SetTimeoutRequest.SerializeToString,
            books__pb2.SetTimeoutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PropagateTimeout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/PropagateTimeout',
            books__pb2.SetTimeoutRequest.SerializeToString,
            books__pb2.PropagateTimeoutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetClean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookStore/SetClean',
            books__pb2.SetCleanRequest.SerializeToString,
            books__pb2.SetCleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
