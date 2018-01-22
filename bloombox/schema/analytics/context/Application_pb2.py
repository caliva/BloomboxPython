# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics/context/Application.proto

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


import bq_field_pb2 as bq__field__pb2
from structs import Version_pb2 as structs_dot_Version__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='analytics/context/Application.proto',
  package='analytics.context',
  syntax='proto3',
  serialized_pb=_b('\n#analytics/context/Application.proto\x12\x11\x61nalytics.context\x1a\x0e\x62q_field.proto\x1a\x15structs/Version.proto\"\xf7\x02\n\x0eWebApplication\x12=\n\x06origin\x18\x01 \x01(\tB-\x8a@*Specifies an origin for a web application.\x12P\n\x08location\x18\x02 \x01(\tB>\x8a@;Full, absolute URL the user was at when the event was sent.\x12-\n\x06\x61nchor\x18\x03 \x01(\tB\x1d\x8a@\x1a\x41nchor in the URL, if any.\x12/\n\x05title\x18\x04 \x01(\tB \x8a@\x1dTitle of the current webpage.\x12\x34\n\x08referrer\x18\x05 \x01(\tB\"\x8a@\x1fReferring URL for this webpage.\x12>\n\x08protocol\x18\x06 \x01(\tB,\x8a@)Protocol that was used to serve this URL.\"\xdd\x03\n\x11\x44\x65viceApplication\x12L\n\x04type\x18\x01 \x01(\x0e\x32\".analytics.context.ApplicationTypeB\x1a\xf0?\x01\x8a@\x14Type of application.\x12P\n\x07version\x18\x02 \x01(\x0b\x32\x14.structs.VersionSpecB)\x8a@&Version for the reporting application.\x12\x7f\n\x03web\x18\n \x01(\x0b\x32!.analytics.context.WebApplicationBM\x8a@JSpecifies information about an event that was sent from a web application.H\x00\x12\x45\n\tbundle_id\x18\x14 \x01(\tB0\x8a@-Specifies a bundle ID for an iOS application.H\x00\x12X\n\x12\x61ndroid_package_id\x18\x1e \x01(\tB:\x8a@7Specifies an application ID for an Android application.H\x00\x42\x06\n\x04spec*,\n\x0f\x41pplicationType\x12\x0c\n\x08INTERNAL\x10\x00\x12\x0b\n\x07PARTNER\x10\x01\x42\x41\n$io.bloombox.schema.telemetry.contextB\x12\x41pplicationContextH\x01P\x00\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,structs_dot_Version__pb2.DESCRIPTOR,])

_APPLICATIONTYPE = _descriptor.EnumDescriptor(
  name='ApplicationType',
  full_name='analytics.context.ApplicationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INTERNAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTNER', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=955,
  serialized_end=999,
)
_sym_db.RegisterEnumDescriptor(_APPLICATIONTYPE)

ApplicationType = enum_type_wrapper.EnumTypeWrapper(_APPLICATIONTYPE)
INTERNAL = 0
PARTNER = 1



_WEBAPPLICATION = _descriptor.Descriptor(
  name='WebApplication',
  full_name='analytics.context.WebApplication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin', full_name='analytics.context.WebApplication.origin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@*Specifies an origin for a web application.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='analytics.context.WebApplication.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@;Full, absolute URL the user was at when the event was sent.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='anchor', full_name='analytics.context.WebApplication.anchor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\032Anchor in the URL, if any.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='analytics.context.WebApplication.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\035Title of the current webpage.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referrer', full_name='analytics.context.WebApplication.referrer', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\037Referring URL for this webpage.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='analytics.context.WebApplication.protocol', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@)Protocol that was used to serve this URL.')), file=DESCRIPTOR),
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
  serialized_start=98,
  serialized_end=473,
)


_DEVICEAPPLICATION = _descriptor.Descriptor(
  name='DeviceApplication',
  full_name='analytics.context.DeviceApplication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='analytics.context.DeviceApplication.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\024Type of application.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='analytics.context.DeviceApplication.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@&Version for the reporting application.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='web', full_name='analytics.context.DeviceApplication.web', index=2,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@JSpecifies information about an event that was sent from a web application.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bundle_id', full_name='analytics.context.DeviceApplication.bundle_id', index=3,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@-Specifies a bundle ID for an iOS application.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='android_package_id', full_name='analytics.context.DeviceApplication.android_package_id', index=4,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@7Specifies an application ID for an Android application.')), file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='spec', full_name='analytics.context.DeviceApplication.spec',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=476,
  serialized_end=953,
)

