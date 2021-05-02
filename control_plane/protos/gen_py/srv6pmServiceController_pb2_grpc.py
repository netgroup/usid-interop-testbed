# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import srv6pmServiceController_pb2 as srv6pmServiceController__pb2


class SRv6PMControllerStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMeasurementData = channel.unary_unary(
                '/srv6pm.SRv6PMController/SendMeasurementData',
                request_serializer=srv6pmServiceController__pb2.SendMeasurementDataRequest.SerializeToString,
                response_deserializer=srv6pmServiceController__pb2.SendMeasurementDataResponse.FromString,
                )
        self.SendIperfData = channel.unary_unary(
                '/srv6pm.SRv6PMController/SendIperfData',
                request_serializer=srv6pmServiceController__pb2.SendIperfDataRequest.SerializeToString,
                response_deserializer=srv6pmServiceController__pb2.SendIperfDataResponse.FromString,
                )


class SRv6PMControllerServicer(object):
    """Missing associated documentation comment in .proto file"""

    def SendMeasurementData(self, request, context):
        """send data of an experiment
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendIperfData(self, request, context):
        """send Iperf data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SRv6PMControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMeasurementData': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMeasurementData,
                    request_deserializer=srv6pmServiceController__pb2.SendMeasurementDataRequest.FromString,
                    response_serializer=srv6pmServiceController__pb2.SendMeasurementDataResponse.SerializeToString,
            ),
            'SendIperfData': grpc.unary_unary_rpc_method_handler(
                    servicer.SendIperfData,
                    request_deserializer=srv6pmServiceController__pb2.SendIperfDataRequest.FromString,
                    response_serializer=srv6pmServiceController__pb2.SendIperfDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'srv6pm.SRv6PMController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SRv6PMController(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def SendMeasurementData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/srv6pm.SRv6PMController/SendMeasurementData',
            srv6pmServiceController__pb2.SendMeasurementDataRequest.SerializeToString,
            srv6pmServiceController__pb2.SendMeasurementDataResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendIperfData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/srv6pm.SRv6PMController/SendIperfData',
            srv6pmServiceController__pb2.SendIperfDataRequest.SerializeToString,
            srv6pmServiceController__pb2.SendIperfDataResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)