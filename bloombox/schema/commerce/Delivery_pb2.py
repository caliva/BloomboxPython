# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: commerce/Delivery.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from geo import Address_pb2 as geo_dot_Address__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='commerce/Delivery.proto',
  package='commerce',
  syntax='proto3',
  serialized_pb=_b('\n\x17\x63ommerce/Delivery.proto\x12\x08\x63ommerce\x1a\x11geo/Address.proto\"J\n\x13\x44\x65liveryDestination\x12\x1d\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x0c.geo.Address\x12\x14\n\x0cinstructions\x18\x02 \x01(\tB3\n\x1bio.bloombox.schema.commerceB\rOrderDeliveryH\x01P\x00\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[geo_dot_Address__pb2.DESCRIPTOR,])




_DELIVERYDESTINATION = _descriptor.Descriptor(
  name='DeliveryDestination',
  full_name='commerce.DeliveryDestination',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='commerce.DeliveryDestination.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instructions', full_name='commerce.DeliveryDestination.instructions', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=130,
)

_DELIVERYDESTINATION.fields_by_name['address'].message_type = geo_dot_Address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name['DeliveryDestination'] = _DELIVERYDESTINATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeliveryDestination = _reflection.GeneratedProtocolMessageType('DeliveryDestination', (_message.Message,), dict(
  DESCRIPTOR = _DELIVERYDESTINATION,
  __module__ = 'commerce.Delivery_pb2'
  # @@protoc_insertion_point(class_scope:commerce.DeliveryDestination)
  ))
_sym_db.RegisterMessage(DeliveryDestination)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.bloombox.schema.commerceB\rOrderDeliveryH\001P\000\370\001\001'))
# @@protoc_insertion_point(module_scope)
