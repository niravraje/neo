# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: registry.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='registry.proto',
  package='registry',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eregistry.proto\x12\x08registry\"*\n\x0bHistoryArgs\x12\x0c\n\x04page\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"G\n\x06Widget\x12\x0f\n\x07station\x18\x01 \x01(\t\x12\x0f\n\x07\x66\x65\x61ture\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\" \n\x0eSuccessMessage\x12\x0e\n\x06status\x18\x01 \x01(\x08\"R\n\x07History\x12\x0f\n\x07history\x18\x01 \x01(\t\x12\x12\n\ntotalPages\x18\x02 \x01(\t\x12\x13\n\x0b\x63urrentPage\x18\x03 \x01(\t\x12\r\n\x05\x65xist\x18\x04 \x01(\x08\x32\x80\x01\n\x08Registry\x12<\n\x0eregisterWidget\x12\x10.registry.Widget\x1a\x18.registry.SuccessMessage\x12\x36\n\ngetHistory\x12\x15.registry.HistoryArgs\x1a\x11.registry.Historyb\x06proto3'
)




_HISTORYARGS = _descriptor.Descriptor(
  name='HistoryArgs',
  full_name='registry.HistoryArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='registry.HistoryArgs.page', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='registry.HistoryArgs.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=28,
  serialized_end=70,
)


_WIDGET = _descriptor.Descriptor(
  name='Widget',
  full_name='registry.Widget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='station', full_name='registry.Widget.station', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feature', full_name='registry.Widget.feature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='registry.Widget.date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='registry.Widget.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=72,
  serialized_end=143,
)


_SUCCESSMESSAGE = _descriptor.Descriptor(
  name='SuccessMessage',
  full_name='registry.SuccessMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='registry.SuccessMessage.status', index=0,
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
  serialized_start=145,
  serialized_end=177,
)


_HISTORY = _descriptor.Descriptor(
  name='History',
  full_name='registry.History',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='history', full_name='registry.History.history', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalPages', full_name='registry.History.totalPages', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currentPage', full_name='registry.History.currentPage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exist', full_name='registry.History.exist', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=179,
  serialized_end=261,
)

DESCRIPTOR.message_types_by_name['HistoryArgs'] = _HISTORYARGS
DESCRIPTOR.message_types_by_name['Widget'] = _WIDGET
DESCRIPTOR.message_types_by_name['SuccessMessage'] = _SUCCESSMESSAGE
DESCRIPTOR.message_types_by_name['History'] = _HISTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HistoryArgs = _reflection.GeneratedProtocolMessageType('HistoryArgs', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYARGS,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.HistoryArgs)
  })
_sym_db.RegisterMessage(HistoryArgs)

Widget = _reflection.GeneratedProtocolMessageType('Widget', (_message.Message,), {
  'DESCRIPTOR' : _WIDGET,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.Widget)
  })
_sym_db.RegisterMessage(Widget)

SuccessMessage = _reflection.GeneratedProtocolMessageType('SuccessMessage', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESSMESSAGE,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.SuccessMessage)
  })
_sym_db.RegisterMessage(SuccessMessage)

History = _reflection.GeneratedProtocolMessageType('History', (_message.Message,), {
  'DESCRIPTOR' : _HISTORY,
  '__module__' : 'registry_pb2'
  # @@protoc_insertion_point(class_scope:registry.History)
  })
_sym_db.RegisterMessage(History)



_REGISTRY = _descriptor.ServiceDescriptor(
  name='Registry',
  full_name='registry.Registry',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=264,
  serialized_end=392,
  methods=[
  _descriptor.MethodDescriptor(
    name='registerWidget',
    full_name='registry.Registry.registerWidget',
    index=0,
    containing_service=None,
    input_type=_WIDGET,
    output_type=_SUCCESSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getHistory',
    full_name='registry.Registry.getHistory',
    index=1,
    containing_service=None,
    input_type=_HISTORYARGS,
    output_type=_HISTORY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REGISTRY)

DESCRIPTOR.services_by_name['Registry'] = _REGISTRY

# @@protoc_insertion_point(module_scope)
