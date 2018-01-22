# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: products/Edible.proto

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


from base import ProductKey_pb2 as base_dot_ProductKey__pb2
from content import MaterialsData_pb2 as content_dot_MaterialsData__pb2
from content import ProductContent_pb2 as content_dot_ProductContent__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='products/Edible.proto',
  package='products',
  syntax='proto3',
  serialized_pb=_b('\n\x15products/Edible.proto\x12\x08products\x1a\x15\x62\x61se/ProductKey.proto\x1a\x1b\x63ontent/MaterialsData.proto\x1a\x1c\x63ontent/ProductContent.proto\"1\n\x10\x45\x64ibleIngredient\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\t\"\xf5\x01\n\x06\x45\x64ible\x12\x1d\n\x03key\x18\x01 \x01(\x0b\x32\x10.base.ProductKey\x12\"\n\x04type\x18\x02 \x01(\x0e\x32\x14.products.EdibleType\x12#\n\x05\x66lags\x18\x03 \x03(\x0e\x32\x14.products.EdibleFlag\x12(\n\x07product\x18\x04 \x01(\x0b\x32\x17.content.ProductContent\x12(\n\x08material\x18\x05 \x01(\x0b\x32\x16.content.MaterialsData\x12/\n\x0bingredients\x18\x06 \x03(\x0b\x32\x1a.products.EdibleIngredient*Y\n\nEdibleType\x12\x16\n\x12UNSPECIFIED_EDIBLE\x10\x00\x12\r\n\tCHOCOLATE\x10\x01\x12\x0e\n\nBAKED_GOOD\x10\x02\x12\t\n\x05\x43\x41NDY\x10\x03\x12\t\n\x05\x44RINK\x10\x04*t\n\nEdibleFlag\x12\x12\n\x0eNO_EDIBLE_FLAG\x10\x00\x12\t\n\x05VEGAN\x10\x01\x12\x0f\n\x0bGLUTEN_FREE\x10\x02\x12\x0e\n\nSUGAR_FREE\x10\x03\x12\x0e\n\nFAIR_TRADE\x10\x04\x12\x0b\n\x07ORGANIC\x10\x05\x12\t\n\x05LOCAL\x10\x06\x42\x32\n\x1aio.bloombox.schema.productB\rEdibleProductH\x01P\x00\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[base_dot_ProductKey__pb2.DESCRIPTOR,content_dot_MaterialsData__pb2.DESCRIPTOR,content_dot_ProductContent__pb2.DESCRIPTOR,])

_EDIBLETYPE = _descriptor.EnumDescriptor(
  name='EdibleType',
  full_name='products.EdibleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_EDIBLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHOCOLATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAKED_GOOD', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANDY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRINK', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=416,
  serialized_end=505,
)
_sym_db.RegisterEnumDescriptor(_EDIBLETYPE)

EdibleType = enum_type_wrapper.EnumTypeWrapper(_EDIBLETYPE)
_EDIBLEFLAG = _descriptor.EnumDescriptor(
  name='EdibleFlag',
  full_name='products.EdibleFlag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_EDIBLE_FLAG', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VEGAN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLUTEN_FREE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUGAR_FREE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIR_TRADE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORGANIC', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=507,
  serialized_end=623,
)
_sym_db.RegisterEnumDescriptor(_EDIBLEFLAG)

EdibleFlag = enum_type_wrapper.EnumTypeWrapper(_EDIBLEFLAG)
UNSPECIFIED_EDIBLE = 0
CHOCOLATE = 1
BAKED_GOOD = 2
CANDY = 3
DRINK = 4
NO_EDIBLE_FLAG = 0
VEGAN = 1
GLUTEN_FREE = 2
SUGAR_FREE = 3
FAIR_TRADE = 4
ORGANIC = 5
LOCAL = 6



_EDIBLEINGREDIENT = _descriptor.Descriptor(
  name='EdibleIngredient',
  full_name='products.EdibleIngredient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='products.EdibleIngredient.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='products.EdibleIngredient.amount', index=1,
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
  serialized_start=117,
  serialized_end=166,
)


_EDIBLE = _descriptor.Descriptor(
  name='Edible',
  full_name='products.Edible',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='products.Edible.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='products.Edible.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='products.Edible.flags', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product', full_name='products.Edible.product', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='material', full_name='products.Edible.material', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ingredients', full_name='products.Edible.ingredients', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=169,
  serialized_end=414,
)

_EDIBLE.fields_by_name['key'].message_type = base_dot_ProductKey__pb2._PRODUCTKEY
_EDIBLE.fields_by_name['type'].enum_type = _EDIBLETYPE
_EDIBLE.fields_by_name['flags'].enum_type = _EDIBLEFLAG
_EDIBLE.fields_by_name['product'].message_type = content_dot_ProductContent__pb2._PRODUCTCONTENT
_EDIBLE.fields_by_name['material'].message_type = content_dot_MaterialsData__pb2._MATERIALSDATA
_EDIBLE.fields_by_name['ingredients'].message_type = _EDIBLEINGREDIENT
DESCRIPTOR.message_types_by_name['EdibleIngredient'] = _EDIBLEINGREDIENT
DESCRIPTOR.message_types_by_name['Edible'] = _EDIBLE
DESCRIPTOR.enum_types_by_name['EdibleType'] = _EDIBLETYPE
DESCRIPTOR.enum_types_by_name['EdibleFlag'] = _EDIBLEFLAG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EdibleIngredient = _reflection.GeneratedProtocolMessageType('EdibleIngredient', (_message.Message,), dict(
  DESCRIPTOR = _EDIBLEINGREDIENT,
  __module__ = 'products.Edible_pb2'
  # @@protoc_insertion_point(class_scope:products.EdibleIngredient)
  ))
_sym_db.RegisterMessage(EdibleIngredient)

Edible = _reflection.GeneratedProtocolMessageType('Edible', (_message.Message,), dict(
  DESCRIPTOR = _EDIBLE,
  __module__ = 'products.Edible_pb2'
  # @@protoc_insertion_point(class_scope:products.Edible)
  ))
_sym_db.RegisterMessage(Edible)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032io.bloombox.schema.productB\rEdibleProductH\001P\000\370\001\001'))
# @@protoc_insertion_point(module_scope)