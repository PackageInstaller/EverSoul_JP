# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ChallengeModeClear.proto
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
    'ChallengeModeClear.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x43hallengeModeClear.proto\x12\x05ReqPb\"\xe6\x01\n\x12\x43hallengeModeClear\x12\x14\n\x0c\x63learStageNo\x18\x01 \x01(\x05\x12\x12\n\naliveCount\x18\x02 \x01(\x05\x12\x35\n\x10heroIdxKillCount\x18\x03 \x03(\x0b\x32\x1b.ReqPb.sHeroIdxAndKillCount\x12\x18\n\x10useUltimateCount\x18\x04 \x01(\x05\x12\x1b\n\x13useActiveSkillCount\x18\x05 \x01(\x05\x12\x15\n\rformationType\x18\x06 \x03(\x05\x12!\n\x08stageLog\x18\x07 \x03(\x0b\x32\x0f.ReqPb.stageLog\":\n\x14sHeroIdxAndKillCount\x12\x0f\n\x07heroIdx\x18\x01 \x01(\t\x12\x11\n\tkillCount\x18\x02 \x01(\x05\"\x93\x01\n\x08stageLog\x12\x0e\n\x06\x61ttack\x18\x01 \x01(\x05\x12\x0e\n\x06\x64\x61mage\x18\x02 \x01(\x05\x12\x10\n\x08recovery\x18\x03 \x01(\x05\x12\x1c\n\x05skill\x18\x04 \x03(\x0b\x32\r.ReqPb.sSkill\x12\x0e\n\x06heroNo\x18\x05 \x01(\x05\x12\x0f\n\x07heroIdx\x18\x06 \x01(\t\x12\x16\n\x0e\x66ormationIndex\x18\x07 \x01(\x05\"/\n\x06sSkill\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\n\n\x02no\x18\x02 \x01(\x05\x12\x0b\n\x03\x63nt\x18\x03 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ChallengeModeClear_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHALLENGEMODECLEAR']._serialized_start=36
  _globals['_CHALLENGEMODECLEAR']._serialized_end=266
  _globals['_SHEROIDXANDKILLCOUNT']._serialized_start=268
  _globals['_SHEROIDXANDKILLCOUNT']._serialized_end=326
  _globals['_STAGELOG']._serialized_start=329
  _globals['_STAGELOG']._serialized_end=476
  _globals['_SSKILL']._serialized_start=478
  _globals['_SSKILL']._serialized_end=525
# @@protoc_insertion_point(module_scope)
