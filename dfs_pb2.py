# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dfs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dfs.proto',
  package='dfs',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tdfs.proto\x12\x03\x64\x66s\")\n\x0cWriteRequest\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"-\n\x0eSegmentRequest\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x0e\n\x06\x63hunks\x18\x02 \x03(\t\"\x1a\n\nStringList\x12\x0c\n\x04strs\x18\x01 \x03(\t\"\x15\n\x05\x42ytes\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x15\n\x06String\x12\x0b\n\x03str\x18\x01 \x01(\t\"\x16\n\x04\x42ool\x12\x0e\n\x06verify\x18\x01 \x01(\x08\"\x07\n\x05\x45mpty2\xa2\x01\n\x0b\x43hunkServer\x12\x1f\n\x04Read\x12\x0b.dfs.String\x1a\n.dfs.Bytes\x12%\n\x05Write\x12\x11.dfs.WriteRequest\x1a\t.dfs.Bool\x12!\n\x06\x44\x65lete\x12\x0b.dfs.String\x1a\n.dfs.Empty\x12(\n\tGetChunks\x12\n.dfs.Empty\x1a\x0f.dfs.StringList2\xc3\x01\n\x0cMasterServer\x12\'\n\x0cRegisterPeer\x12\x0b.dfs.String\x1a\n.dfs.Empty\x12,\n\x0cGetLocations\x12\x0b.dfs.String\x1a\x0f.dfs.StringList\x12(\n\rDeleteSegment\x12\x0b.dfs.String\x1a\n.dfs.Empty\x12\x32\n\nAddSegment\x12\x13.dfs.SegmentRequest\x1a\x0f.dfs.StringListb\x06proto3'
)




_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='dfs.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cid', full_name='dfs.WriteRequest.cid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='dfs.WriteRequest.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=59,
)


_SEGMENTREQUEST = _descriptor.Descriptor(
  name='SegmentRequest',
  full_name='dfs.SegmentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sid', full_name='dfs.SegmentRequest.sid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chunks', full_name='dfs.SegmentRequest.chunks', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=106,
)


_STRINGLIST = _descriptor.Descriptor(
  name='StringList',
  full_name='dfs.StringList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='strs', full_name='dfs.StringList.strs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=134,
)


_BYTES = _descriptor.Descriptor(
  name='Bytes',
  full_name='dfs.Bytes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='dfs.Bytes.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=157,
)


_STRING = _descriptor.Descriptor(
  name='String',
  full_name='dfs.String',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='str', full_name='dfs.String.str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=180,
)


_BOOL = _descriptor.Descriptor(
  name='Bool',
  full_name='dfs.Bool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='verify', full_name='dfs.Bool.verify', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=204,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='dfs.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=213,
)

DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['SegmentRequest'] = _SEGMENTREQUEST
DESCRIPTOR.message_types_by_name['StringList'] = _STRINGLIST
DESCRIPTOR.message_types_by_name['Bytes'] = _BYTES
DESCRIPTOR.message_types_by_name['String'] = _STRING
DESCRIPTOR.message_types_by_name['Bool'] = _BOOL
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)

SegmentRequest = _reflection.GeneratedProtocolMessageType('SegmentRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEGMENTREQUEST,
  '__module__' : 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.SegmentRequest)
  })
_sym_db.RegisterMessage(SegmentRequest)

StringList = _reflection.GeneratedProtocolMessageType('StringList', (_message.Message,), {
  'DESCRIPTOR' : _STRINGLIST,
  '__module__' : 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.StringList)
  })
_sym_db.RegisterMessage(StringList)

Bytes = _reflection.GeneratedProtocolMessageType('Bytes', (_message.Message,), {
  'DESCRIPTOR' : _BYTES,
  '__module__' : 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.Bytes)
  })
_sym_db.RegisterMessage(Bytes)

String = _reflection.GeneratedProtocolMessageType('String', (_message.Message,), {
  'DESCRIPTOR' : _STRING,
  '__module__' : 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.String)
  })
_sym_db.RegisterMessage(String)

Bool = _reflection.GeneratedProtocolMessageType('Bool', (_message.Message,), {
  'DESCRIPTOR' : _BOOL,
  '__module__' : 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.Bool)
  })
_sym_db.RegisterMessage(Bool)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'dfs_pb2'
  # @@protoc_insertion_point(class_scope:dfs.Empty)
  })
_sym_db.RegisterMessage(Empty)



_CHUNKSERVER = _descriptor.ServiceDescriptor(
  name='ChunkServer',
  full_name='dfs.ChunkServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=216,
  serialized_end=378,
  methods=[
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='dfs.ChunkServer.Read',
    index=0,
    containing_service=None,
    input_type=_STRING,
    output_type=_BYTES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='dfs.ChunkServer.Write',
    index=1,
    containing_service=None,
    input_type=_WRITEREQUEST,
    output_type=_BOOL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='dfs.ChunkServer.Delete',
    index=2,
    containing_service=None,
    input_type=_STRING,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetChunks',
    full_name='dfs.ChunkServer.GetChunks',
    index=3,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_STRINGLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHUNKSERVER)

DESCRIPTOR.services_by_name['ChunkServer'] = _CHUNKSERVER


_MASTERSERVER = _descriptor.ServiceDescriptor(
  name='MasterServer',
  full_name='dfs.MasterServer',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=381,
  serialized_end=576,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterPeer',
    full_name='dfs.MasterServer.RegisterPeer',
    index=0,
    containing_service=None,
    input_type=_STRING,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLocations',
    full_name='dfs.MasterServer.GetLocations',
    index=1,
    containing_service=None,
    input_type=_STRING,
    output_type=_STRINGLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSegment',
    full_name='dfs.MasterServer.DeleteSegment',
    index=2,
    containing_service=None,
    input_type=_STRING,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddSegment',
    full_name='dfs.MasterServer.AddSegment',
    index=3,
    containing_service=None,
    input_type=_SEGMENTREQUEST,
    output_type=_STRINGLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MASTERSERVER)

DESCRIPTOR.services_by_name['MasterServer'] = _MASTERSERVER

# @@protoc_insertion_point(module_scope)
