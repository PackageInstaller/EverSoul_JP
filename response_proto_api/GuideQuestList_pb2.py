# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: GuideQuestList.proto
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
    'GuideQuestList.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14GuideQuestList.proto\x12\x04\x45sPb\"f\n\x0eGuideQuestList\x12%\n\nguideQuest\x18\x01 \x03(\x0b\x32\x11.EsPb.sGuideQuest\x12\x16\n\x0e\x63ompleteNoList\x18\x02 \x03(\x05\x12\x15\n\rreceiveNoList\x18\x03 \x03(\x05\"-\n\x0bsGuideQuest\x12\x0f\n\x07questNo\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GuideQuestList_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GUIDEQUESTLIST']._serialized_start=30
  _globals['_GUIDEQUESTLIST']._serialized_end=132
  _globals['_SGUIDEQUEST']._serialized_start=134
  _globals['_SGUIDEQUEST']._serialized_end=179
# @@protoc_insertion_point(module_scope)
