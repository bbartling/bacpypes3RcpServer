# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pingpong.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epingpong.proto\x12\x08pingpong\"\x1b\n\x0bPingRequest\x12\x0c\n\x04ping\x18\x01 \x01(\t\"\x19\n\tPongReply\x12\x0c\n\x04pong\x18\x01 \x01(\t2@\n\x08PingPong\x12\x34\n\x04Ping\x12\x15.pingpong.PingRequest\x1a\x13.pingpong.PongReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pingpong_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PINGREQUEST']._serialized_start=28
  _globals['_PINGREQUEST']._serialized_end=55
  _globals['_PONGREPLY']._serialized_start=57
  _globals['_PONGREPLY']._serialized_end=82
  _globals['_PINGPONG']._serialized_start=84
  _globals['_PINGPONG']._serialized_end=148
# @@protoc_insertion_point(module_scope)