from __future__ import absolute_import
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TSDArchives_sos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import TSDArchives_pb2 as TSDArchives__pb2
from . import TSSArchives_sos_pb2 as TSSArchives__sos__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TSDArchives_sos.proto',
  package='TSD',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x15TSDArchives_sos.proto\x12\x03TSD\x1a\x11TSDArchives.proto\x1a\x15TSSArchives_sos.proto\"C\n\x12SpecSetFillArchive\x12\x1e\n\x04\x66ill\x18\x01 \x01(\x0b\x32\x10.TSD.FillArchive\x12\r\n\x05unset\x18\x02 \x02(\x08\"M\n\x15SpecSetLineEndArchive\x12%\n\x08line_end\x18\x01 \x01(\x0b\x32\x13.TSD.LineEndArchive\x12\r\n\x05unset\x18\x02 \x02(\x08\"U\n\x18SpecSetReflectionArchive\x12*\n\nreflection\x18\x01 \x01(\x0b\x32\x16.TSD.ReflectionArchive\x12\r\n\x05unset\x18\x02 \x02(\x08\"I\n\x14SpecSetShadowArchive\x12\"\n\x06shadow\x18\x01 \x01(\x0b\x32\x12.TSD.ShadowArchive\x12\r\n\x05unset\x18\x02 \x02(\x08\"I\n\x14SpecSetStrokeArchive\x12\"\n\x06stroke\x18\x01 \x01(\x0b\x32\x12.TSD.StrokeArchive\x12\r\n\x05unset\x18\x02 \x02(\x08\"\xa1\x02\n\x0fSpecFillArchive\x12\x44\n\x19spec_color_fill_set_color\x18\x01 \x01(\x0b\x32!.TSD.SpecColorFillSetColorArchive\x12J\n\x1cspec_gradient_fill_set_angle\x18\x02 \x01(\x0b\x32$.TSD.SpecGradientFillSetAngleArchive\x12L\n\x1dspec_image_fill_set_technique\x18\x03 \x01(\x0b\x32%.TSD.SpecImageFillSetTechniqueArchive\x12.\n\rspec_set_fill\x18\x04 \x01(\x0b\x32\x17.TSD.SpecSetFillArchive\"K\n\x12SpecLineEndArchive\x12\x35\n\x11spec_set_line_end\x18\x01 \x01(\x0b\x32\x1a.TSD.SpecSetLineEndArchive\"\x9e\x01\n\x15SpecReflectionArchive\x12I\n\x1bspec_reflection_set_opacity\x18\x01 \x01(\x0b\x32$.TSD.SpecReflectionSetOpacityArchive\x12:\n\x13spec_set_reflection\x18\x02 \x01(\x0b\x32\x1d.TSD.SpecSetReflectionArchive\"\x8a\x03\n\x11SpecShadowArchive\x12\x32\n\x0fspec_set_shadow\x18\x01 \x01(\x0b\x32\x19.TSD.SpecSetShadowArchive\x12=\n\x15spec_shadow_set_angle\x18\x02 \x01(\x0b\x32\x1e.TSD.SpecShadowSetAngleArchive\x12=\n\x15spec_shadow_set_color\x18\x03 \x01(\x0b\x32\x1e.TSD.SpecShadowSetColorArchive\x12?\n\x16spec_shadow_set_offset\x18\x04 \x01(\x0b\x32\x1f.TSD.SpecShadowSetOffsetArchive\x12\x41\n\x17spec_shadow_set_opacity\x18\x05 \x01(\x0b\x32 .TSD.SpecShadowSetOpacityArchive\x12?\n\x16spec_shadow_set_radius\x18\x06 \x01(\x0b\x32\x1f.TSD.SpecShadowSetRadiusArchive\"\xd0\x02\n\x11SpecStrokeArchive\x12\x46\n\x1aspec_frame_set_asset_scale\x18\x01 \x01(\x0b\x32\".TSD.SpecFrameSetAssetScaleArchive\x12\x32\n\x0fspec_set_stroke\x18\x02 \x01(\x0b\x32\x19.TSD.SpecSetStrokeArchive\x12=\n\x15spec_stroke_set_color\x18\x03 \x01(\x0b\x32\x1e.TSD.SpecStrokeSetColorArchive\x12\x41\n\x17spec_stroke_set_pattern\x18\x04 \x01(\x0b\x32 .TSD.SpecStrokeSetPatternArchive\x12=\n\x15spec_stroke_set_width\x18\x05 \x01(\x0b\x32\x1e.TSD.SpecStrokeSetWidthArchive\"\x9c\x04\n&BaseShapeStylePropertyChangeSetArchive\x12\"\n\x04\x66ill\x18\x01 \x01(\x0b\x32\x14.TSD.SpecFillArchive\x12\x16\n\x0e\x66ill_undefined\x18\x02 \x01(\x08\x12&\n\x06stroke\x18\x03 \x01(\x0b\x32\x16.TSD.SpecStrokeArchive\x12\x18\n\x10stroke_undefined\x18\x04 \x01(\x08\x12\'\n\x07opacity\x18\x05 \x01(\x0b\x32\x16.TSS.SpecDoubleArchive\x12\x19\n\x11opacity_undefined\x18\x06 \x01(\x08\x12&\n\x06shadow\x18\x07 \x01(\x0b\x32\x16.TSD.SpecShadowArchive\x12\x18\n\x10shadow_undefined\x18\x08 \x01(\x08\x12.\n\nreflection\x18\t \x01(\x0b\x32\x1a.TSD.SpecReflectionArchive\x12\x1c\n\x14reflection_undefined\x18\n \x01(\x08\x12.\n\rhead_line_end\x18\x0b \x01(\x0b\x32\x17.TSD.SpecLineEndArchive\x12\x1f\n\x17head_line_end_undefined\x18\x0c \x01(\x08\x12.\n\rtail_line_end\x18\r \x01(\x0b\x32\x17.TSD.SpecLineEndArchive\x12\x1f\n\x17tail_line_end_undefined\x18\x0e \x01(\x08\"\xba\x02\n\"MediaStylePropertyChangeSetArchive\x12&\n\x06stroke\x18\x01 \x01(\x0b\x32\x16.TSD.SpecStrokeArchive\x12\x18\n\x10stroke_undefined\x18\x02 \x01(\x08\x12\'\n\x07opacity\x18\x03 \x01(\x0b\x32\x16.TSS.SpecDoubleArchive\x12\x19\n\x11opacity_undefined\x18\x04 \x01(\x08\x12&\n\x06shadow\x18\x05 \x01(\x0b\x32\x16.TSD.SpecShadowArchive\x12\x18\n\x10shadow_undefined\x18\x06 \x01(\x08\x12.\n\nreflection\x18\x07 \x01(\x0b\x32\x1a.TSD.SpecReflectionArchive\x12\x1c\n\x14reflection_undefined\x18\x08 \x01(\x08')
  ,
  dependencies=[TSDArchives__pb2.DESCRIPTOR,TSSArchives__sos__pb2.DESCRIPTOR,])




