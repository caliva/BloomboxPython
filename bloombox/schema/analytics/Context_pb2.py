# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics/Context.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bq_field_pb2 as bq__field__pb2
from geo import Location_pb2 as geo_dot_Location__pb2
from identity import User_pb2 as identity_dot_User__pb2
from temporal import Instant_pb2 as temporal_dot_Instant__pb2
from partner import Partner_pb2 as partner_dot_Partner__pb2
from partner import PartnerLocation_pb2 as partner_dot_PartnerLocation__pb2
from structs import Version_pb2 as structs_dot_Version__pb2
from analytics import Scope_pb2 as analytics_dot_Scope__pb2
from analytics.context import Browser_pb2 as analytics_dot_context_dot_Browser__pb2
from analytics.context import Library_pb2 as analytics_dot_context_dot_Library__pb2
from analytics.context import Collection_pb2 as analytics_dot_context_dot_Collection__pb2
from analytics.context import Application_pb2 as analytics_dot_context_dot_Application__pb2
from analytics.context import NativeDevice_pb2 as analytics_dot_context_dot_NativeDevice__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='analytics/Context.proto',
  package='analytics',
  syntax='proto3',
  serialized_pb=_b('\n\x17\x61nalytics/Context.proto\x12\tanalytics\x1a\x0e\x62q_field.proto\x1a\x12geo/Location.proto\x1a\x13identity/User.proto\x1a\x16temporal/Instant.proto\x1a\x15partner/Partner.proto\x1a\x1dpartner/PartnerLocation.proto\x1a\x15structs/Version.proto\x1a\x15\x61nalytics/Scope.proto\x1a\x1f\x61nalytics/context/Browser.proto\x1a\x1f\x61nalytics/context/Library.proto\x1a\"analytics/context/Collection.proto\x1a#analytics/context/Application.proto\x1a$analytics/context/NativeDevice.proto\"\xb8\x04\n\rEventPosition\x12\x89\x01\n\x06ingest\x18\x02 \x01(\x0b\x32\x11.temporal.InstantBf\xf0?\x01\xfa?\tTIMESTAMP\x8a@TTimestamp describing when this event was ingested by the backend telemetry pipeline.\x12\x97\x01\n\x08occurred\x18\x03 \x01(\x0b\x32\x11.temporal.InstantBr\xf0?\x01\xfa?\tTIMESTAMP\x8a@`Timestamp describing when this event occurred, as reported by the submitting device or endpoint.\x12\x82\x01\n\tprocessed\x18\x04 \x01(\x04\x42o\xfa?\tTIMESTAMP\x8a@`Timestamp describing when this event occurred, as reported by the submitting device or endpoint.\x12|\n\x08\x65nriched\x18\x05 \x01(\x04\x42j\xfa?\tTIMESTAMP\x8a@[Timestamps describing each instance of this event being enriched by the telemetry pipeline.\"\xb0\x02\n\x0b\x45ventActors\x12^\n\x04user\x18\x01 \x01(\x0b\x32\x0e.identity.UserB@\x8a@=User account that was logged in when the event was submitted.\x12Z\n\x07partner\x18\x02 \x01(\x0b\x32\x10.partner.PartnerB7\x8a@4Partner account under which the event was submitted.\x12\x65\n\x08location\x18\x03 \x01(\x0b\x32\x18.partner.PartnerLocationB9\x8a@6Location account under which this event was submitted.\"\xd4\x0b\n\x07\x43ontext\x12r\n\ncollection\x18\x01 \x01(\x0b\x32\x1d.analytics.context.CollectionB?\xf0?\x01\x8a@9Collection information, specifies event type or category.\x12`\n\x08user_key\x18\x02 \x01(\x0b\x32\x11.identity.UserKeyB;\x8a@8Specifies the user associated with this event, if known.\x12M\n\x0b\x66ingerprint\x18\x03 \x01(\tB8\x8a@5Unique device fingerprint for this analytics context.\x12\x97\x01\n\x05group\x18\x04 \x01(\tB\x87\x01\x8a@\x83\x01\x41rbitrary group ID for this event. Gathers events into buckets of variable size, usually used to indicate a user or device session.\x12h\n\x08hostname\x18\x05 \x01(\tBV\x8a@SHostname of the server or client that transmitted this information, if it is known.\x12l\n\nip_address\x18\x06 \x01(\tBX\x8a@UIP address of the server or client that transmitted this information, if is is known.\x12O\n\x05scope\x18\x07 \x01(\x0b\x32\x10.analytics.ScopeB.\x8a@+Partner and commercial scope of this event.\x12V\n\x03\x61pp\x18\x08 \x01(\x0b\x32$.analytics.context.DeviceApplicationB#\x8a@ Application version information.\x12R\n\x07library\x18\t \x01(\x0b\x32 .analytics.context.DeviceLibraryB\x1f\x8a@\x1cLibrary version information.\x12\xf6\x01\n\x06native\x18\n \x01(\x0b\x32&.analytics.context.NativeDeviceContextB\xbd\x01\x8a@\xb9\x01Specifies information about a native device, when the event is being sent from a native context of some kind, such as a mobile phone application or embedded device running partner code.\x12\xac\x01\n\x07\x62rowser\x18\x0b \x01(\x0b\x32\'.analytics.context.BrowserDeviceContextBr\x8a@oSpecifies information about a web browser, when the event is being sent from some kind of web browsing context.\x12\x8c\x01\n\x08location\x18\x0c \x01(\x0b\x32\r.geo.LocationBk\x8a@hOrigin location for this event, as determined by geolocation or explicit inclusion in the event payload.B7\n\x1cio.bloombox.schema.telemetryB\x10\x41nalyticsContextH\x01P\x00\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[bq__field__pb2.DESCRIPTOR,geo_dot_Location__pb2.DESCRIPTOR,identity_dot_User__pb2.DESCRIPTOR,temporal_dot_Instant__pb2.DESCRIPTOR,partner_dot_Partner__pb2.DESCRIPTOR,partner_dot_PartnerLocation__pb2.DESCRIPTOR,structs_dot_Version__pb2.DESCRIPTOR,analytics_dot_Scope__pb2.DESCRIPTOR,analytics_dot_context_dot_Browser__pb2.DESCRIPTOR,analytics_dot_context_dot_Library__pb2.DESCRIPTOR,analytics_dot_context_dot_Collection__pb2.DESCRIPTOR,analytics_dot_context_dot_Application__pb2.DESCRIPTOR,analytics_dot_context_dot_NativeDevice__pb2.DESCRIPTOR,])




_EVENTPOSITION = _descriptor.Descriptor(
  name='EventPosition',
  full_name='analytics.EventPosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ingest', full_name='analytics.EventPosition.ingest', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\372?\tTIMESTAMP\212@TTimestamp describing when this event was ingested by the backend telemetry pipeline.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occurred', full_name='analytics.EventPosition.occurred', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\372?\tTIMESTAMP\212@`Timestamp describing when this event occurred, as reported by the submitting device or endpoint.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processed', full_name='analytics.EventPosition.processed', index=2,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372?\tTIMESTAMP\212@`Timestamp describing when this event occurred, as reported by the submitting device or endpoint.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enriched', full_name='analytics.EventPosition.enriched', index=3,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372?\tTIMESTAMP\212@[Timestamps describing each instance of this event being enriched by the telemetry pipeline.')), file=DESCRIPTOR),
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
  serialized_start=397,
  serialized_end=965,
)


_EVENTACTORS = _descriptor.Descriptor(
  name='EventActors',
  full_name='analytics.EventActors',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='analytics.EventActors.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@=User account that was logged in when the event was submitted.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner', full_name='analytics.EventActors.partner', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@4Partner account under which the event was submitted.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='analytics.EventActors.location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@6Location account under which this event was submitted.')), file=DESCRIPTOR),
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
  serialized_start=968,
  serialized_end=1272,
)


_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='analytics.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collection', full_name='analytics.Context.collection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@9Collection information, specifies event type or category.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_key', full_name='analytics.Context.user_key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@8Specifies the user associated with this event, if known.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='analytics.Context.fingerprint', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@5Unique device fingerprint for this analytics context.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='analytics.Context.group', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\203\001Arbitrary group ID for this event. Gathers events into buckets of variable size, usually used to indicate a user or device session.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='analytics.Context.hostname', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@SHostname of the server or client that transmitted this information, if it is known.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='analytics.Context.ip_address', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@UIP address of the server or client that transmitted this information, if is is known.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='analytics.Context.scope', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@+Partner and commercial scope of this event.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app', full_name='analytics.Context.app', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@ Application version information.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='library', full_name='analytics.Context.library', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\034Library version information.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='native', full_name='analytics.Context.native', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\271\001Specifies information about a native device, when the event is being sent from a native context of some kind, such as a mobile phone application or embedded device running partner code.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='browser', full_name='analytics.Context.browser', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@oSpecifies information about a web browser, when the event is being sent from some kind of web browsing context.')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='analytics.Context.location', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@hOrigin location for this event, as determined by geolocation or explicit inclusion in the event payload.')), file=DESCRIPTOR),
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
  serialized_start=1275,
  serialized_end=2767,
)

_EVENTPOSITION.fields_by_name['ingest'].message_type = temporal_dot_Instant__pb2._INSTANT
_EVENTPOSITION.fields_by_name['occurred'].message_type = temporal_dot_Instant__pb2._INSTANT
_EVENTACTORS.fields_by_name['user'].message_type = identity_dot_User__pb2._USER
_EVENTACTORS.fields_by_name['partner'].message_type = partner_dot_Partner__pb2._PARTNER
_EVENTACTORS.fields_by_name['location'].message_type = partner_dot_PartnerLocation__pb2._PARTNERLOCATION
_CONTEXT.fields_by_name['collection'].message_type = analytics_dot_context_dot_Collection__pb2._COLLECTION
_CONTEXT.fields_by_name['user_key'].message_type = identity_dot_User__pb2._USERKEY
_CONTEXT.fields_by_name['scope'].message_type = analytics_dot_Scope__pb2._SCOPE
_CONTEXT.fields_by_name['app'].message_type = analytics_dot_context_dot_Application__pb2._DEVICEAPPLICATION
_CONTEXT.fields_by_name['library'].message_type = analytics_dot_context_dot_Library__pb2._DEVICELIBRARY
_CONTEXT.fields_by_name['native'].message_type = analytics_dot_context_dot_NativeDevice__pb2._NATIVEDEVICECONTEXT
_CONTEXT.fields_by_name['browser'].message_type = analytics_dot_context_dot_Browser__pb2._BROWSERDEVICECONTEXT
_CONTEXT.fields_by_name['location'].message_type = geo_dot_Location__pb2._LOCATION
DESCRIPTOR.message_types_by_name['EventPosition'] = _EVENTPOSITION
DESCRIPTOR.message_types_by_name['EventActors'] = _EVENTACTORS
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventPosition = _reflection.GeneratedProtocolMessageType('EventPosition', (_message.Message,), dict(
  DESCRIPTOR = _EVENTPOSITION,
  __module__ = 'analytics.Context_pb2'
  # @@protoc_insertion_point(class_scope:analytics.EventPosition)
  ))
_sym_db.RegisterMessage(EventPosition)

EventActors = _reflection.GeneratedProtocolMessageType('EventActors', (_message.Message,), dict(
  DESCRIPTOR = _EVENTACTORS,
  __module__ = 'analytics.Context_pb2'
  # @@protoc_insertion_point(class_scope:analytics.EventActors)
  ))
_sym_db.RegisterMessage(EventActors)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT,
  __module__ = 'analytics.Context_pb2'
  # @@protoc_insertion_point(class_scope:analytics.Context)
  ))
_sym_db.RegisterMessage(Context)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034io.bloombox.schema.telemetryB\020AnalyticsContextH\001P\000\370\001\001'))
_EVENTPOSITION.fields_by_name['ingest'].has_options = True
_EVENTPOSITION.fields_by_name['ingest']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\372?\tTIMESTAMP\212@TTimestamp describing when this event was ingested by the backend telemetry pipeline.'))
_EVENTPOSITION.fields_by_name['occurred'].has_options = True
_EVENTPOSITION.fields_by_name['occurred']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\372?\tTIMESTAMP\212@`Timestamp describing when this event occurred, as reported by the submitting device or endpoint.'))
_EVENTPOSITION.fields_by_name['processed'].has_options = True
_EVENTPOSITION.fields_by_name['processed']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372?\tTIMESTAMP\212@`Timestamp describing when this event occurred, as reported by the submitting device or endpoint.'))
_EVENTPOSITION.fields_by_name['enriched'].has_options = True
_EVENTPOSITION.fields_by_name['enriched']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372?\tTIMESTAMP\212@[Timestamps describing each instance of this event being enriched by the telemetry pipeline.'))
_EVENTACTORS.fields_by_name['user'].has_options = True
_EVENTACTORS.fields_by_name['user']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@=User account that was logged in when the event was submitted.'))
_EVENTACTORS.fields_by_name['partner'].has_options = True
_EVENTACTORS.fields_by_name['partner']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@4Partner account under which the event was submitted.'))
_EVENTACTORS.fields_by_name['location'].has_options = True
_EVENTACTORS.fields_by_name['location']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@6Location account under which this event was submitted.'))
_CONTEXT.fields_by_name['collection'].has_options = True
_CONTEXT.fields_by_name['collection']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\360?\001\212@9Collection information, specifies event type or category.'))
_CONTEXT.fields_by_name['user_key'].has_options = True
_CONTEXT.fields_by_name['user_key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@8Specifies the user associated with this event, if known.'))
_CONTEXT.fields_by_name['fingerprint'].has_options = True
_CONTEXT.fields_by_name['fingerprint']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@5Unique device fingerprint for this analytics context.'))
_CONTEXT.fields_by_name['group'].has_options = True
_CONTEXT.fields_by_name['group']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\203\001Arbitrary group ID for this event. Gathers events into buckets of variable size, usually used to indicate a user or device session.'))
_CONTEXT.fields_by_name['hostname'].has_options = True
_CONTEXT.fields_by_name['hostname']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@SHostname of the server or client that transmitted this information, if it is known.'))
_CONTEXT.fields_by_name['ip_address'].has_options = True
_CONTEXT.fields_by_name['ip_address']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@UIP address of the server or client that transmitted this information, if is is known.'))
_CONTEXT.fields_by_name['scope'].has_options = True
_CONTEXT.fields_by_name['scope']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@+Partner and commercial scope of this event.'))
_CONTEXT.fields_by_name['app'].has_options = True
_CONTEXT.fields_by_name['app']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@ Application version information.'))
_CONTEXT.fields_by_name['library'].has_options = True
_CONTEXT.fields_by_name['library']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\034Library version information.'))
_CONTEXT.fields_by_name['native'].has_options = True
_CONTEXT.fields_by_name['native']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@\271\001Specifies information about a native device, when the event is being sent from a native context of some kind, such as a mobile phone application or embedded device running partner code.'))
_CONTEXT.fields_by_name['browser'].has_options = True
_CONTEXT.fields_by_name['browser']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@oSpecifies information about a web browser, when the event is being sent from some kind of web browsing context.'))
_CONTEXT.fields_by_name['location'].has_options = True
_CONTEXT.fields_by_name['location']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\212@hOrigin location for this event, as determined by geolocation or explicit inclusion in the event payload.'))
# @@protoc_insertion_point(module_scope)