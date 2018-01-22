# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: structs/pricing/PricingDescriptor.proto

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


from structs.pricing import SaleDescriptor_pb2 as structs_dot_pricing_dot_SaleDescriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='structs/pricing/PricingDescriptor.proto',
  package='structs.pricing',
  syntax='proto3',
  serialized_pb=_b('\n\'structs/pricing/PricingDescriptor.proto\x12\x0fstructs.pricing\x1a$structs/pricing/SaleDescriptor.proto\"=\n\x17PricingTierAvailability\x12\x0f\n\x07offered\x18\x01 \x01(\x08\x12\x11\n\tavailable\x18\x02 \x01(\x08\"\x9a\x01\n\x15UnitPricingDescriptor\x12\x13\n\x0bprice_value\x18\x01 \x01(\x02\x12\x38\n\x06status\x18\x02 \x01(\x0b\x32(.structs.pricing.PricingTierAvailability\x12\x32\n\tdiscounts\x18\x03 \x03(\x0b\x32\x1f.structs.pricing.SaleDescriptor\"\x9e\x01\n\x19WeightedPricingDescriptor\x12\x32\n\x06weight\x18\x01 \x01(\x0e\x32\".structs.pricing.PricingWeightTier\x12\x34\n\x04tier\x18\x02 \x01(\x0b\x32&.structs.pricing.UnitPricingDescriptor\x12\x17\n\x0fweight_in_grams\x18\x03 \x01(\x02\"\x1a\n\x18\x46reebiePricingDescriptor\"\x80\x02\n\x11PricingDescriptor\x12*\n\x04type\x18\x01 \x01(\x0e\x32\x1c.structs.pricing.PricingType\x12\x36\n\x04unit\x18\x14 \x01(\x0b\x32&.structs.pricing.UnitPricingDescriptorH\x00\x12>\n\x08weighted\x18\x15 \x01(\x0b\x32*.structs.pricing.WeightedPricingDescriptorH\x00\x12<\n\x07\x66reebie\x18\x16 \x01(\x0b\x32).structs.pricing.FreebiePricingDescriptorH\x00\x42\t\n\x07pricing\"z\n\x0eProductPricing\x12\x32\n\tdiscounts\x18\x01 \x03(\x0b\x32\x1f.structs.pricing.SaleDescriptor\x12\x34\n\x08manifest\x18\x02 \x03(\x0b\x32\".structs.pricing.PricingDescriptor*2\n\x0bPricingType\x12\x08\n\x04UNIT\x10\x00\x12\x0c\n\x08WEIGHTED\x10\x01\x12\x0b\n\x07\x46REEBIE\x10\x02*\x89\x01\n\x11PricingWeightTier\x12\t\n\x05OTHER\x10\x00\x12\x08\n\x04GRAM\x10\x01\x12\x0c\n\x08HALFGRAM\x10\x02\x12\x0f\n\x0bQUARTERGRAM\x10\x03\x12\x07\n\x03\x44UB\x10\x04\x12\n\n\x06\x45IGHTH\x10\x05\x12\x0b\n\x07QUARTER\x10\x06\x12\x08\n\x04HALF\x10\x07\x12\t\n\x05OUNCE\x10\x08\x12\t\n\x05POUND\x10\tB>\n!io.bloombox.schema.product.structB\x12ProductPricingSpecH\x01P\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[structs_dot_pricing_dot_SaleDescriptor__pb2.DESCRIPTOR,])

_PRICINGTYPE = _descriptor.EnumDescriptor(
  name='PricingType',
  full_name='structs.pricing.PricingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEIGHTED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FREEBIE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=890,
  serialized_end=940,
)
_sym_db.RegisterEnumDescriptor(_PRICINGTYPE)

PricingType = enum_type_wrapper.EnumTypeWrapper(_PRICINGTYPE)
_PRICINGWEIGHTTIER = _descriptor.EnumDescriptor(
  name='PricingWeightTier',
  full_name='structs.pricing.PricingWeightTier',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HALFGRAM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUARTERGRAM', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUB', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EIGHTH', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUARTER', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HALF', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUNCE', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POUND', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=943,
  serialized_end=1080,
)
_sym_db.RegisterEnumDescriptor(_PRICINGWEIGHTTIER)

PricingWeightTier = enum_type_wrapper.EnumTypeWrapper(_PRICINGWEIGHTTIER)
UNIT = 0
WEIGHTED = 1
FREEBIE = 2
OTHER = 0
GRAM = 1
HALFGRAM = 2
QUARTERGRAM = 3
DUB = 4
EIGHTH = 5
QUARTER = 6
HALF = 7
OUNCE = 8
POUND = 9



_PRICINGTIERAVAILABILITY = _descriptor.Descriptor(
  name='PricingTierAvailability',
  full_name='structs.pricing.PricingTierAvailability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offered', full_name='structs.pricing.PricingTierAvailability.offered', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available', full_name='structs.pricing.PricingTierAvailability.available', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=98,
  serialized_end=159,
)


_UNITPRICINGDESCRIPTOR = _descriptor.Descriptor(
  name='UnitPricingDescriptor',
  full_name='structs.pricing.UnitPricingDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price_value', full_name='structs.pricing.UnitPricingDescriptor.price_value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='structs.pricing.UnitPricingDescriptor.status', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discounts', full_name='structs.pricing.UnitPricingDescriptor.discounts', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=162,
  serialized_end=316,
)


_WEIGHTEDPRICINGDESCRIPTOR = _descriptor.Descriptor(
  name='WeightedPricingDescriptor',
  full_name='structs.pricing.WeightedPricingDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='structs.pricing.WeightedPricingDescriptor.weight', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tier', full_name='structs.pricing.WeightedPricingDescriptor.tier', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight_in_grams', full_name='structs.pricing.WeightedPricingDescriptor.weight_in_grams', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=319,
  serialized_end=477,
)


_FREEBIEPRICINGDESCRIPTOR = _descriptor.Descriptor(
  name='FreebiePricingDescriptor',
  full_name='structs.pricing.FreebiePricingDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=479,
  serialized_end=505,
)


_PRICINGDESCRIPTOR = _descriptor.Descriptor(
  name='PricingDescriptor',
  full_name='structs.pricing.PricingDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='structs.pricing.PricingDescriptor.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='structs.pricing.PricingDescriptor.unit', index=1,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weighted', full_name='structs.pricing.PricingDescriptor.weighted', index=2,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freebie', full_name='structs.pricing.PricingDescriptor.freebie', index=3,
      number=22, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='pricing', full_name='structs.pricing.PricingDescriptor.pricing',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=508,
  serialized_end=764,
)


_PRODUCTPRICING = _descriptor.Descriptor(
  name='ProductPricing',
  full_name='structs.pricing.ProductPricing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='discounts', full_name='structs.pricing.ProductPricing.discounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manifest', full_name='structs.pricing.ProductPricing.manifest', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=766,
  serialized_end=888,
)

_UNITPRICINGDESCRIPTOR.fields_by_name['status'].message_type = _PRICINGTIERAVAILABILITY
_UNITPRICINGDESCRIPTOR.fields_by_name['discounts'].message_type = structs_dot_pricing_dot_SaleDescriptor__pb2._SALEDESCRIPTOR
_WEIGHTEDPRICINGDESCRIPTOR.fields_by_name['weight'].enum_type = _PRICINGWEIGHTTIER
_WEIGHTEDPRICINGDESCRIPTOR.fields_by_name['tier'].message_type = _UNITPRICINGDESCRIPTOR
_PRICINGDESCRIPTOR.fields_by_name['type'].enum_type = _PRICINGTYPE
_PRICINGDESCRIPTOR.fields_by_name['unit'].message_type = _UNITPRICINGDESCRIPTOR
_PRICINGDESCRIPTOR.fields_by_name['weighted'].message_type = _WEIGHTEDPRICINGDESCRIPTOR
_PRICINGDESCRIPTOR.fields_by_name['freebie'].message_type = _FREEBIEPRICINGDESCRIPTOR
_PRICINGDESCRIPTOR.oneofs_by_name['pricing'].fields.append(
  _PRICINGDESCRIPTOR.fields_by_name['unit'])
_PRICINGDESCRIPTOR.fields_by_name['unit'].containing_oneof = _PRICINGDESCRIPTOR.oneofs_by_name['pricing']
_PRICINGDESCRIPTOR.oneofs_by_name['pricing'].fields.append(
  _PRICINGDESCRIPTOR.fields_by_name['weighted'])
_PRICINGDESCRIPTOR.fields_by_name['weighted'].containing_oneof = _PRICINGDESCRIPTOR.oneofs_by_name['pricing']
_PRICINGDESCRIPTOR.oneofs_by_name['pricing'].fields.append(
  _PRICINGDESCRIPTOR.fields_by_name['freebie'])
_PRICINGDESCRIPTOR.fields_by_name['freebie'].containing_oneof = _PRICINGDESCRIPTOR.oneofs_by_name['pricing']
_PRODUCTPRICING.fields_by_name['discounts'].message_type = structs_dot_pricing_dot_SaleDescriptor__pb2._SALEDESCRIPTOR
_PRODUCTPRICING.fields_by_name['manifest'].message_type = _PRICINGDESCRIPTOR
DESCRIPTOR.message_types_by_name['PricingTierAvailability'] = _PRICINGTIERAVAILABILITY
DESCRIPTOR.message_types_by_name['UnitPricingDescriptor'] = _UNITPRICINGDESCRIPTOR
DESCRIPTOR.message_types_by_name['WeightedPricingDescriptor'] = _WEIGHTEDPRICINGDESCRIPTOR
DESCRIPTOR.message_types_by_name['FreebiePricingDescriptor'] = _FREEBIEPRICINGDESCRIPTOR
DESCRIPTOR.message_types_by_name['PricingDescriptor'] = _PRICINGDESCRIPTOR
DESCRIPTOR.message_types_by_name['ProductPricing'] = _PRODUCTPRICING
DESCRIPTOR.enum_types_by_name['PricingType'] = _PRICINGTYPE
DESCRIPTOR.enum_types_by_name['PricingWeightTier'] = _PRICINGWEIGHTTIER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PricingTierAvailability = _reflection.GeneratedProtocolMessageType('PricingTierAvailability', (_message.Message,), dict(
  DESCRIPTOR = _PRICINGTIERAVAILABILITY,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:structs.pricing.PricingTierAvailability)
  ))
