# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from checkin.v1beta1 import CheckinService_Beta1_pb2 as checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2


class CheckinStub(object):
  """Specifies the checkin service, which accepts opaque identification information for the purpose of checking users in
  to a physical brick-and-mortar retail location.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/services.checkin.v1beta1.Checkin/Ping',
        request_serializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.Ping.Request.SerializeToString,
        response_deserializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.Ping.Response.FromString,
        )
    self.Identification = channel.unary_unary(
        '/services.checkin.v1beta1.Checkin/Identification',
        request_serializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.IDCheckin.Request.SerializeToString,
        response_deserializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.CheckinResponse.FromString,
        )
    self.Card = channel.unary_unary(
        '/services.checkin.v1beta1.Checkin/Card',
        request_serializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.CardCheckin.Request.SerializeToString,
        response_deserializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.CheckinResponse.FromString,
        )


class CheckinServicer(object):
  """Specifies the checkin service, which accepts opaque identification information for the purpose of checking users in
  to a physical brick-and-mortar retail location.
  """

  def Ping(self, request, context):
    """Ping the checkin server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Identification(self, request, context):
    """Specifies an operation to check a user in via their government ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Card(self, request, context):
    """Specifies an operation to check a user in via their government ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CheckinServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.Ping.Request.FromString,
          response_serializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.Ping.Response.SerializeToString,
      ),
      'Identification': grpc.unary_unary_rpc_method_handler(
          servicer.Identification,
          request_deserializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.IDCheckin.Request.FromString,
          response_serializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.CheckinResponse.SerializeToString,
      ),
      'Card': grpc.unary_unary_rpc_method_handler(
          servicer.Card,
          request_deserializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.CardCheckin.Request.FromString,
          response_serializer=checkin_dot_v1beta1_dot_CheckinService__Beta1__pb2.CheckinResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'services.checkin.v1beta1.Checkin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
