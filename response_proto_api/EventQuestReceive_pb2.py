# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: EventQuestReceive.proto
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
    'EventQuestReceive.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x45ventQuestReceive.proto\x12\x04\x45sPb\"\xc5\x01\n\x11\x45ventQuestReceive\x12\x1b\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x0c.EsPb.sEvent\x12\'\n\x0b\x65ventResult\x18\x02 \x01(\x0b\x32\x12.EsPb.sEventResult\x12$\n\x08\x63urrency\x18\x03 \x01(\x0b\x32\x12.EsPb.sCurrencyAll\x12#\n\titemEquip\x18\x04 \x03(\x0b\x32\x10.EsPb.sItemEquip\x12\x1f\n\x07itemEtc\x18\x05 \x03(\x0b\x32\x0e.EsPb.sItemEtc\"l\n\x06sEvent\x12\x11\n\teventType\x18\x01 \x01(\x05\x12\r\n\x05group\x18\x02 \x01(\x05\x12\x13\n\x0b\x65ventNumber\x18\x03 \x01(\x05\x12\x10\n\x08\x62\x65havior\x18\x04 \x01(\x05\x12\r\n\x05value\x18\x05 \x01(\x05\x12\n\n\x02no\x18\x06 \x01(\x05\"s\n\x0csEventResult\x12\x11\n\teventType\x18\x01 \x01(\x05\x12\r\n\x05group\x18\x02 \x01(\x05\x12\x13\n\x0b\x65ventNumber\x18\x03 \x01(\x05\x12\r\n\x05subNo\x18\x04 \x01(\x05\x12\x11\n\tisReceive\x18\x05 \x01(\x05\x12\n\n\x02\x64t\x18\x06 \x01(\x03\"4\n\x0csCurrencyAll\x12$\n\x0b\x61llCurrency\x18\x01 \x03(\x0b\x32\x0f.EsPb.sCurrency\":\n\tsCurrency\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.EsPb.E_CURRENCY\x12\r\n\x05value\x18\x02 \x01(\x03\"5\n\nsItemEquip\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06itemNo\x18\x02 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x01(\x05\"\'\n\x08sItemEtc\x12\x0e\n\x06itemNo\x18\x01 \x01(\x05\x12\x0b\n\x03\x63nt\x18\x02 \x01(\x05*\xc5\x07\n\nE_CURRENCY\x12\x08\n\x04None\x10\x00\x12\x08\n\x04Gold\x10\x01\x12\x0b\n\x07\x46reeDia\x10\x02\x12\x0c\n\x08ManaDust\x10\x03\x12\x0f\n\x0bManaCrystal\x10\x04\x12\x07\n\x03\x45xp\x10\x05\x12\t\n\x05Heart\x10\x06\x12\x0f\n\x0bLifeEssence\x10\x08\x12\x0f\n\x0b\x41renaTicket\x10\t\x12\x0b\n\x07\x44ungeon\x10\n\x12\t\n\x05Guild\x10\x0b\x12\x0b\n\x07Release\x10\x0c\x12\t\n\x05\x41rena\x10\r\x12\n\n\x06Relics\x10\x0e\x12\n\n\x06Silver\x10\x10\x12\x12\n\x0eSingleRaidCoin\x10\x12\x12\x15\n\x11PickupGachaTicket\x10\x13\x12\t\n\x05Sign1\x10\x14\x12\t\n\x05Sign2\x10\x15\x12\r\n\tSignHuman\x10\x16\x12\r\n\tSignFurry\x10\x17\x12\x0b\n\x07SignElf\x10\x18\x12\x0e\n\nSignUndead\x10\x19\x12\r\n\tSignAngel\x10\x1a\x12\r\n\tSignDemon\x10\x1b\x12\x10\n\x0cNormalTicket\x10\x1c\x12\x0e\n\nRaceTicket\x10\x1d\x12\x11\n\rRareSoulstone\x10\x1e\x12\x11\n\rEpicSoulstone\x10\x1f\x12\x0c\n\x08\x45quipExp\x10 \x12\x1d\n\x19\x43ollaborationSummonTicket\x10!\x12\n\n\x06PayDia\x10*\x12\x13\n\x0fTeamarenaTicket\x10,\x12\x18\n\x14SignatureGachaTicket\x10-\x12\x16\n\x12PremiumGachaTicket\x10.\x12\x1a\n\x16MonthlyHeroResetTicket\x10/\x12\x12\n\x0e\x45quipExpMiddle\x10\x30\x12\x10\n\x0c\x45quipExpHigh\x10\x31\x12\r\n\tZodiacExp\x10\x32\x12\x13\n\x0fLabyrinthTicket\x10\x33\x12\x15\n\x11TranscendentStone\x10\x34\x12\x14\n\x10SingleRaidTicket\x10\x35\x12\x12\n\x0eSetItemEngrave\x10\x36\x12\x19\n\x15RotationDungeonTicket\x10\x37\x12\x0c\n\x08\x45\x64\x65nCoin\x10\x39\x12\x19\n\x15TypeBarrierGateTicket\x10:\x12\x15\n\x11OriginTowerTicket\x10;\x12\x1a\n\x16\x44oubleGateNormalTicket\x10<\x12 \n\x1c\x44oubleGateNormalTicketCharge\x10>\x12\x19\n\x15SignatureEnhanceStone\x10@\x12\x19\n\x15HeroOptionChangeStone\x10\x41\x12\x13\n\x0fWishGachaTicket\x10\x42\x12\x0c\n\x08TotalDia\x10\x64\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'EventQuestReceive_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_E_CURRENCY']._serialized_start=671
  _globals['_E_CURRENCY']._serialized_end=1636
  _globals['_EVENTQUESTRECEIVE']._serialized_start=34
  _globals['_EVENTQUESTRECEIVE']._serialized_end=231
  _globals['_SEVENT']._serialized_start=233
  _globals['_SEVENT']._serialized_end=341
  _globals['_SEVENTRESULT']._serialized_start=343
  _globals['_SEVENTRESULT']._serialized_end=458
  _globals['_SCURRENCYALL']._serialized_start=460
  _globals['_SCURRENCYALL']._serialized_end=512
  _globals['_SCURRENCY']._serialized_start=514
  _globals['_SCURRENCY']._serialized_end=572
  _globals['_SITEMEQUIP']._serialized_start=574
  _globals['_SITEMEQUIP']._serialized_end=627
  _globals['_SITEMETC']._serialized_start=629
  _globals['_SITEMETC']._serialized_end=668
# @@protoc_insertion_point(module_scope)
