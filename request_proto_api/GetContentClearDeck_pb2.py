# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: GetContentClearDeck.proto
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
    'GetContentClearDeck.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19GetContentClearDeck.proto\x12\x05ReqPb\"W\n\x13GetContentClearDeck\x12-\n\x0b\x63ontentType\x18\x01 \x01(\x0e\x32\x18.ReqPb.eContentClearType\x12\x11\n\tcontentNo\x18\x02 \x01(\x05*\x83\x01\n\x11\x65\x43ontentClearType\x12\t\n\x05Stage\x10\x00\x12\x14\n\x10\x46reedomGateClear\x10\x01\x12\x12\n\x0eHumanGateClear\x10\x02\x12\x12\n\x0e\x46urryGateClear\x10\x03\x12\x10\n\x0c\x45lfGateClear\x10\x04\x12\x13\n\x0fUndeadGateClear\x10\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetContentClearDeck_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ECONTENTCLEARTYPE']._serialized_start=126
  _globals['_ECONTENTCLEARTYPE']._serialized_end=257
  _globals['_GETCONTENTCLEARDECK']._serialized_start=36
  _globals['_GETCONTENTCLEARDECK']._serialized_end=123
# @@protoc_insertion_point(module_scope)
