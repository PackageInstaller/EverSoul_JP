# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: EventSingleRaidInfo.proto
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
    'EventSingleRaidInfo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x45ventSingleRaidInfo.proto\x12\x04\x45sPb\"F\n\x13\x45ventSingleRaidInfo\x12/\n\x0f\x65ventSingleRaid\x18\x01 \x03(\x0b\x32\x16.EsPb.sEventSingleRaid\"\x90\x01\n\x10sEventSingleRaid\x12\x12\n\neventGroup\x18\x01 \x01(\x05\x12\x13\n\x0b\x65ventNumber\x18\x02 \x01(\x05\x12\x10\n\x08\x65nterCnt\x18\x03 \x01(\x05\x12\x10\n\x08maxLevel\x18\x04 \x01(\x05\x12\x1a\n\x12maxLevelLastReward\x18\x05 \x01(\x05\x12\x13\n\x0b\x64iaUseCount\x18\x06 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'EventSingleRaidInfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENTSINGLERAIDINFO']._serialized_start=35
  _globals['_EVENTSINGLERAIDINFO']._serialized_end=105
  _globals['_SEVENTSINGLERAID']._serialized_start=108
  _globals['_SEVENTSINGLERAID']._serialized_end=252
# @@protoc_insertion_point(module_scope)
