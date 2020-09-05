from __future__ import absolute_import
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TSAArchives_sos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import TSPMessages_pb2 as TSPMessages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TSAArchives_sos.proto',
  package='TSA',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x15TSAArchives_sos.proto\x12\x03TSA\x1a\x11TSPMessages.proto\"\x85\x01\n\x19\x44rawableZOrderListArchive\x12\x1f\n\x0c\x63ontainer_id\x18\x01 \x01(\x0b\x32\t.TSP.UUID\x12#\n\x10\x64rawable_id_list\x18\x02 \x03(\x0b\x32\t.TSP.UUID\x12\"\n\x1a\x64rawable_id_list_undefined\x18\x03 \x01(\x08')
  ,
  dependencies=[TSPMessages__pb2.DESCRIPTOR,])




_DRAWABLEZORDERLISTARCHIVE = _descriptor.Descriptor(
  name='DrawableZOrderListArchive',
  full_name='TSA.DrawableZOrderListArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='TSA.DrawableZOrderListArchive.container_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drawable_id_list', full_name='TSA.DrawableZOrderListArchive.drawable_id_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drawable_id_list_undefined', full_name='TSA.DrawableZOrderListArchive.drawable_id_list_undefined', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=50,
  serialized_end=183,
)

_DRAWABLEZORDERLISTARCHIVE.fields_by_name['container_id'].message_type = TSPMessages__pb2._UUID
_DRAWABLEZORDERLISTARCHIVE.fields_by_name['drawable_id_list'].message_type = TSPMessages__pb2._UUID
DESCRIPTOR.message_types_by_name['DrawableZOrderListArchive'] = _DRAWABLEZORDERLISTARCHIVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DrawableZOrderListArchive = _reflection.GeneratedProtocolMessageType('DrawableZOrderListArchive', (_message.Message,), dict(
  DESCRIPTOR = _DRAWABLEZORDERLISTARCHIVE,
  __module__ = 'TSAArchives_sos_pb2'
  # @@protoc_insertion_point(class_scope:TSA.DrawableZOrderListArchive)
  ))
_sym_db.RegisterMessage(DrawableZOrderListArchive)


# @@protoc_insertion_point(module_scope)