_SPECSETFILLARCHIVE = _descriptor.Descriptor(
  name='SpecSetFillArchive',
  full_name='TSD.SpecSetFillArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fill', full_name='TSD.SpecSetFillArchive.fill', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unset', full_name='TSD.SpecSetFillArchive.unset', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=139,
)


_SPECSETLINEENDARCHIVE = _descriptor.Descriptor(
  name='SpecSetLineEndArchive',
  full_name='TSD.SpecSetLineEndArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='line_end', full_name='TSD.SpecSetLineEndArchive.line_end', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unset', full_name='TSD.SpecSetLineEndArchive.unset', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=218,
)


_SPECSETREFLECTIONARCHIVE = _descriptor.Descriptor(
  name='SpecSetReflectionArchive',
  full_name='TSD.SpecSetReflectionArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reflection', full_name='TSD.SpecSetReflectionArchive.reflection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unset', full_name='TSD.SpecSetReflectionArchive.unset', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=305,
)


_SPECSETSHADOWARCHIVE = _descriptor.Descriptor(
  name='SpecSetShadowArchive',
  full_name='TSD.SpecSetShadowArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shadow', full_name='TSD.SpecSetShadowArchive.shadow', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unset', full_name='TSD.SpecSetShadowArchive.unset', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=380,
)


