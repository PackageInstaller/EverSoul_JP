# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: DoubleGateSweep.proto
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
    'DoubleGateSweep.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x44oubleGateSweep.proto\x12\x04\x45sPb\"\xd7\x01\n\x0f\x44oubleGateSweep\x12$\n\x08\x63urrency\x18\x01 \x01(\x0b\x32\x12.EsPb.sCurrencyAll\x12#\n\titemEquip\x18\x02 \x03(\x0b\x32\x10.EsPb.sItemEquip\x12\x1f\n\x07itemEtc\x18\x03 \x03(\x0b\x32\x0e.EsPb.sItemEtc\x12\x31\n\x10itemChangeAmount\x18\x04 \x03(\x0b\x32\x17.EsPb.sItemChangeAmount\x12%\n\ndoubleGate\x18\x05 \x01(\x0b\x32\x11.EsPb.sDoubleGate\"4\n\x0csCurrencyAll\x12$\n\x0b\x61llCurrency\x18\x01 \x03(\x0b\x32\x0f.EsPb.sCurrency\":\n\tsCurrency\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.EsPb.E_CURRENCY\x12\r\n\x05value\x18\x02 \x01(\x03\"5\n\nsItemEquip\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06itemNo\x18\x02 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x01(\x05\"\'\n\x08sItemEtc\x12\x0e\n\x06itemNo\x18\x01 \x01(\x05\x12\x0b\n\x03\x63nt\x18\x02 \x01(\x05\"0\n\x11sItemChangeAmount\x12\x0e\n\x06itemNo\x18\x01 \x01(\x05\x12\x0b\n\x03\x63nt\x18\x02 \x01(\x05\"\xa3\x01\n\x0bsDoubleGate\x12-\n\tstageType\x18\x01 \x01(\x0e\x32\x1a.EsPb.eDoubleGateStageType\x12\x12\n\ndifficulty\x18\x02 \x01(\x05\x12\x0f\n\x07isEnter\x18\x03 \x01(\x05\x12\x17\n\x0fsweepDifficulty\x18\x04 \x01(\x05\x12\'\n\x06record\x18\x05 \x03(\x0b\x32\x17.EsPb.sDoubleGateRecord\"O\n\x11sDoubleGateRecord\x12\x11\n\troundType\x18\x01 \x01(\x05\x12\'\n\x08heroInfo\x18\x02 \x03(\x0b\x32\x15.EsPb.sDoubleGateHero\"S\n\x0fsDoubleGateHero\x12\x0f\n\x07heroIdx\x18\x01 \x01(\t\x12\x0e\n\x06heroNo\x18\x02 \x01(\x05\x12\r\n\x05level\x18\x03 \x01(\x05\x12\x10\n\x08gradeSno\x18\x04 \x01(\x05*\xc5\x07\n\nE_CURRENCY\x12\x08\n\x04None\x10\x00\x12\x08\n\x04Gold\x10\x01\x12\x0b\n\x07\x46reeDia\x10\x02\x12\x0c\n\x08ManaDust\x10\x03\x12\x0f\n\x0bManaCrystal\x10\x04\x12\x07\n\x03\x45xp\x10\x05\x12\t\n\x05Heart\x10\x06\x12\x0f\n\x0bLifeEssence\x10\x08\x12\x0f\n\x0b\x41renaTicket\x10\t\x12\x0b\n\x07\x44ungeon\x10\n\x12\t\n\x05Guild\x10\x0b\x12\x0b\n\x07Release\x10\x0c\x12\t\n\x05\x41rena\x10\r\x12\n\n\x06Relics\x10\x0e\x12\n\n\x06Silver\x10\x10\x12\x12\n\x0eSingleRaidCoin\x10\x12\x12\x15\n\x11PickupGachaTicket\x10\x13\x12\t\n\x05Sign1\x10\x14\x12\t\n\x05Sign2\x10\x15\x12\r\n\tSignHuman\x10\x16\x12\r\n\tSignFurry\x10\x17\x12\x0b\n\x07SignElf\x10\x18\x12\x0e\n\nSignUndead\x10\x19\x12\r\n\tSignAngel\x10\x1a\x12\r\n\tSignDemon\x10\x1b\x12\x10\n\x0cNormalTicket\x10\x1c\x12\x0e\n\nRaceTicket\x10\x1d\x12\x11\n\rRareSoulstone\x10\x1e\x12\x11\n\rEpicSoulstone\x10\x1f\x12\x0c\n\x08\x45quipExp\x10 \x12\x1d\n\x19\x43ollaborationSummonTicket\x10!\x12\n\n\x06PayDia\x10*\x12\x13\n\x0fTeamarenaTicket\x10,\x12\x18\n\x14SignatureGachaTicket\x10-\x12\x16\n\x12PremiumGachaTicket\x10.\x12\x1a\n\x16MonthlyHeroResetTicket\x10/\x12\x12\n\x0e\x45quipExpMiddle\x10\x30\x12\x10\n\x0c\x45quipExpHigh\x10\x31\x12\r\n\tZodiacExp\x10\x32\x12\x13\n\x0fLabyrinthTicket\x10\x33\x12\x15\n\x11TranscendentStone\x10\x34\x12\x14\n\x10SingleRaidTicket\x10\x35\x12\x12\n\x0eSetItemEngrave\x10\x36\x12\x19\n\x15RotationDungeonTicket\x10\x37\x12\x0c\n\x08\x45\x64\x65nCoin\x10\x39\x12\x19\n\x15TypeBarrierGateTicket\x10:\x12\x15\n\x11OriginTowerTicket\x10;\x12\x1a\n\x16\x44oubleGateNormalTicket\x10<\x12 \n\x1c\x44oubleGateNormalTicketCharge\x10>\x12\x19\n\x15SignatureEnhanceStone\x10@\x12\x19\n\x15HeroOptionChangeStone\x10\x41\x12\x13\n\x0fWishGachaTicket\x10\x42\x12\x0c\n\x08TotalDia\x10\x64*\xae\x01\n\x14\x65\x44oubleGateStageType\x12\x1b\n\x17\x44oubleGateStageTypeNone\x10\x00\x12\x1f\n\x1b\x44oubleGateNormalManaCrystal\x10\x01\x12\x18\n\x14\x44oubleGateNormalGold\x10\x02\x12\x1c\n\x18\x44oubleGateNormalManaDust\x10\x03\x12 \n\x1c\x44oubleGateNormalEnhanceStone\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DoubleGateSweep_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_E_CURRENCY']._serialized_start=842
  _globals['_E_CURRENCY']._serialized_end=1807
  _globals['_EDOUBLEGATESTAGETYPE']._serialized_start=1810
  _globals['_EDOUBLEGATESTAGETYPE']._serialized_end=1984
  _globals['_DOUBLEGATESWEEP']._serialized_start=32
  _globals['_DOUBLEGATESWEEP']._serialized_end=247
  _globals['_SCURRENCYALL']._serialized_start=249
  _globals['_SCURRENCYALL']._serialized_end=301
  _globals['_SCURRENCY']._serialized_start=303
  _globals['_SCURRENCY']._serialized_end=361
  _globals['_SITEMEQUIP']._serialized_start=363
  _globals['_SITEMEQUIP']._serialized_end=416
  _globals['_SITEMETC']._serialized_start=418
  _globals['_SITEMETC']._serialized_end=457
  _globals['_SITEMCHANGEAMOUNT']._serialized_start=459
  _globals['_SITEMCHANGEAMOUNT']._serialized_end=507
  _globals['_SDOUBLEGATE']._serialized_start=510
  _globals['_SDOUBLEGATE']._serialized_end=673
  _globals['_SDOUBLEGATERECORD']._serialized_start=675
  _globals['_SDOUBLEGATERECORD']._serialized_end=754
  _globals['_SDOUBLEGATEHERO']._serialized_start=756
  _globals['_SDOUBLEGATEHERO']._serialized_end=839
# @@protoc_insertion_point(module_scope)
