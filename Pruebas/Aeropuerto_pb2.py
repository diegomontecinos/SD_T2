# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Aeropuerto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Aeropuerto.proto',
  package='Aeropuerto',
  syntax='proto3',
  serialized_options=_b('\n\033io.grpc.examples.AeropuertoB\017AeropuertoProtoP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x10\x41\x65ropuerto.proto\x12\nAeropuerto\"\x19\n\x07mensaje\x12\x0e\n\x06\x61ltura\x18\x01 \x01(\x05\"\x19\n\trespuesta\x12\x0c\n\x04\x66lag\x18\x01 \x01(\t2G\n\x06Prueba\x12=\n\renviar_altura\x12\x13.Aeropuerto.mensaje\x1a\x15.Aeropuerto.respuesta\"\x00\x42\x36\n\x1bio.grpc.examples.AeropuertoB\x0f\x41\x65ropuertoProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_MENSAJE = _descriptor.Descriptor(
  name='mensaje',
  full_name='Aeropuerto.mensaje',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='altura', full_name='Aeropuerto.mensaje.altura', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=57,
)


_RESPUESTA = _descriptor.Descriptor(
  name='respuesta',
  full_name='Aeropuerto.respuesta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='Aeropuerto.respuesta.flag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['mensaje'] = _MENSAJE
DESCRIPTOR.message_types_by_name['respuesta'] = _RESPUESTA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

mensaje = _reflection.GeneratedProtocolMessageType('mensaje', (_message.Message,), dict(
  DESCRIPTOR = _MENSAJE,
  __module__ = 'Aeropuerto_pb2'
  # @@protoc_insertion_point(class_scope:Aeropuerto.mensaje)
  ))
_sym_db.RegisterMessage(mensaje)

respuesta = _reflection.GeneratedProtocolMessageType('respuesta', (_message.Message,), dict(
  DESCRIPTOR = _RESPUESTA,
  __module__ = 'Aeropuerto_pb2'
  # @@protoc_insertion_point(class_scope:Aeropuerto.respuesta)
  ))
_sym_db.RegisterMessage(respuesta)


DESCRIPTOR._options = None

_PRUEBA = _descriptor.ServiceDescriptor(
  name='Prueba',
  full_name='Aeropuerto.Prueba',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=86,
  serialized_end=157,
  methods=[
  _descriptor.MethodDescriptor(
    name='enviar_altura',
    full_name='Aeropuerto.Prueba.enviar_altura',
    index=0,
    containing_service=None,
    input_type=_MENSAJE,
    output_type=_RESPUESTA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRUEBA)

DESCRIPTOR.services_by_name['Prueba'] = _PRUEBA

# @@protoc_insertion_point(module_scope)