_SPECSETSTROKEARCHIVE = _descriptor.Descriptor(
  name='SpecSetStrokeArchive',
  full_name='TSD.SpecSetStrokeArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stroke', full_name='TSD.SpecSetStrokeArchive.stroke', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unset', full_name='TSD.SpecSetStrokeArchive.unset', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=455,
)


_SPECFILLARCHIVE = _descriptor.Descriptor(
  name='SpecFillArchive',
  full_name='TSD.SpecFillArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec_color_fill_set_color', full_name='TSD.SpecFillArchive.spec_color_fill_set_color', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_gradient_fill_set_angle', full_name='TSD.SpecFillArchive.spec_gradient_fill_set_angle', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_image_fill_set_technique', full_name='TSD.SpecFillArchive.spec_image_fill_set_technique', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_set_fill', full_name='TSD.SpecFillArchive.spec_set_fill', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=458,
  serialized_end=747,
)


_SPECLINEENDARCHIVE = _descriptor.Descriptor(
  name='SpecLineEndArchive',
  full_name='TSD.SpecLineEndArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec_set_line_end', full_name='TSD.SpecLineEndArchive.spec_set_line_end', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=749,
  serialized_end=824,
)


_SPECREFLECTIONARCHIVE = _descriptor.Descriptor(
  name='SpecReflectionArchive',
  full_name='TSD.SpecReflectionArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec_reflection_set_opacity', full_name='TSD.SpecReflectionArchive.spec_reflection_set_opacity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_set_reflection', full_name='TSD.SpecReflectionArchive.spec_set_reflection', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=827,
  serialized_end=985,
)


_SPECSHADOWARCHIVE = _descriptor.Descriptor(
  name='SpecShadowArchive',
  full_name='TSD.SpecShadowArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec_set_shadow', full_name='TSD.SpecShadowArchive.spec_set_shadow', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_shadow_set_angle', full_name='TSD.SpecShadowArchive.spec_shadow_set_angle', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_shadow_set_color', full_name='TSD.SpecShadowArchive.spec_shadow_set_color', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_shadow_set_offset', full_name='TSD.SpecShadowArchive.spec_shadow_set_offset', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_shadow_set_opacity', full_name='TSD.SpecShadowArchive.spec_shadow_set_opacity', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_shadow_set_radius', full_name='TSD.SpecShadowArchive.spec_shadow_set_radius', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=988,
  serialized_end=1382,
)


_SPECSTROKEARCHIVE = _descriptor.Descriptor(
  name='SpecStrokeArchive',
  full_name='TSD.SpecStrokeArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec_frame_set_asset_scale', full_name='TSD.SpecStrokeArchive.spec_frame_set_asset_scale', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_set_stroke', full_name='TSD.SpecStrokeArchive.spec_set_stroke', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_stroke_set_color', full_name='TSD.SpecStrokeArchive.spec_stroke_set_color', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_stroke_set_pattern', full_name='TSD.SpecStrokeArchive.spec_stroke_set_pattern', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec_stroke_set_width', full_name='TSD.SpecStrokeArchive.spec_stroke_set_width', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1385,
  serialized_end=1721,
)


