# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/ProductType.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import ProductKind_pb2 as base_dot_ProductKind__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='base/ProductType.proto',
  package='base',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x62\x61se/ProductType.proto\x12\x04\x62\x61se\x1a\x16\x62\x61se/ProductKind.proto\".\n\x0bProductType\x12\x1f\n\x04kind\x18\x01 \x01(\x0e\x32\x11.base.ProductKindB1\n\x17io.bloombox.schema.baseB\x0f\x42\x61seProductTypeH\x01P\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[base_dot_ProductKind__pb2.DESCRIPTOR,])




_PRODUCTTYPE = _descriptor.Descriptor(
  name='ProductType',
  full_name='base.ProductType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='base.ProductType.kind', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=102,
)

_PRODUCTTYPE.fields_by_name['kind'].enum_type = base_dot_ProductKind__pb2._PRODUCTKIND
DESCRIPTOR.message_types_by_name['ProductType'] = _PRODUCTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProductType = _reflection.GeneratedProtocolMessageType('ProductType', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTTYPE,
  __module__ = 'base.ProductType_pb2'
  # @@protoc_insertion_point(class_scope:base.ProductType)
  ))
_sym_db.RegisterMessage(ProductType)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027io.bloombox.schema.baseB\017BaseProductTypeH\001P\001\370\001\001'))
# @@protoc_insertion_point(module_scope)
