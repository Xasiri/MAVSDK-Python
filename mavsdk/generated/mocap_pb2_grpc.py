# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import mocap_pb2 as mocap__pb2


class MocapServiceStub(object):
    """*
    Motion Capture allow vehicles to navigate when a global
    position source is unavailable or unreliable
    (e.g. indoors, or when flying under a bridge. etc.).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetVisionPositionEstimate = channel.unary_unary(
                '/mavsdk.rpc.mocap.MocapService/SetVisionPositionEstimate',
                request_serializer=mocap__pb2.SetVisionPositionEstimateRequest.SerializeToString,
                response_deserializer=mocap__pb2.SetVisionPositionEstimateResponse.FromString,
                )
        self.SetAttitudePositionMocap = channel.unary_unary(
                '/mavsdk.rpc.mocap.MocapService/SetAttitudePositionMocap',
                request_serializer=mocap__pb2.SetAttitudePositionMocapRequest.SerializeToString,
                response_deserializer=mocap__pb2.SetAttitudePositionMocapResponse.FromString,
                )
        self.SetOdometry = channel.unary_unary(
                '/mavsdk.rpc.mocap.MocapService/SetOdometry',
                request_serializer=mocap__pb2.SetOdometryRequest.SerializeToString,
                response_deserializer=mocap__pb2.SetOdometryResponse.FromString,
                )


class MocapServiceServicer(object):
    """*
    Motion Capture allow vehicles to navigate when a global
    position source is unavailable or unreliable
    (e.g. indoors, or when flying under a bridge. etc.).
    """

    def SetVisionPositionEstimate(self, request, context):
        """Send Global position/attitude estimate from a vision source.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttitudePositionMocap(self, request, context):
        """Send motion capture attitude and position.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetOdometry(self, request, context):
        """Send odometry information with an external interface.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MocapServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetVisionPositionEstimate': grpc.unary_unary_rpc_method_handler(
                    servicer.SetVisionPositionEstimate,
                    request_deserializer=mocap__pb2.SetVisionPositionEstimateRequest.FromString,
                    response_serializer=mocap__pb2.SetVisionPositionEstimateResponse.SerializeToString,
            ),
            'SetAttitudePositionMocap': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttitudePositionMocap,
                    request_deserializer=mocap__pb2.SetAttitudePositionMocapRequest.FromString,
                    response_serializer=mocap__pb2.SetAttitudePositionMocapResponse.SerializeToString,
            ),
            'SetOdometry': grpc.unary_unary_rpc_method_handler(
                    servicer.SetOdometry,
                    request_deserializer=mocap__pb2.SetOdometryRequest.FromString,
                    response_serializer=mocap__pb2.SetOdometryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.mocap.MocapService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MocapService(object):
    """*
    Motion Capture allow vehicles to navigate when a global
    position source is unavailable or unreliable
    (e.g. indoors, or when flying under a bridge. etc.).
    """

    @staticmethod
    def SetVisionPositionEstimate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.mocap.MocapService/SetVisionPositionEstimate',
            mocap__pb2.SetVisionPositionEstimateRequest.SerializeToString,
            mocap__pb2.SetVisionPositionEstimateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttitudePositionMocap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.mocap.MocapService/SetAttitudePositionMocap',
            mocap__pb2.SetAttitudePositionMocapRequest.SerializeToString,
            mocap__pb2.SetAttitudePositionMocapResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetOdometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.mocap.MocapService/SetOdometry',
            mocap__pb2.SetOdometryRequest.SerializeToString,
            mocap__pb2.SetOdometryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