_BASESHAPESTYLEPROPERTYCHANGESETARCHIVE = _descriptor.Descriptor(
  name='BaseShapeStylePropertyChangeSetArchive',
  full_name='TSD.BaseShapeStylePropertyChangeSetArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fill', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.fill', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fill_undefined', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.fill_undefined', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stroke', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.stroke', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stroke_undefined', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.stroke_undefined', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opacity', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.opacity', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opacity_undefined', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.opacity_undefined', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shadow', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.shadow', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shadow_undefined', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.shadow_undefined', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reflection', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.reflection', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reflection_undefined', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.reflection_undefined', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head_line_end', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.head_line_end', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head_line_end_undefined', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.head_line_end_undefined', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tail_line_end', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.tail_line_end', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tail_line_end_undefined', full_name='TSD.BaseShapeStylePropertyChangeSetArchive.tail_line_end_undefined', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1724,
  serialized_end=2264,
)


_MEDIASTYLEPROPERTYCHANGESETARCHIVE = _descriptor.Descriptor(
  name='MediaStylePropertyChangeSetArchive',
  full_name='TSD.MediaStylePropertyChangeSetArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stroke', full_name='TSD.MediaStylePropertyChangeSetArchive.stroke', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stroke_undefined', full_name='TSD.MediaStylePropertyChangeSetArchive.stroke_undefined', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opacity', full_name='TSD.MediaStylePropertyChangeSetArchive.opacity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opacity_undefined', full_name='TSD.MediaStylePropertyChangeSetArchive.opacity_undefined', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shadow', full_name='TSD.MediaStylePropertyChangeSetArchive.shadow', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shadow_undefined', full_name='TSD.MediaStylePropertyChangeSetArchive.shadow_undefined', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reflection', full_name='TSD.MediaStylePropertyChangeSetArchive.reflection', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reflection_undefined', full_name='TSD.MediaStylePropertyChangeSetArchive.reflection_undefined', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2267,
  serialized_end=2581,
)

