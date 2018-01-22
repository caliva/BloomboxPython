# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: media/MediaOrientation.proto

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
  name='media/MediaOrientation.proto',
  package='media',
  syntax='proto3',
  serialized_pb=_b('\n\x1cmedia/MediaOrientation.proto\x12\x05media*\x84\x01\n\x10MediaOrientation\x12\x06\n\x02UP\x10\x00\x12\x08\n\x04\x44OWN\x10\x01\x12\x08\n\x04LEFT\x10\x02\x12\t\n\x05RIGHT\x10\x03\x12\x0f\n\x0bUP_MIRRORED\x10\x04\x12\x11\n\rDOWN_MIRRORED\x10\x05\x12\x11\n\rLEFT_MIRRORED\x10\x06\x12\x12\n\x0eRIGHT_MIRRORED\x10\x07\x42!\n\x18io.bloombox.schema.mediaH\x01P\x01\xf8\x01\x01\x62\x06proto3')
)

_MEDIAORIENTATION = _descriptor.EnumDescriptor(
  name='MediaOrientation',
  full_name='media.MediaOrientation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UP_MIRRORED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWN_MIRRORED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT_MIRRORED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_MIRRORED', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=40,
  serialized_end=172,
)
_sym_db.RegisterEnumDescriptor(_MEDIAORIENTATION)

MediaOrientation = enum_type_wrapper.EnumTypeWrapper(_MEDIAORIENTATION)
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
UP_MIRRORED = 4
DOWN_MIRRORED = 5
LEFT_MIRRORED = 6
RIGHT_MIRRORED = 7


DESCRIPTOR.enum_types_by_name['MediaOrientation'] = _MEDIAORIENTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030io.bloombox.schema.mediaH\001P\001\370\001\001'))
# @@protoc_insertion_point(module_scope)