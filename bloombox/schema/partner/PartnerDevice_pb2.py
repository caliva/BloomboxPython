# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: partner/PartnerDevice.proto

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


from device import Device_pb2 as device_dot_Device__pb2
from partner import Partner_pb2 as partner_dot_Partner__pb2
from partner import PartnerLocation_pb2 as partner_dot_PartnerLocation__pb2
from temporal import Instant_pb2 as temporal_dot_Instant__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='partner/PartnerDevice.proto',
  package='partner',
  syntax='proto3',
  serialized_pb=_b('\n\x1bpartner/PartnerDevice.proto\x12\x07partner\x1a\x13\x64\x65vice/Device.proto\x1a\x15partner/Partner.proto\x1a\x1dpartner/PartnerLocation.proto\x1a\x16temporal/Instant.proto\"O\n\x10PartnerDeviceKey\x12-\n\x08location\x18\x01 \x01(\x0b\x32\x1b.partner.PartnerLocationKey\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"\xaa\x02\n\rPartnerDevice\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12!\n\x07partner\x18\x02 \x01(\x0b\x32\x10.partner.Partner\x12*\n\x08location\x18\x03 \x01(\x0b\x32\x18.partner.PartnerLocation\x12(\n\x04type\x18\x04 \x01(\x0e\x32\x1a.partner.PartnerDeviceType\x12*\n\x05\x66lags\x18\x05 \x01(\x0b\x32\x1b.partner.PartnerDeviceFlags\x12\x1e\n\x06\x64\x65vice\x18\x06 \x01(\x0b\x32\x0e.device.Device\x12\x1f\n\x04seen\x18\x07 \x01(\x0b\x32\x11.temporal.Instant\x12%\n\nregistered\x18\x08 \x01(\x0b\x32\x11.temporal.Instant\"V\n\x12PartnerDeviceFlags\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\x12\x11\n\tsuspended\x18\x02 \x01(\x08\x12\x0c\n\x04\x62\x65ta\x18\x03 \x01(\x08\x12\x0f\n\x07sandbox\x18\x04 \x01(\x08*\x93\x01\n\x11PartnerDeviceType\x12\x1b\n\x17UNSPECIFIED_DEVICE_TYPE\x10\x00\x12\x0c\n\x08INTERNAL\x10\x01\x12\x0f\n\x0bMENU_TABLET\x10\n\x12\x0b\n\x07MENU_TV\x10\x0b\x12\x13\n\x0f\x43HECKIN_STATION\x10\x14\x12\x0e\n\nCHECKIN_TV\x10\x15\x12\x10\n\x0cPOS_REGISTER\x10\x1e\x42 \n\x1aio.bloombox.schema.partnerH\x01P\x01\x62\x06proto3')
  ,
  dependencies=[device_dot_Device__pb2.DESCRIPTOR,partner_dot_Partner__pb2.DESCRIPTOR,partner_dot_PartnerLocation__pb2.DESCRIPTOR,temporal_dot_Instant__pb2.DESCRIPTOR,])

_PARTNERDEVICETYPE = _descriptor.EnumDescriptor(
  name='PartnerDeviceType',
  full_name='partner.PartnerDeviceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_DEVICE_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MENU_TABLET', index=2, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MENU_TV', index=3, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKIN_STATION', index=4, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKIN_TV', index=5, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POS_REGISTER', index=6, number=30,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=610,
  serialized_end=757,
)
_sym_db.RegisterEnumDescriptor(_PARTNERDEVICETYPE)

PartnerDeviceType = enum_type_wrapper.EnumTypeWrapper(_PARTNERDEVICETYPE)
UNSPECIFIED_DEVICE_TYPE = 0
INTERNAL = 1
MENU_TABLET = 10
MENU_TV = 11
CHECKIN_STATION = 20
CHECKIN_TV = 21
POS_REGISTER = 30



