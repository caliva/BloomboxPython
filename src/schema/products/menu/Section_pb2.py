# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: products/menu/Section.proto

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


from content import Name_pb2 as content_dot_Name__pb2
from media import MediaItem_pb2 as media_dot_MediaItem__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='products/menu/Section.proto',
  package='opencannabis.products.menu.section',
  syntax='proto3',
  serialized_pb=_b('\n\x1bproducts/menu/Section.proto\x12\"opencannabis.products.menu.section\x1a\x12\x63ontent/Name.proto\x1a\x15media/MediaItem.proto\"`\n\rCustomSection\x12\n\n\x02id\x18\x01 \x01(\t\x12\x43\n\x06\x66ilter\x18\x02 \x01(\x0e\x32\x33.opencannabis.products.menu.section.FilteredSection\"N\n\x0cSectionMedia\x12>\n\x17tablet_homescreen_media\x18\x02 \x01(\x0b\x32\x1d.opencannabis.media.MediaItem\"|\n\x0fSectionSettings\x12(\n\x04name\x18\x01 \x01(\x0b\x32\x1a.opencannabis.content.Name\x12?\n\x05media\x18\x02 \x01(\x0b\x32\x30.opencannabis.products.menu.section.SectionMedia\"\xb9\x02\n\x0bSectionSpec\x12>\n\x07section\x18\x01 \x01(\x0e\x32+.opencannabis.products.menu.section.SectionH\x00\x12K\n\x0e\x63ustom_section\x18\x02 \x01(\x0b\x32\x31.opencannabis.products.menu.section.CustomSectionH\x00\x12\x0e\n\x04name\x18\x03 \x01(\tH\x00\x12\x45\n\x08settings\x18\x04 \x01(\x0b\x32\x33.opencannabis.products.menu.section.SectionSettings\x12>\n\x05\x66lags\x18\x05 \x03(\x0e\x32/.opencannabis.products.menu.section.SectionFlagB\x06\n\x04spec*\'\n\x0bSectionFlag\x12\n\n\x06HIDDEN\x10\x00\x12\x0c\n\x08\x46\x45\x41TURED\x10\x01*\x8d\x01\n\x07Section\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07\x46LOWERS\x10\x01\x12\x0c\n\x08\x45XTRACTS\x10\x02\x12\x0b\n\x07\x45\x44IBLES\x10\x03\x12\x0e\n\nCARTRIDGES\x10\x04\x12\x0e\n\nAPOTHECARY\x10\x05\x12\x0c\n\x08PREROLLS\x10\x06\x12\n\n\x06PLANTS\x10\x07\x12\x0f\n\x0bMERCHANDISE\x10\x08*2\n\x0f\x46ilteredSection\x12\x0b\n\x07ON_SALE\x10\x00\x12\t\n\x05HOUSE\x10\x01\x12\x07\n\x03\x43\x42\x44\x10\x02\x42)\n#io.opencannabis.schema.menu.sectionH\x01P\x01\x62\x06proto3')
  ,
  dependencies=[content_dot_Name__pb2.DESCRIPTOR,media_dot_MediaItem__pb2.DESCRIPTOR,])

_SECTIONFLAG = _descriptor.EnumDescriptor(
  name='SectionFlag',
  full_name='opencannabis.products.menu.section.SectionFlag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HIDDEN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=730,
  serialized_end=769,
)
_sym_db.RegisterEnumDescriptor(_SECTIONFLAG)

SectionFlag = enum_type_wrapper.EnumTypeWrapper(_SECTIONFLAG)
_SECTION = _descriptor.EnumDescriptor(
  name='Section',
  full_name='opencannabis.products.menu.section.Section',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOWERS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTRACTS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EDIBLES', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARTRIDGES', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APOTHECARY', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREROLLS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLANTS', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MERCHANDISE', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=772,
  serialized_end=913,
)
_sym_db.RegisterEnumDescriptor(_SECTION)

Section = enum_type_wrapper.EnumTypeWrapper(_SECTION)
_FILTEREDSECTION = _descriptor.EnumDescriptor(
  name='FilteredSection',
  full_name='opencannabis.products.menu.section.FilteredSection',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ON_SALE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOUSE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CBD', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=915,
  serialized_end=965,
)
_sym_db.RegisterEnumDescriptor(_FILTEREDSECTION)

FilteredSection = enum_type_wrapper.EnumTypeWrapper(_FILTEREDSECTION)
HIDDEN = 0
FEATURED = 1
UNSPECIFIED = 0
FLOWERS = 1
EXTRACTS = 2
EDIBLES = 3
CARTRIDGES = 4
APOTHECARY = 5
PREROLLS = 6
PLANTS = 7
MERCHANDISE = 8
ON_SALE = 0
HOUSE = 1
CBD = 2



_CUSTOMSECTION = _descriptor.Descriptor(
  name='CustomSection',
  full_name='opencannabis.products.menu.section.CustomSection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='opencannabis.products.menu.section.CustomSection.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='opencannabis.products.menu.section.CustomSection.filter', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=110,
  serialized_end=206,
)


