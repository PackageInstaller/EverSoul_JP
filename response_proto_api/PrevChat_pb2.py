# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: PrevChat.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'PrevChat.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ePrevChat.proto\x12\x04\x45sPb\"%\n\x08PrevChat\x12\x19\n\x04\x63hat\x18\x01 \x03(\x0b\x32\x0b.EsPb.sChat\"w\n\x05sChat\x12!\n\x08userInfo\x18\x01 \x01(\x0b\x32\x0f.EsPb.tUserInfo\x12\x0f\n\x07message\x18\x02 \x01(\t\x12.\n\x0bmessageType\x18\x03 \x01(\x0e\x32\x19.EsPb.E_CHAT_MESSAGE_TYPE\x12\n\n\x02\x64t\x18\x04 \x01(\x03\"w\n\ttUserInfo\x12\x0e\n\x06\x63ookie\x18\x01 \x01(\t\x12\x0f\n\x07userIdx\x18\x02 \x01(\t\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12#\n\tthumbnail\x18\x04 \x01(\x0b\x32\x10.EsPb.sThumbnail\x12\x12\n\nguildGrade\x18\x05 \x01(\x03\"b\n\nsThumbnail\x12\x16\n\x0ethumbnailFrame\x18\x01 \x01(\x05\x12\x16\n\x0ethumbnailImage\x18\x02 \x01(\x05\x12\x11\n\tuseCustom\x18\x03 \x01(\x08\x12\x11\n\tthumbnail\x18\x04 \x01(\x0c*N\n\x13\x45_CHAT_MESSAGE_TYPE\x12\x0e\n\nCommonChat\x10\x00\x12\x0c\n\x08\x45moticon\x10\x01\x12\x19\n\x15SystemGuildNameChange\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PrevChat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_E_CHAT_MESSAGE_TYPE']._serialized_start=405
  _globals['_E_CHAT_MESSAGE_TYPE']._serialized_end=483
  _globals['_PREVCHAT']._serialized_start=24
  _globals['_PREVCHAT']._serialized_end=61
  _globals['_SCHAT']._serialized_start=63
  _globals['_SCHAT']._serialized_end=182
  _globals['_TUSERINFO']._serialized_start=184
  _globals['_TUSERINFO']._serialized_end=303
  _globals['_STHUMBNAIL']._serialized_start=305
  _globals['_STHUMBNAIL']._serialized_end=403
# @@protoc_insertion_point(module_scope)
