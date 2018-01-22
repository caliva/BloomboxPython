# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: telemetry/v1beta2/commerce/ShopEvents_Beta2.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from analytics import Context_pb2 as analytics_dot_Context__pb2
from analytics.commerce import ShopAnalytics_pb2 as analytics_dot_commerce_dot_ShopAnalytics__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='telemetry/v1beta2/commerce/ShopEvents_Beta2.proto',
  package='services.telemetry.v1beta2',
  syntax='proto3',
  serialized_pb=_b('\n1telemetry/v1beta2/commerce/ShopEvents_Beta2.proto\x12\x1aservices.telemetry.v1beta2\x1a\x17\x61nalytics/Context.proto\x1a&analytics/commerce/ShopAnalytics.proto\"e\n\x0eShopImpression\x12#\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x12.analytics.Context\x12.\n\nimpression\x18\x02 \x01(\x0b\x32\x1a.analytics.shop.Impression\"S\n\x08ShopView\x12#\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x12.analytics.Context\x12\"\n\x04view\x18\x02 \x01(\x0b\x32\x14.analytics.shop.View\"Y\n\nShopAction\x12#\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x12.analytics.Context\x12&\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x16.analytics.shop.ActionBG\n-io.bloombox.schema.services.telemetry.v1beta2H\x01P\x01\xaa\x02\x11Telemetry.v1beta2b\x06proto3')
  ,
  dependencies=[analytics_dot_Context__pb2.DESCRIPTOR,analytics_dot_commerce_dot_ShopAnalytics__pb2.DESCRIPTOR,])




_SHOPIMPRESSION = _descriptor.Descriptor(
  name='ShopImpression',
  full_name='services.telemetry.v1beta2.ShopImpression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='services.telemetry.v1beta2.ShopImpression.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='impression', full_name='services.telemetry.v1beta2.ShopImpression.impression', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=146,
  serialized_end=247,
)


_SHOPVIEW = _descriptor.Descriptor(
  name='ShopView',
  full_name='services.telemetry.v1beta2.ShopView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='services.telemetry.v1beta2.ShopView.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view', full_name='services.telemetry.v1beta2.ShopView.view', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=249,
  serialized_end=332,
)


_SHOPACTION = _descriptor.Descriptor(
  name='ShopAction',
  full_name='services.telemetry.v1beta2.ShopAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='services.telemetry.v1beta2.ShopAction.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='services.telemetry.v1beta2.ShopAction.action', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=334,
  serialized_end=423,
)

_SHOPIMPRESSION.fields_by_name['context'].message_type = analytics_dot_Context__pb2._CONTEXT
_SHOPIMPRESSION.fields_by_name['impression'].message_type = analytics_dot_commerce_dot_ShopAnalytics__pb2._IMPRESSION
_SHOPVIEW.fields_by_name['context'].message_type = analytics_dot_Context__pb2._CONTEXT
_SHOPVIEW.fields_by_name['view'].message_type = analytics_dot_commerce_dot_ShopAnalytics__pb2._VIEW
_SHOPACTION.fields_by_name['context'].message_type = analytics_dot_Context__pb2._CONTEXT
_SHOPACTION.fields_by_name['action'].message_type = analytics_dot_commerce_dot_ShopAnalytics__pb2._ACTION
DESCRIPTOR.message_types_by_name['ShopImpression'] = _SHOPIMPRESSION
DESCRIPTOR.message_types_by_name['ShopView'] = _SHOPVIEW
DESCRIPTOR.message_types_by_name['ShopAction'] = _SHOPACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShopImpression = _reflection.GeneratedProtocolMessageType('ShopImpression', (_message.Message,), dict(
  DESCRIPTOR = _SHOPIMPRESSION,
  __module__ = 'telemetry.v1beta2.commerce.ShopEvents_Beta2_pb2'
  # @@protoc_insertion_point(class_scope:services.telemetry.v1beta2.ShopImpression)
  ))
_sym_db.RegisterMessage(ShopImpression)

ShopView = _reflection.GeneratedProtocolMessageType('ShopView', (_message.Message,), dict(
  DESCRIPTOR = _SHOPVIEW,
  __module__ = 'telemetry.v1beta2.commerce.ShopEvents_Beta2_pb2'
  # @@protoc_insertion_point(class_scope:services.telemetry.v1beta2.ShopView)
  ))
_sym_db.RegisterMessage(ShopView)

ShopAction = _reflection.GeneratedProtocolMessageType('ShopAction', (_message.Message,), dict(
  DESCRIPTOR = _SHOPACTION,
  __module__ = 'telemetry.v1beta2.commerce.ShopEvents_Beta2_pb2'
  # @@protoc_insertion_point(class_scope:services.telemetry.v1beta2.ShopAction)
  ))
_sym_db.RegisterMessage(ShopAction)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n-io.bloombox.schema.services.telemetry.v1beta2H\001P\001\252\002\021Telemetry.v1beta2'))
# @@protoc_insertion_point(module_scope)