_PARTNERDEVICEKEY = _descriptor.Descriptor(
  name='PartnerDeviceKey',
  full_name='partner.PartnerDeviceKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='partner.PartnerDeviceKey.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='partner.PartnerDeviceKey.uuid', index=1,
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
  serialized_start=139,
  serialized_end=218,
)


_PARTNERDEVICE = _descriptor.Descriptor(
  name='PartnerDevice',
  full_name='partner.PartnerDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='partner.PartnerDevice.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner', full_name='partner.PartnerDevice.partner', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='partner.PartnerDevice.location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='partner.PartnerDevice.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='partner.PartnerDevice.flags', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='partner.PartnerDevice.device', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seen', full_name='partner.PartnerDevice.seen', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registered', full_name='partner.PartnerDevice.registered', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=221,
  serialized_end=519,
)


_PARTNERDEVICEFLAGS = _descriptor.Descriptor(
  name='PartnerDeviceFlags',
  full_name='partner.PartnerDeviceFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active', full_name='partner.PartnerDeviceFlags.active', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suspended', full_name='partner.PartnerDeviceFlags.suspended', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beta', full_name='partner.PartnerDeviceFlags.beta', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sandbox', full_name='partner.PartnerDeviceFlags.sandbox', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=521,
  serialized_end=607,
)

_PARTNERDEVICEKEY.fields_by_name['location'].message_type = partner_dot_PartnerLocation__pb2._PARTNERLOCATIONKEY
_PARTNERDEVICE.fields_by_name['partner'].message_type = partner_dot_Partner__pb2._PARTNER
_PARTNERDEVICE.fields_by_name['location'].message_type = partner_dot_PartnerLocation__pb2._PARTNERLOCATION
_PARTNERDEVICE.fields_by_name['type'].enum_type = _PARTNERDEVICETYPE
_PARTNERDEVICE.fields_by_name['flags'].message_type = _PARTNERDEVICEFLAGS
_PARTNERDEVICE.fields_by_name['device'].message_type = device_dot_Device__pb2._DEVICE
_PARTNERDEVICE.fields_by_name['seen'].message_type = temporal_dot_Instant__pb2._INSTANT
_PARTNERDEVICE.fields_by_name['registered'].message_type = temporal_dot_Instant__pb2._INSTANT
DESCRIPTOR.message_types_by_name['PartnerDeviceKey'] = _PARTNERDEVICEKEY
DESCRIPTOR.message_types_by_name['PartnerDevice'] = _PARTNERDEVICE
DESCRIPTOR.message_types_by_name['PartnerDeviceFlags'] = _PARTNERDEVICEFLAGS
DESCRIPTOR.enum_types_by_name['PartnerDeviceType'] = _PARTNERDEVICETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PartnerDeviceKey = _reflection.GeneratedProtocolMessageType('PartnerDeviceKey', (_message.Message,), dict(
  DESCRIPTOR = _PARTNERDEVICEKEY,
  __module__ = 'partner.PartnerDevice_pb2'
  # @@protoc_insertion_point(class_scope:partner.PartnerDeviceKey)
  ))
_sym_db.RegisterMessage(PartnerDeviceKey)

PartnerDevice = _reflection.GeneratedProtocolMessageType('PartnerDevice', (_message.Message,), dict(
  DESCRIPTOR = _PARTNERDEVICE,
  __module__ = 'partner.PartnerDevice_pb2'
  # @@protoc_insertion_point(class_scope:partner.PartnerDevice)
  ))
_sym_db.RegisterMessage(PartnerDevice)

PartnerDeviceFlags = _reflection.GeneratedProtocolMessageType('PartnerDeviceFlags', (_message.Message,), dict(
  DESCRIPTOR = _PARTNERDEVICEFLAGS,
  __module__ = 'partner.PartnerDevice_pb2'
  # @@protoc_insertion_point(class_scope:partner.PartnerDeviceFlags)
  ))
_sym_db.RegisterMessage(PartnerDeviceFlags)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032io.bloombox.schema.partnerH\001P\001'))
# @@protoc_insertion_point(module_scope)