_SECTIONMEDIA = _descriptor.Descriptor(
  name='SectionMedia',
  full_name='opencannabis.products.menu.section.SectionMedia',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tablet_homescreen_media', full_name='opencannabis.products.menu.section.SectionMedia.tablet_homescreen_media', index=0,
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
  serialized_start=208,
  serialized_end=286,
)


_SECTIONSETTINGS = _descriptor.Descriptor(
  name='SectionSettings',
  full_name='opencannabis.products.menu.section.SectionSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='opencannabis.products.menu.section.SectionSettings.name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='media', full_name='opencannabis.products.menu.section.SectionSettings.media', index=1,
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
  serialized_start=288,
  serialized_end=412,
)


_SECTIONSPEC = _descriptor.Descriptor(
  name='SectionSpec',
  full_name='opencannabis.products.menu.section.SectionSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='section', full_name='opencannabis.products.menu.section.SectionSpec.section', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_section', full_name='opencannabis.products.menu.section.SectionSpec.custom_section', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='opencannabis.products.menu.section.SectionSpec.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='opencannabis.products.menu.section.SectionSpec.settings', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='opencannabis.products.menu.section.SectionSpec.flags', index=4,
      number=5, type=14, cpp_type=8, label=3,
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
    _descriptor.OneofDescriptor(
      name='spec', full_name='opencannabis.products.menu.section.SectionSpec.spec',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=415,
  serialized_end=728,
)

_CUSTOMSECTION.fields_by_name['filter'].enum_type = _FILTEREDSECTION
_SECTIONMEDIA.fields_by_name['tablet_homescreen_media'].message_type = media_dot_MediaItem__pb2._MEDIAITEM
_SECTIONSETTINGS.fields_by_name['name'].message_type = content_dot_Name__pb2._NAME
_SECTIONSETTINGS.fields_by_name['media'].message_type = _SECTIONMEDIA
_SECTIONSPEC.fields_by_name['section'].enum_type = _SECTION
_SECTIONSPEC.fields_by_name['custom_section'].message_type = _CUSTOMSECTION
_SECTIONSPEC.fields_by_name['settings'].message_type = _SECTIONSETTINGS
_SECTIONSPEC.fields_by_name['flags'].enum_type = _SECTIONFLAG
_SECTIONSPEC.oneofs_by_name['spec'].fields.append(
  _SECTIONSPEC.fields_by_name['section'])
_SECTIONSPEC.fields_by_name['section'].containing_oneof = _SECTIONSPEC.oneofs_by_name['spec']
_SECTIONSPEC.oneofs_by_name['spec'].fields.append(
  _SECTIONSPEC.fields_by_name['custom_section'])
_SECTIONSPEC.fields_by_name['custom_section'].containing_oneof = _SECTIONSPEC.oneofs_by_name['spec']
_SECTIONSPEC.oneofs_by_name['spec'].fields.append(
  _SECTIONSPEC.fields_by_name['name'])
_SECTIONSPEC.fields_by_name['name'].containing_oneof = _SECTIONSPEC.oneofs_by_name['spec']
DESCRIPTOR.message_types_by_name['CustomSection'] = _CUSTOMSECTION
DESCRIPTOR.message_types_by_name['SectionMedia'] = _SECTIONMEDIA
DESCRIPTOR.message_types_by_name['SectionSettings'] = _SECTIONSETTINGS
DESCRIPTOR.message_types_by_name['SectionSpec'] = _SECTIONSPEC
DESCRIPTOR.enum_types_by_name['SectionFlag'] = _SECTIONFLAG
DESCRIPTOR.enum_types_by_name['Section'] = _SECTION
DESCRIPTOR.enum_types_by_name['FilteredSection'] = _FILTEREDSECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomSection = _reflection.GeneratedProtocolMessageType('CustomSection', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMSECTION,
  __module__ = 'products.menu.Section_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.products.menu.section.CustomSection)
  ))
_sym_db.RegisterMessage(CustomSection)

SectionMedia = _reflection.GeneratedProtocolMessageType('SectionMedia', (_message.Message,), dict(
  DESCRIPTOR = _SECTIONMEDIA,
  __module__ = 'products.menu.Section_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.products.menu.section.SectionMedia)
  ))
_sym_db.RegisterMessage(SectionMedia)

SectionSettings = _reflection.GeneratedProtocolMessageType('SectionSettings', (_message.Message,), dict(
  DESCRIPTOR = _SECTIONSETTINGS,
  __module__ = 'products.menu.Section_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.products.menu.section.SectionSettings)
  ))
_sym_db.RegisterMessage(SectionSettings)

SectionSpec = _reflection.GeneratedProtocolMessageType('SectionSpec', (_message.Message,), dict(
  DESCRIPTOR = _SECTIONSPEC,
  __module__ = 'products.menu.Section_pb2'
  # @@protoc_insertion_point(class_scope:opencannabis.products.menu.section.SectionSpec)
  ))
_sym_db.RegisterMessage(SectionSpec)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#io.opencannabis.schema.menu.sectionH\001P\001'))
# @@protoc_insertion_point(module_scope)