# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: SignatureUnEquip.proto
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
    'SignatureUnEquip.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16SignatureUnEquip.proto\x12\x04\x45sPb\"7\n\x10SignatureUnEquip\x12#\n\theroEquip\x18\x01 \x01(\x0b\x32\x10.EsPb.sHeroEquip\"C\n\nsHeroEquip\x12\x0f\n\x07heroIdx\x18\x01 \x01(\t\x12$\n\x05\x65quip\x18\x02 \x01(\x0b\x32\x15.EsPb.sSlotAndEquipId\"4\n\x0fsSlotAndEquipId\x12\x0c\n\x04slot\x18\x01 \x01(\x05\x12\x13\n\x0bitemEquipId\x18\x02 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SignatureUnEquip_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SIGNATUREUNEQUIP']._serialized_start=32
  _globals['_SIGNATUREUNEQUIP']._serialized_end=87
  _globals['_SHEROEQUIP']._serialized_start=89
  _globals['_SHEROEQUIP']._serialized_end=156
  _globals['_SSLOTANDEQUIPID']._serialized_start=158
  _globals['_SSLOTANDEQUIPID']._serialized_end=210
# @@protoc_insertion_point(module_scope)
