# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/ProductKind.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='base/ProductKind.proto',
  package='base',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x62\x61se/ProductKind.proto\x12\x04\x62\x61se*\x80\x01\n\x0bProductKind\x12\x0b\n\x07\x46LOWERS\x10\x00\x12\x0b\n\x07\x45\x44IBLES\x10\x01\x12\x0c\n\x08\x45XTRACTS\x10\x02\x12\x0c\n\x08PREROLLS\x10\x03\x12\x0e\n\nAPOTHECARY\x10\x04\x12\x0e\n\nCARTRIDGES\x10\x05\x12\n\n\x06PLANTS\x10\x06\x12\x0f\n\x0bMERCHANDISE\x10\x07\x42\x31\n\x17io.bloombox.schema.baseB\x0f\x42\x61seProductKindH\x01P\x01\xf8\x01\x01\x62\x06proto3')
)

_PRODUCTKIND = _descriptor.EnumDescriptor(
  name='ProductKind',
  full_name='base.ProductKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLOWERS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EDIBLES', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTRACTS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREROLLS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APOTHECARY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARTRIDGES', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLANTS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MERCHANDISE', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=33,
  serialized_end=161,
)
_sym_db.RegisterEnumDescriptor(_PRODUCTKIND)

ProductKind = enum_type_wrapper.EnumTypeWrapper(_PRODUCTKIND)
FLOWERS = 0
EDIBLES = 1
EXTRACTS = 2
PREROLLS = 3
APOTHECARY = 4
CARTRIDGES = 5
PLANTS = 6
MERCHANDISE = 7


DESCRIPTOR.enum_types_by_name['ProductKind'] = _PRODUCTKIND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027io.bloombox.schema.baseB\017BaseProductKindH\001P\001\370\001\001'))
# @@protoc_insertion_point(module_scope)
