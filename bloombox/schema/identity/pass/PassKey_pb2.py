# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: identity/pass/PassKey.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='identity/pass/PassKey.proto',
  package='identity.pass',
  syntax='proto3',
  serialized_pb=_b('\n\x1bidentity/pass/PassKey.proto\x12\ridentity.pass\"7\n\x07PassKey\x12\x0f\n\x07\x65ncoded\x18\x01 \x01(\t\x12\x0e\n\x06serial\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\tB\x1d\n\x17io.bloombox.schema.passH\x01P\x01\x62\x06proto3')
)




_PASSKEY = _descriptor.Descriptor(
  name='PassKey',
  full_name='identity.pass.PassKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encoded', full_name='identity.pass.PassKey.encoded', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial', full_name='identity.pass.PassKey.serial', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='identity.pass.PassKey.uid', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=46,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['PassKey'] = _PASSKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PassKey = _reflection.GeneratedProtocolMessageType('PassKey', (_message.Message,), dict(
  DESCRIPTOR = _PASSKEY,
  __module__ = 'identity.pass.PassKey_pb2'
  # @@protoc_insertion_point(class_scope:identity.pass.PassKey)
  ))
_sym_db.RegisterMessage(PassKey)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027io.bloombox.schema.passH\001P\001'))
# @@protoc_insertion_point(module_scope)