_SPECSETFILLARCHIVE.fields_by_name['fill'].message_type = TSDArchives__pb2._FILLARCHIVE
_SPECSETLINEENDARCHIVE.fields_by_name['line_end'].message_type = TSDArchives__pb2._LINEENDARCHIVE
_SPECSETREFLECTIONARCHIVE.fields_by_name['reflection'].message_type = TSDArchives__pb2._REFLECTIONARCHIVE
_SPECSETSHADOWARCHIVE.fields_by_name['shadow'].message_type = TSDArchives__pb2._SHADOWARCHIVE
_SPECSETSTROKEARCHIVE.fields_by_name['stroke'].message_type = TSDArchives__pb2._STROKEARCHIVE
_SPECFILLARCHIVE.fields_by_name['spec_color_fill_set_color'].message_type = TSDArchives__pb2._SPECCOLORFILLSETCOLORARCHIVE
_SPECFILLARCHIVE.fields_by_name['spec_gradient_fill_set_angle'].message_type = TSDArchives__pb2._SPECGRADIENTFILLSETANGLEARCHIVE
_SPECFILLARCHIVE.fields_by_name['spec_image_fill_set_technique'].message_type = TSDArchives__pb2._SPECIMAGEFILLSETTECHNIQUEARCHIVE
_SPECFILLARCHIVE.fields_by_name['spec_set_fill'].message_type = _SPECSETFILLARCHIVE
_SPECLINEENDARCHIVE.fields_by_name['spec_set_line_end'].message_type = _SPECSETLINEENDARCHIVE
_SPECREFLECTIONARCHIVE.fields_by_name['spec_reflection_set_opacity'].message_type = TSDArchives__pb2._SPECREFLECTIONSETOPACITYARCHIVE
_SPECREFLECTIONARCHIVE.fields_by_name['spec_set_reflection'].message_type = _SPECSETREFLECTIONARCHIVE
_SPECSHADOWARCHIVE.fields_by_name['spec_set_shadow'].message_type = _SPECSETSHADOWARCHIVE
_SPECSHADOWARCHIVE.fields_by_name['spec_shadow_set_angle'].message_type = TSDArchives__pb2._SPECSHADOWSETANGLEARCHIVE
_SPECSHADOWARCHIVE.fields_by_name['spec_shadow_set_color'].message_type = TSDArchives__pb2._SPECSHADOWSETCOLORARCHIVE
_SPECSHADOWARCHIVE.fields_by_name['spec_shadow_set_offset'].message_type = TSDArchives__pb2._SPECSHADOWSETOFFSETARCHIVE
_SPECSHADOWARCHIVE.fields_by_name['spec_shadow_set_opacity'].message_type = TSDArchives__pb2._SPECSHADOWSETOPACITYARCHIVE
_SPECSHADOWARCHIVE.fields_by_name['spec_shadow_set_radius'].message_type = TSDArchives__pb2._SPECSHADOWSETRADIUSARCHIVE
_SPECSTROKEARCHIVE.fields_by_name['spec_frame_set_asset_scale'].message_type = TSDArchives__pb2._SPECFRAMESETASSETSCALEARCHIVE
_SPECSTROKEARCHIVE.fields_by_name['spec_set_stroke'].message_type = _SPECSETSTROKEARCHIVE
_SPECSTROKEARCHIVE.fields_by_name['spec_stroke_set_color'].message_type = TSDArchives__pb2._SPECSTROKESETCOLORARCHIVE
_SPECSTROKEARCHIVE.fields_by_name['spec_stroke_set_pattern'].message_type = TSDArchives__pb2._SPECSTROKESETPATTERNARCHIVE
_SPECSTROKEARCHIVE.fields_by_name['spec_stroke_set_width'].message_type = TSDArchives__pb2._SPECSTROKESETWIDTHARCHIVE
_BASESHAPESTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['fill'].message_type = _SPECFILLARCHIVE
_BASESHAPESTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['stroke'].message_type = _SPECSTROKEARCHIVE
_BASESHAPESTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['opacity'].message_type = TSSArchives__sos__pb2._SPECDOUBLEARCHIVE
_BASESHAPESTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['shadow'].message_type = _SPECSHADOWARCHIVE
_BASESHAPESTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['reflection'].message_type = _SPECREFLECTIONARCHIVE
_BASESHAPESTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['head_line_end'].message_type = _SPECLINEENDARCHIVE
_BASESHAPESTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['tail_line_end'].message_type = _SPECLINEENDARCHIVE
_MEDIASTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['stroke'].message_type = _SPECSTROKEARCHIVE
_MEDIASTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['opacity'].message_type = TSSArchives__sos__pb2._SPECDOUBLEARCHIVE
_MEDIASTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['shadow'].message_type = _SPECSHADOWARCHIVE
_MEDIASTYLEPROPERTYCHANGESETARCHIVE.fields_by_name['reflection'].message_type = _SPECREFLECTIONARCHIVE
DESCRIPTOR.message_types_by_name['SpecSetFillArchive'] = _SPECSETFILLARCHIVE
DESCRIPTOR.message_types_by_name['SpecSetLineEndArchive'] = _SPECSETLINEENDARCHIVE
DESCRIPTOR.message_types_by_name['SpecSetReflectionArchive'] = _SPECSETREFLECTIONARCHIVE
DESCRIPTOR.message_types_by_name['SpecSetShadowArchive'] = _SPECSETSHADOWARCHIVE
DESCRIPTOR.message_types_by_name['SpecSetStrokeArchive'] = _SPECSETSTROKEARCHIVE
DESCRIPTOR.message_types_by_name['SpecFillArchive'] = _SPECFILLARCHIVE
DESCRIPTOR.message_types_by_name['SpecLineEndArchive'] = _SPECLINEENDARCHIVE
DESCRIPTOR.message_types_by_name['SpecReflectionArchive'] = _SPECREFLECTIONARCHIVE
DESCRIPTOR.message_types_by_name['SpecShadowArchive'] = _SPECSHADOWARCHIVE
DESCRIPTOR.message_types_by_name['SpecStrokeArchive'] = _SPECSTROKEARCHIVE
DESCRIPTOR.message_types_by_name['BaseShapeStylePropertyChangeSetArchive'] = _BASESHAPESTYLEPROPERTYCHANGESETARCHIVE
DESCRIPTOR.message_types_by_name['MediaStylePropertyChangeSetArchive'] = _MEDIASTYLEPROPERTYCHANGESETARCHIVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpecSetFillArchive = _reflection.GeneratedProtocolMessageType('SpecSetFillArchive', (_message.Message,), dict(
  DESCRIPTOR = _SPECSETFILLARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.SpecSetFillArchive)
  ))