_DEVICEAPPLICATION.fields_by_name['type'].enum_type = _APPLICATIONTYPE
_DEVICEAPPLICATION.fields_by_name['version'].message_type = structs_dot_Version__pb2._VERSIONSPEC
_DEVICEAPPLICATION.fields_by_name['web'].message_type = _WEBAPPLICATION
_DEVICEAPPLICATION.oneofs_by_name['spec'].fields.append(
  _DEVICEAPPLICATION.fields_by_name['web'])
_DEVICEAPPLICATION.fields_by_name['web'].containing_oneof = _DEVICEAPPLICATION.oneofs_by_name['spec']
_DEVICEAPPLICATION.oneofs_by_name['spec'].fields.append(
  _DEVICEAPPLICATION.fields_by_name['bundle_id'])
_DEVICEAPPLICATION.fields_by_name['bundle_id'].containing_oneof = _DEVICEAPPLICATION.oneofs_by_name['spec']
_DEVICEAPPLICATION.oneofs_by_name['spec'].fields.append(
  _DEVICEAPPLICATION.fields_by_name['android_package_id'])
_DEVICEAPPLICATION.fields_by_name['android_package_id'].containing_oneof = _DEVICEAPPLICATION.oneofs_by_name['spec']
DESCRIPTOR.message_types_by_name['WebApplication'] = _WEBAPPLICATION
DESCRIPTOR.message_types_by_name['DeviceApplication'] = _DEVICEAPPLICATION
DESCRIPTOR.enum_types_by_name['ApplicationType'] = _APPLICATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WebApplication = _reflection.GeneratedProtocolMessageType('WebApplication', (_message.Message,), dict(
  DESCRIPTOR = _WEBAPPLICATION,
  __module__ = 'analytics.context.Application_pb2'
  # @@protoc_insertion_point(class_scope:analytics.context.WebApplication)
  ))
_sym_db.RegisterMessage(WebApplication)

DeviceApplication = _reflection.GeneratedProtocolMessageType('DeviceApplication', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEAPPLICATION,
  __module__ = 'analytics.context.Application_pb2'
  # @@protoc_insertion_point(class_scope:analytics.context.DeviceApplication)
  ))
_sym_db.RegisterMessage(DeviceApplication)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$io.bloombox.schema.telemetry.contextB\022ApplicationContextH\001P\000\370\001\001'))
_WEBAPPLICATION.fields_by_name['origin'].has_options = True
_WEBAPPLICATION.fields_by_name['origin']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@*Specifies an origin for a web application.'))
_WEBAPPLICATION.fields_by_name['location'].has_options = True
_WEBAPPLICATION.fields_by_name['location']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@;Full, absolute URL the user was at when the event was sent.'))
_WEBAPPLICATION.fields_by_name['anchor'].has_options = True
_WEBAPPLICATION.fields_by_name['anchor']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\032Anchor in the URL, if any.'))
_WEBAPPLICATION.fields_by_name['title'].has_options = True
_WEBAPPLICATION.fields_by_name['title']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\035Title of the current webpage.'))
_WEBAPPLICATION.fields_by_name['referrer'].has_options = True
_WEBAPPLICATION.fields_by_name['referrer']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\037Referring URL for this webpage.'))
_WEBAPPLICATION.fields_by_name['protocol'].has_options = True
_WEBAPPLICATION.fields_by_name['protocol']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@)Protocol that was used to serve this URL.'))
_DEVICEAPPLICATION.fields_by_name['type'].has_options = True
_DEVICEAPPLICATION.fields_by_name['type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@\024Type of application.'))
_DEVICEAPPLICATION.fields_by_name['version'].has_options = True
_DEVICEAPPLICATION.fields_by_name['version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@&Version for the reporting application.'))
_DEVICEAPPLICATION.fields_by_name['web'].has_options = True
_DEVICEAPPLICATION.fields_by_name['web']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@JSpecifies information about an event that was sent from a web application.'))
_DEVICEAPPLICATION.fields_by_name['bundle_id'].has_options = True
_DEVICEAPPLICATION.fields_by_name['bundle_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@-Specifies a bundle ID for an iOS application.'))
_DEVICEAPPLICATION.fields_by_name['android_package_id'].has_options = True
_DEVICEAPPLICATION.fields_by_name['android_package_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@7Specifies an application ID for an Android application.'))
# @@protoc_insertion_point(module_scope)