_sym_db.RegisterMessage(PricingTierAvailability)

UnitPricingDescriptor = _reflection.GeneratedProtocolMessageType('UnitPricingDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _UNITPRICINGDESCRIPTOR,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:structs.pricing.UnitPricingDescriptor)
  ))
_sym_db.RegisterMessage(UnitPricingDescriptor)

WeightedPricingDescriptor = _reflection.GeneratedProtocolMessageType('WeightedPricingDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _WEIGHTEDPRICINGDESCRIPTOR,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:structs.pricing.WeightedPricingDescriptor)
  ))
_sym_db.RegisterMessage(WeightedPricingDescriptor)

FreebiePricingDescriptor = _reflection.GeneratedProtocolMessageType('FreebiePricingDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _FREEBIEPRICINGDESCRIPTOR,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:structs.pricing.FreebiePricingDescriptor)
  ))
_sym_db.RegisterMessage(FreebiePricingDescriptor)

PricingDescriptor = _reflection.GeneratedProtocolMessageType('PricingDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _PRICINGDESCRIPTOR,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:structs.pricing.PricingDescriptor)
  ))
_sym_db.RegisterMessage(PricingDescriptor)

ProductPricing = _reflection.GeneratedProtocolMessageType('ProductPricing', (_message.Message,), dict(
  DESCRIPTOR = _PRODUCTPRICING,
  __module__ = 'structs.pricing.PricingDescriptor_pb2'
  # @@protoc_insertion_point(class_scope:structs.pricing.ProductPricing)
  ))
_sym_db.RegisterMessage(ProductPricing)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!io.bloombox.schema.product.structB\022ProductPricingSpecH\001P\001\370\001\001'))
# @@protoc_insertion_point(module_scope)