_sym_db.RegisterMessage(SpecSetFillArchive)

SpecSetLineEndArchive = _reflection.GeneratedProtocolMessageType('SpecSetLineEndArchive', (_message.Message,), dict(
  DESCRIPTOR = _SPECSETLINEENDARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.SpecSetLineEndArchive)
  ))
_sym_db.RegisterMessage(SpecSetLineEndArchive)

SpecSetReflectionArchive = _reflection.GeneratedProtocolMessageType('SpecSetReflectionArchive', (_message.Message,), dict(
  DESCRIPTOR = _SPECSETREFLECTIONARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.SpecSetReflectionArchive)
  ))
_sym_db.RegisterMessage(SpecSetReflectionArchive)

SpecSetShadowArchive = _reflection.GeneratedProtocolMessageType('SpecSetShadowArchive', (_message.Message,), dict(
  DESCRIPTOR = _SPECSETSHADOWARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.SpecSetShadowArchive)
  ))
_sym_db.RegisterMessage(SpecSetShadowArchive)

SpecSetStrokeArchive = _reflection.GeneratedProtocolMessageType('SpecSetStrokeArchive', (_message.Message,), dict(
  DESCRIPTOR = _SPECSETSTROKEARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.SpecSetStrokeArchive)
  ))
_sym_db.RegisterMessage(SpecSetStrokeArchive)

SpecFillArchive = _reflection.GeneratedProtocolMessageType('SpecFillArchive', (_message.Message,), dict(
  DESCRIPTOR = _SPECFILLARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.SpecFillArchive)
  ))
_sym_db.RegisterMessage(SpecFillArchive)

SpecLineEndArchive = _reflection.GeneratedProtocolMessageType('SpecLineEndArchive', (_message.Message,), dict(
  DESCRIPTOR = _SPECLINEENDARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.SpecLineEndArchive)
  ))
_sym_db.RegisterMessage(SpecLineEndArchive)

SpecReflectionArchive = _reflection.GeneratedProtocolMessageType('SpecReflectionArchive', (_message.Message,), dict(
  DESCRIPTOR = _SPECREFLECTIONARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.SpecReflectionArchive)
  ))
_sym_db.RegisterMessage(SpecReflectionArchive)

SpecShadowArchive = _reflection.GeneratedProtocolMessageType('SpecShadowArchive', (_message.Message,), dict(
  DESCRIPTOR = _SPECSHADOWARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.SpecShadowArchive)
  ))
_sym_db.RegisterMessage(SpecShadowArchive)

SpecStrokeArchive = _reflection.GeneratedProtocolMessageType('SpecStrokeArchive', (_message.Message,), dict(
  DESCRIPTOR = _SPECSTROKEARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.SpecStrokeArchive)
  ))
_sym_db.RegisterMessage(SpecStrokeArchive)

BaseShapeStylePropertyChangeSetArchive = _reflection.GeneratedProtocolMessageType('BaseShapeStylePropertyChangeSetArchive', (_message.Message,), dict(
  DESCRIPTOR = _BASESHAPESTYLEPROPERTYCHANGESETARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.BaseShapeStylePropertyChangeSetArchive)
  ))
_sym_db.RegisterMessage(BaseShapeStylePropertyChangeSetArchive)

MediaStylePropertyChangeSetArchive = _reflection.GeneratedProtocolMessageType('MediaStylePropertyChangeSetArchive', (_message.Message,), dict(
  DESCRIPTOR = _MEDIASTYLEPROPERTYCHANGESETARCHIVE,
  __module__ = 'TSDArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSD.MediaStylePropertyChangeSetArchive)
  ))
_sym_db.RegisterMessage(MediaStylePropertyChangeSetArchive)


# @@protoc_insertion_point(module_scope)
