# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Torre_pb2 as Torre__pb2


class Serv_AeropuertoStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.enviar_despegue = channel.unary_unary(
        '/Aeropuerto.Serv_Aeropuerto/enviar_despegue',
        request_serializer=Torre__pb2.Pista_Des.SerializeToString,
        response_deserializer=Torre__pb2.Resp_Des.FromString,
        )
    self.confirmar_despegue = channel.unary_unary(
        '/Aeropuerto.Serv_Aeropuerto/confirmar_despegue',
        request_serializer=Torre__pb2.Cons_Des.SerializeToString,
        response_deserializer=Torre__pb2.Resp_Cons.FromString,
        )
    self.enviar_aterrizaje = channel.unary_unary(
        '/Aeropuerto.Serv_Aeropuerto/enviar_aterrizaje',
        request_serializer=Torre__pb2.Pista_At.SerializeToString,
        response_deserializer=Torre__pb2.Resp_At.FromString,
        )
    self.enviar_info = channel.unary_unary(
        '/Aeropuerto.Serv_Aeropuerto/enviar_info',
        request_serializer=Torre__pb2.Id_Pantalla.SerializeToString,
        response_deserializer=Torre__pb2.Resp_Pantalla.FromString,
        )


class Serv_AeropuertoServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def enviar_despegue(self, request, context):
    """solicitud de despegue
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def confirmar_despegue(self, request, context):
    """
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def enviar_aterrizaje(self, request, context):
    """asignacion pista de aterrizaje
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def enviar_info(self, request, context):
    """Enviar info pantallas
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_Serv_AeropuertoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'enviar_despegue': grpc.unary_unary_rpc_method_handler(
          servicer.enviar_despegue,
          request_deserializer=Torre__pb2.Pista_Des.FromString,
          response_serializer=Torre__pb2.Resp_Des.SerializeToString,
      ),
      'confirmar_despegue': grpc.unary_unary_rpc_method_handler(
          servicer.confirmar_despegue,
          request_deserializer=Torre__pb2.Cons_Des.FromString,
          response_serializer=Torre__pb2.Resp_Cons.SerializeToString,
      ),
      'enviar_aterrizaje': grpc.unary_unary_rpc_method_handler(
          servicer.enviar_aterrizaje,
          request_deserializer=Torre__pb2.Pista_At.FromString,
          response_serializer=Torre__pb2.Resp_At.SerializeToString,
      ),
      'enviar_info': grpc.unary_unary_rpc_method_handler(
          servicer.enviar_info,
          request_deserializer=Torre__pb2.Id_Pantalla.FromString,
          response_serializer=Torre__pb2.Resp_Pantalla.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Aeropuerto.Serv_Aeropuerto', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
