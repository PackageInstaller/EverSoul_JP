# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: DungeonLoad.proto
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
    'DungeonLoad.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x44ungeonLoad.proto\x12\x04\x45sPb\"[\n\x0b\x44ungeonLoad\x12\x1f\n\x07\x64ungeon\x18\x01 \x01(\x0b\x32\x0e.EsPb.sDungeon\x12+\n\rdungeonReward\x18\x02 \x03(\x0b\x32\x14.EsPb.sDungeonReward\"\x8e\x04\n\x08sDungeon\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tdungeonNo\x18\x02 \x01(\x05\x12\x14\n\x0c\x64ungeonLevel\x18\x03 \x01(\x05\x12\t\n\x01x\x18\x04 \x01(\x02\x12\t\n\x01z\x18\x05 \x01(\x02\x12\x0f\n\x07mapInfo\x18\x06 \x01(\x0c\x12\x15\n\rconditionInfo\x18\x07 \x01(\x0c\x12\x10\n\x08heroInfo\x18\x08 \x01(\x0c\x12\x16\n\x0e\x61\x64\x64itionalInfo\x18\t \x01(\x0c\x12\x11\n\trelicInfo\x18\n \x01(\x0c\x12\x0f\n\x07isEnter\x18\x0b \x01(\x05\x12\x0f\n\x07isClear\x18\x0c \x01(\x05\x12\x14\n\x0cisFirstClear\x18\r \x01(\x05\x12\x11\n\tmissionNo\x18\x0e \x01(\x05\x12\x12\n\nmissionCnt\x18\x0f \x01(\x05\x12\x0c\n\x04seed\x18\x10 \x01(\x05\x12\x13\n\x0b\x64ungeonItem\x18\x11 \x01(\x0c\x12\x12\n\ndifficulty\x18\x12 \x01(\x05\x12\x15\n\rultimatePoint\x18\x13 \x01(\x05\x12\x16\n\x0eplayerObjectId\x18\x14 \x01(\x05\x12\x11\n\tuseTicket\x18\x15 \x01(\x08\x12\x15\n\rmaxClearLevel\x18\x16 \x01(\x05\x12\x0f\n\x07isSweep\x18\x17 \x01(\x05\x12\x16\n\x0eisPerfectClear\x18\x18 \x01(\x05\x12\x1f\n\x17isHiddenKeyNotAvailable\x18\x19 \x01(\x05\x12\x19\n\x11randomGimmickSeed\x18\x1a \x01(\x05\"J\n\x0esDungeonReward\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.EsPb.eDungeonRewardType\x12\x10\n\x08rewardNo\x18\x02 \x01(\x05*\\\n\x12\x65\x44ungeonRewardType\x12\x15\n\x11NoneDungeonReward\x10\x00\x12\x0b\n\x07Mission\x10\x01\x12\n\n\x06Object\x10\x02\x12\x0b\n\x07Monster\x10\x03\x12\t\n\x05\x43hest\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DungeonLoad_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EDUNGEONREWARDTYPE']._serialized_start=725
  _globals['_EDUNGEONREWARDTYPE']._serialized_end=817
  _globals['_DUNGEONLOAD']._serialized_start=27
  _globals['_DUNGEONLOAD']._serialized_end=118
  _globals['_SDUNGEON']._serialized_start=121
  _globals['_SDUNGEON']._serialized_end=647
  _globals['_SDUNGEONREWARD']._serialized_start=649
  _globals['_SDUNGEONREWARD']._serialized_end=723
# @@protoc_insertion_point(module_scope)
