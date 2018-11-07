# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Torre.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Torre.proto',
  package='Aeropuerto',
  syntax='proto3',
  serialized_options=_b('\n\033io.grpc.examples.AeropuertoB\017AeropuertoProtoP\001\242\002\003HLW'),
  serialized_pb=_b('\n\x0bTorre.proto\x12\nAeropuerto\"3\n\tPista_Des\x12\x10\n\x08Id_avion\x18\x01 \x01(\t\x12\x14\n\x0cName_destino\x18\x02 \x01(\t\"\xb6\x01\n\x08Resp_Des\x12\x1d\n\x15\x41utorizacion_despegue\x18\x01 \x01(\x08\x12\x16\n\x0ePista_despegue\x18\x02 \x01(\t\x12\x17\n\x0f\x41ltura_despegue\x18\x03 \x01(\x05\x12\x19\n\x11Posicion_despegue\x18\x04 \x01(\x05\x12\x19\n\x11\x41nterior_despegue\x18\x05 \x01(\t\x12\x12\n\nIp_destino\x18\x06 \x01(\t\x12\x10\n\x08Id_avion\x18\x07 \x01(\t\"\x1c\n\x08Pista_At\x12\x10\n\x08Id_avion\x18\x01 \x01(\t\"\xab\x01\n\x07Resp_At\x12\x1f\n\x17\x41utorizacion_aterrizaje\x18\x01 \x01(\x08\x12\x18\n\x10Pista_aterrizaje\x18\x02 \x01(\x05\x12\x19\n\x11\x41ltura_aterrizaje\x18\x03 \x01(\x05\x12\x1b\n\x13Posicion_aterrizaje\x18\x04 \x01(\x05\x12\x1b\n\x13\x41nterior_aterrizaje\x18\x05 \x01(\t\x12\x10\n\x08Id_avion\x18\x06 \x01(\t2L\n\x08\x44\x65spegue\x12@\n\x0f\x65nviar_despegue\x12\x15.Aeropuerto.Pista_Des\x1a\x14.Aeropuerto.Resp_Des\"\x00\x32N\n\nAterrizaje\x12@\n\x11\x65nviar_aterrizaje\x12\x14.Aeropuerto.Pista_At\x1a\x13.Aeropuerto.Resp_At\"\x00\x42\x36\n\x1bio.grpc.examples.AeropuertoB\x0f\x41\x65ropuertoProtoP\x01\xa2\x02\x03HLWb\x06proto3')
)




_PISTA_DES = _descriptor.Descriptor(
  name='Pista_Des',
  full_name='Aeropuerto.Pista_Des',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id_avion', full_name='Aeropuerto.Pista_Des.Id_avion', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Name_destino', full_name='Aeropuerto.Pista_Des.Name_destino', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=27,
  serialized_end=78,
)


_RESP_DES = _descriptor.Descriptor(
  name='Resp_Des',
  full_name='Aeropuerto.Resp_Des',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Autorizacion_despegue', full_name='Aeropuerto.Resp_Des.Autorizacion_despegue', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Pista_despegue', full_name='Aeropuerto.Resp_Des.Pista_despegue', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Altura_despegue', full_name='Aeropuerto.Resp_Des.Altura_despegue', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Posicion_despegue', full_name='Aeropuerto.Resp_Des.Posicion_despegue', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Anterior_despegue', full_name='Aeropuerto.Resp_Des.Anterior_despegue', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Ip_destino', full_name='Aeropuerto.Resp_Des.Ip_destino', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Id_avion', full_name='Aeropuerto.Resp_Des.Id_avion', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=81,
  serialized_end=263,
)


_PISTA_AT = _descriptor.Descriptor(
  name='Pista_At',
  full_name='Aeropuerto.Pista_At',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id_avion', full_name='Aeropuerto.Pista_At.Id_avion', index=0,
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
  serialized_start=265,
  serialized_end=293,
)


_RESP_AT = _descriptor.Descriptor(
  name='Resp_At',
  full_name='Aeropuerto.Resp_At',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Autorizacion_aterrizaje', full_name='Aeropuerto.Resp_At.Autorizacion_aterrizaje', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Pista_aterrizaje', full_name='Aeropuerto.Resp_At.Pista_aterrizaje', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Altura_aterrizaje', full_name='Aeropuerto.Resp_At.Altura_aterrizaje', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Posicion_aterrizaje', full_name='Aeropuerto.Resp_At.Posicion_aterrizaje', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Anterior_aterrizaje', full_name='Aeropuerto.Resp_At.Anterior_aterrizaje', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Id_avion', full_name='Aeropuerto.Resp_At.Id_avion', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=296,
  serialized_end=467,
)

DESCRIPTOR.message_types_by_name['Pista_Des'] = _PISTA_DES
DESCRIPTOR.message_types_by_name['Resp_Des'] = _RESP_DES
DESCRIPTOR.message_types_by_name['Pista_At'] = _PISTA_AT
DESCRIPTOR.message_types_by_name['Resp_At'] = _RESP_AT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pista_Des = _reflection.GeneratedProtocolMessageType('Pista_Des', (_message.Message,), dict(
  DESCRIPTOR = _PISTA_DES,
  __module__ = 'Torre_pb2'
  # @@protoc_insertion_point(class_scope:Aeropuerto.Pista_Des)
  ))
_sym_db.RegisterMessage(Pista_Des)

Resp_Des = _reflection.GeneratedProtocolMessageType('Resp_Des', (_message.Message,), dict(
  DESCRIPTOR = _RESP_DES,
  __module__ = 'Torre_pb2'
  # @@protoc_insertion_point(class_scope:Aeropuerto.Resp_Des)
  ))
_sym_db.RegisterMessage(Resp_Des)

Pista_At = _reflection.GeneratedProtocolMessageType('Pista_At', (_message.Message,), dict(
  DESCRIPTOR = _PISTA_AT,
  __module__ = 'Torre_pb2'
  # @@protoc_insertion_point(class_scope:Aeropuerto.Pista_At)
  ))
_sym_db.RegisterMessage(Pista_At)

Resp_At = _reflection.GeneratedProtocolMessageType('Resp_At', (_message.Message,), dict(
  DESCRIPTOR = _RESP_AT,
  __module__ = 'Torre_pb2'
  # @@protoc_insertion_point(class_scope:Aeropuerto.Resp_At)
  ))
_sym_db.RegisterMessage(Resp_At)


DESCRIPTOR._options = None

_DESPEGUE = _descriptor.ServiceDescriptor(
  name='Despegue',
  full_name='Aeropuerto.Despegue',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=469,
  serialized_end=545,
  methods=[
  _descriptor.MethodDescriptor(
    name='enviar_despegue',
    full_name='Aeropuerto.Despegue.enviar_despegue',
    index=0,
    containing_service=None,
    input_type=_PISTA_DES,
    output_type=_RESP_DES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DESPEGUE)

DESCRIPTOR.services_by_name['Despegue'] = _DESPEGUE


_ATERRIZAJE = _descriptor.ServiceDescriptor(
  name='Aterrizaje',
  full_name='Aeropuerto.Aterrizaje',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=547,
  serialized_end=625,
  methods=[
  _descriptor.MethodDescriptor(
    name='enviar_aterrizaje',
    full_name='Aeropuerto.Aterrizaje.enviar_aterrizaje',
    index=0,
    containing_service=None,
    input_type=_PISTA_AT,
    output_type=_RESP_AT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ATERRIZAJE)

DESCRIPTOR.services_by_name['Aterrizaje'] = _ATERRIZAJE

# @@protoc_insertion_point(module_scope)
