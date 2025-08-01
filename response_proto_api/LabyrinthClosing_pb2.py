# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: LabyrinthClosing.proto
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
    'LabyrinthClosing.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16LabyrinthClosing.proto\x12\x04\x45sPb\"\xf9\x01\n\x10LabyrinthClosing\x12$\n\x08\x63urrency\x18\x01 \x01(\x0b\x32\x12.EsPb.sCurrencyAll\x12#\n\titemEquip\x18\x02 \x03(\x0b\x32\x10.EsPb.sItemEquip\x12\x1f\n\x07itemEtc\x18\x03 \x03(\x0b\x32\x0e.EsPb.sItemEtc\x12+\n\rdungeonReward\x18\x04 \x03(\x0b\x32\x14.EsPb.sDungeonReward\x12\x1f\n\x07\x64ungeon\x18\x05 \x01(\x0b\x32\x0e.EsPb.sDungeon\x12+\n\rlabyrinthInfo\x18\x06 \x01(\x0b\x32\x14.EsPb.sLabyrinthInfo\"4\n\x0csCurrencyAll\x12$\n\x0b\x61llCurrency\x18\x01 \x03(\x0b\x32\x0f.EsPb.sCurrency\":\n\tsCurrency\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.EsPb.E_CURRENCY\x12\r\n\x05value\x18\x02 \x01(\x03\"5\n\nsItemEquip\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06itemNo\x18\x02 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x01(\x05\"\'\n\x08sItemEtc\x12\x0e\n\x06itemNo\x18\x01 \x01(\x05\x12\x0b\n\x03\x63nt\x18\x02 \x01(\x05\"J\n\x0esDungeonReward\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.EsPb.eDungeonRewardType\x12\x10\n\x08rewardNo\x18\x02 \x01(\x05\"\x8e\x04\n\x08sDungeon\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tdungeonNo\x18\x02 \x01(\x05\x12\x14\n\x0c\x64ungeonLevel\x18\x03 \x01(\x05\x12\t\n\x01x\x18\x04 \x01(\x02\x12\t\n\x01z\x18\x05 \x01(\x02\x12\x0f\n\x07mapInfo\x18\x06 \x01(\x0c\x12\x15\n\rconditionInfo\x18\x07 \x01(\x0c\x12\x10\n\x08heroInfo\x18\x08 \x01(\x0c\x12\x16\n\x0e\x61\x64\x64itionalInfo\x18\t \x01(\x0c\x12\x11\n\trelicInfo\x18\n \x01(\x0c\x12\x0f\n\x07isEnter\x18\x0b \x01(\x05\x12\x0f\n\x07isClear\x18\x0c \x01(\x05\x12\x14\n\x0cisFirstClear\x18\r \x01(\x05\x12\x11\n\tmissionNo\x18\x0e \x01(\x05\x12\x12\n\nmissionCnt\x18\x0f \x01(\x05\x12\x0c\n\x04seed\x18\x10 \x01(\x05\x12\x13\n\x0b\x64ungeonItem\x18\x11 \x01(\x0c\x12\x12\n\ndifficulty\x18\x12 \x01(\x05\x12\x15\n\rultimatePoint\x18\x13 \x01(\x05\x12\x16\n\x0eplayerObjectId\x18\x14 \x01(\x05\x12\x11\n\tuseTicket\x18\x15 \x01(\x08\x12\x15\n\rmaxClearLevel\x18\x16 \x01(\x05\x12\x0f\n\x07isSweep\x18\x17 \x01(\x05\x12\x16\n\x0eisPerfectClear\x18\x18 \x01(\x05\x12\x1f\n\x17isHiddenKeyNotAvailable\x18\x19 \x01(\x05\x12\x19\n\x11randomGimmickSeed\x18\x1a \x01(\x05\"\xff\x01\n\x0esLabyrinthInfo\x12\x11\n\tisPlaying\x18\x01 \x01(\x08\x12\x1a\n\x12\x63urrentLabyrinthNo\x18\x02 \x01(\x05\x12\x1d\n\x15\x63urrentAdditionalInfo\x18\x03 \x01(\x0c\x12\x15\n\rmaxClearFloor\x18\x04 \x01(\x05\x12\x0f\n\x07isClear\x18\x05 \x01(\x05\x12\x0f\n\x07isSweep\x18\x06 \x01(\x05\x12\x16\n\x0emaxLabyrinthNo\x18\x07 \x01(\x05\x12\x19\n\x11labyrinthClearCnt\x18\x08 \x01(\x05\x12\x1a\n\x12labyrinthTicketCnt\x18\t \x01(\x05\x12\x17\n\x0fisLabyrinthOpen\x18\n \x01(\x08*\xc5\x07\n\nE_CURRENCY\x12\x08\n\x04None\x10\x00\x12\x08\n\x04Gold\x10\x01\x12\x0b\n\x07\x46reeDia\x10\x02\x12\x0c\n\x08ManaDust\x10\x03\x12\x0f\n\x0bManaCrystal\x10\x04\x12\x07\n\x03\x45xp\x10\x05\x12\t\n\x05Heart\x10\x06\x12\x0f\n\x0bLifeEssence\x10\x08\x12\x0f\n\x0b\x41renaTicket\x10\t\x12\x0b\n\x07\x44ungeon\x10\n\x12\t\n\x05Guild\x10\x0b\x12\x0b\n\x07Release\x10\x0c\x12\t\n\x05\x41rena\x10\r\x12\n\n\x06Relics\x10\x0e\x12\n\n\x06Silver\x10\x10\x12\x12\n\x0eSingleRaidCoin\x10\x12\x12\x15\n\x11PickupGachaTicket\x10\x13\x12\t\n\x05Sign1\x10\x14\x12\t\n\x05Sign2\x10\x15\x12\r\n\tSignHuman\x10\x16\x12\r\n\tSignFurry\x10\x17\x12\x0b\n\x07SignElf\x10\x18\x12\x0e\n\nSignUndead\x10\x19\x12\r\n\tSignAngel\x10\x1a\x12\r\n\tSignDemon\x10\x1b\x12\x10\n\x0cNormalTicket\x10\x1c\x12\x0e\n\nRaceTicket\x10\x1d\x12\x11\n\rRareSoulstone\x10\x1e\x12\x11\n\rEpicSoulstone\x10\x1f\x12\x0c\n\x08\x45quipExp\x10 \x12\x1d\n\x19\x43ollaborationSummonTicket\x10!\x12\n\n\x06PayDia\x10*\x12\x13\n\x0fTeamarenaTicket\x10,\x12\x18\n\x14SignatureGachaTicket\x10-\x12\x16\n\x12PremiumGachaTicket\x10.\x12\x1a\n\x16MonthlyHeroResetTicket\x10/\x12\x12\n\x0e\x45quipExpMiddle\x10\x30\x12\x10\n\x0c\x45quipExpHigh\x10\x31\x12\r\n\tZodiacExp\x10\x32\x12\x13\n\x0fLabyrinthTicket\x10\x33\x12\x15\n\x11TranscendentStone\x10\x34\x12\x14\n\x10SingleRaidTicket\x10\x35\x12\x12\n\x0eSetItemEngrave\x10\x36\x12\x19\n\x15RotationDungeonTicket\x10\x37\x12\x0c\n\x08\x45\x64\x65nCoin\x10\x39\x12\x19\n\x15TypeBarrierGateTicket\x10:\x12\x15\n\x11OriginTowerTicket\x10;\x12\x1a\n\x16\x44oubleGateNormalTicket\x10<\x12 \n\x1c\x44oubleGateNormalTicketCharge\x10>\x12\x19\n\x15SignatureEnhanceStone\x10@\x12\x19\n\x15HeroOptionChangeStone\x10\x41\x12\x13\n\x0fWishGachaTicket\x10\x42\x12\x0c\n\x08TotalDia\x10\x64*\\\n\x12\x65\x44ungeonRewardType\x12\x15\n\x11NoneDungeonReward\x10\x00\x12\x0b\n\x07Mission\x10\x01\x12\n\n\x06Object\x10\x02\x12\x0b\n\x07Monster\x10\x03\x12\t\n\x05\x43hest\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'LabyrinthClosing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_E_CURRENCY']._serialized_start=1358
  _globals['_E_CURRENCY']._serialized_end=2323
  _globals['_EDUNGEONREWARDTYPE']._serialized_start=2325
  _globals['_EDUNGEONREWARDTYPE']._serialized_end=2417
  _globals['_LABYRINTHCLOSING']._serialized_start=33
  _globals['_LABYRINTHCLOSING']._serialized_end=282
  _globals['_SCURRENCYALL']._serialized_start=284
  _globals['_SCURRENCYALL']._serialized_end=336
  _globals['_SCURRENCY']._serialized_start=338
  _globals['_SCURRENCY']._serialized_end=396
  _globals['_SITEMEQUIP']._serialized_start=398
  _globals['_SITEMEQUIP']._serialized_end=451
  _globals['_SITEMETC']._serialized_start=453
  _globals['_SITEMETC']._serialized_end=492
  _globals['_SDUNGEONREWARD']._serialized_start=494
  _globals['_SDUNGEONREWARD']._serialized_end=568
  _globals['_SDUNGEON']._serialized_start=571
  _globals['_SDUNGEON']._serialized_end=1097
  _globals['_SLABYRINTHINFO']._serialized_start=1100
  _globals['_SLABYRINTHINFO']._serialized_end=1355
# @@protoc_insertion_point(module_scope)
