# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rService.proto\"(\n\x08Question\x12\x12\n\x05value\x18\x01 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_value\"%\n\x05Reply\x12\x12\n\x05value\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\x08\n\x06_value2+\n\nCalculator\x12\x1d\n\x06isEven\x12\t.Question\x1a\x06.Reply\"\x00\x62\x06proto3')



_QUESTION = DESCRIPTOR.message_types_by_name['Question']
_REPLY = DESCRIPTOR.message_types_by_name['Reply']
Question = _reflection.GeneratedProtocolMessageType('Question', (_message.Message,), {
  'DESCRIPTOR' : _QUESTION,
  '__module__' : 'Service_pb2'
  # @@protoc_insertion_point(class_scope:Question)
  })
_sym_db.RegisterMessage(Question)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'Service_pb2'
  # @@protoc_insertion_point(class_scope:Reply)
  })
_sym_db.RegisterMessage(Reply)

_CALCULATOR = DESCRIPTOR.services_by_name['Calculator']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUESTION._serialized_start=17
  _QUESTION._serialized_end=57
  _REPLY._serialized_start=59
  _REPLY._serialized_end=96
  _CALCULATOR._serialized_start=98
  _CALCULATOR._serialized_end=141
# @@protoc_insertion_point(module_scope)
