# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: AchievementAllReceive.proto
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
    'AchievementAllReceive.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x41\x63hievementAllReceive.proto\x12\x04\x45sPb\"\xb1\x03\n\x15\x41\x63hievementAllReceive\x12\'\n\x0b\x61\x63hievement\x18\x01 \x03(\x0b\x32\x12.EsPb.sAchievement\x12\x19\n\x04hero\x18\x02 \x03(\x0b\x32\x0b.EsPb.sHero\x12-\n\x0eheroReputation\x18\x03 \x03(\x0b\x32\x15.EsPb.sHeroReputation\x12$\n\x08\x63urrency\x18\x04 \x01(\x0b\x32\x12.EsPb.sCurrencyAll\x12#\n\titemEquip\x18\x05 \x03(\x0b\x32\x10.EsPb.sItemEquip\x12\x1f\n\x07itemEtc\x18\x06 \x03(\x0b\x32\x0e.EsPb.sItemEtc\x12#\n\ttaskDaily\x18\x07 \x01(\x0b\x32\x10.EsPb.sTaskDaily\x12%\n\ntaskWeekly\x18\x08 \x01(\x0b\x32\x11.EsPb.sTaskWeekly\x12\'\n\x0bmissionPass\x18\t \x03(\x0b\x32\x12.EsPb.sMissionPass\x12\x1b\n\x05guild\x18\n \x01(\x0b\x32\x0c.EsPb.sGuild\x12\'\n\x0bguildMember\x18\x0b \x03(\x0b\x32\x12.EsPb.sGuildMember\"V\n\x0csAchievement\x12\x10\n\x08\x62\x65havior\x18\x01 \x01(\x05\x12\r\n\x05group\x18\x02 \x01(\x05\x12\r\n\x05value\x18\x03 \x01(\x03\x12\x16\n\x0elastReceivedNo\x18\x04 \x01(\x05\"{\n\x05sHero\x12\x0b\n\x03idx\x18\x01 \x01(\t\x12\x0e\n\x06heroNo\x18\x02 \x01(\x05\x12\r\n\x05level\x18\x03 \x01(\x05\x12\x13\n\x0bisResonance\x18\x04 \x01(\x05\x12\x10\n\x08gradeSno\x18\x05 \x01(\x05\x12\x0f\n\x07raceSno\x18\x06 \x01(\x05\x12\x0e\n\x06isLock\x18\x07 \x01(\x05\"\x9c\x02\n\x0fsHeroReputation\x12\x0e\n\x06heroNo\x18\x01 \x01(\x05\x12\x12\n\nreputation\x18\x02 \x01(\x05\x12\r\n\x05state\x18\x03 \x01(\x05\x12\x0e\n\x06stress\x18\x04 \x01(\x05\x12\x14\n\x0clastUpdateDt\x18\x05 \x01(\x03\x12\x0e\n\x06giftDt\x18\x06 \x01(\x03\x12\x15\n\rcostumeItemNo\x18\x07 \x01(\x05\x12\x13\n\x0bstoryReward\x18\x08 \x01(\x05\x12\x13\n\x0bmaxGradeSno\x18\t \x01(\x05\x12\x10\n\x08objetUid\x18\n \x01(\x05\x12\x12\n\nmaxLevelDt\x18\x0b \x01(\x03\x12\x11\n\tarbeitExp\x18\x0c \x01(\x05\x12\x10\n\x08priority\x18\r \x01(\x05\x12\x14\n\x0crestFinishDt\x18\x0e \x01(\x03\"4\n\x0csCurrencyAll\x12$\n\x0b\x61llCurrency\x18\x01 \x03(\x0b\x32\x0f.EsPb.sCurrency\":\n\tsCurrency\x12\x1e\n\x04type\x18\x01 \x01(\x0e\x32\x10.EsPb.E_CURRENCY\x12\r\n\x05value\x18\x02 \x01(\x03\"5\n\nsItemEquip\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06itemNo\x18\x02 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x01(\x05\"\'\n\x08sItemEtc\x12\x0e\n\x06itemNo\x18\x01 \x01(\x05\x12\x0b\n\x03\x63nt\x18\x02 \x01(\x05\"h\n\nsTaskDaily\x12\x0c\n\x04\x64\x61ys\x18\x01 \x01(\r\x12#\n\ttaskValue\x18\x02 \x03(\x0b\x32\x10.EsPb.sTaskValue\x12\'\n\x0btaskReceive\x18\x03 \x03(\x0b\x32\x12.EsPb.sTaskReceive\"\x19\n\nsTaskValue\x12\x0b\n\x03val\x18\x01 \x01(\r\"\x1b\n\x0csTaskReceive\x12\x0b\n\x03val\x18\x01 \x01(\r\"j\n\x0bsTaskWeekly\x12\r\n\x05weeks\x18\x01 \x01(\r\x12#\n\ttaskValue\x18\x02 \x03(\x0b\x32\x10.EsPb.sTaskValue\x12\'\n\x0btaskReceive\x18\x03 \x03(\x0b\x32\x12.EsPb.sTaskReceive\"\x85\x01\n\x0csMissionPass\x12\x15\n\rmissionPassNo\x18\x01 \x01(\x05\x12\r\n\x05point\x18\x02 \x01(\x05\x12\x15\n\rrewardedPoint\x18\x03 \x01(\x05\x12\x13\n\x0bisBuyTicket\x18\x04 \x01(\x05\x12\x10\n\x08rewardNo\x18\x05 \x01(\x05\x12\x11\n\texpiredDt\x18\x06 \x01(\x03\"\xbe\x02\n\x06sGuild\x12\x0b\n\x03idx\x18\x01 \x01(\t\x12\x10\n\x08\x65mblemNo\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0b\n\x03\x65xp\x18\x04 \x01(\x05\x12\x0b\n\x03\x63nt\x18\x05 \x01(\x05\x12\x10\n\x08joinType\x18\x06 \x01(\x05\x12\x0f\n\x07limitLv\x18\x07 \x01(\x05\x12\x0e\n\x06notice\x18\x08 \x01(\t\x12\n\n\x02\x64t\x18\t \x01(\x03\x12\x15\n\rregularRaidNo\x18\n \x01(\x05\x12\x17\n\x0firregularRaidNo\x18\x0b \x01(\x05\x12\x11\n\traidPoint\x18\x0c \x01(\x05\x12\x15\n\ruseSkillPoint\x18\r \x01(\x05\x12\x12\n\nskillLevel\x18\x0e \x01(\t\x12\x14\n\x0c\x63ustomEmblem\x18\x0f \x01(\x0c\x12\x14\n\x0cskillResetDt\x18\x10 \x01(\x03\x12\x14\n\x0cintroduction\x18\x11 \x01(\t\"\x8d\x02\n\x0csGuildMember\x12\x10\n\x08guildIdx\x18\x01 \x01(\t\x12\x0f\n\x07userIdx\x18\x02 \x01(\t\x12\x11\n\tchannelNo\x18\x03 \x01(\x05\x12\r\n\x05grade\x18\x04 \x01(\x05\x12\n\n\x02\x64t\x18\x05 \x01(\x03\x12\x14\n\x0c\x63ontribution\x18\x06 \x01(\x05\x12\x10\n\x08nickName\x18\x07 \x01(\t\x12\x13\n\x0blastLoginDt\x18\x08 \x01(\x03\x12#\n\tthumbnail\x18\t \x01(\x0b\x32\x10.EsPb.sThumbnail\x12\r\n\x05power\x18\n \x01(\x03\x12\r\n\x05level\x18\x0b \x01(\x05\x12\x10\n\x08logoutDt\x18\x0c \x01(\x03\x12\x1a\n\x12weeklyContribution\x18\r \x01(\x05\"b\n\nsThumbnail\x12\x16\n\x0ethumbnailFrame\x18\x01 \x01(\x05\x12\x16\n\x0ethumbnailImage\x18\x02 \x01(\x05\x12\x11\n\tuseCustom\x18\x03 \x01(\x08\x12\x11\n\tthumbnail\x18\x04 \x01(\x0c*\xc5\x07\n\nE_CURRENCY\x12\x08\n\x04None\x10\x00\x12\x08\n\x04Gold\x10\x01\x12\x0b\n\x07\x46reeDia\x10\x02\x12\x0c\n\x08ManaDust\x10\x03\x12\x0f\n\x0bManaCrystal\x10\x04\x12\x07\n\x03\x45xp\x10\x05\x12\t\n\x05Heart\x10\x06\x12\x0f\n\x0bLifeEssence\x10\x08\x12\x0f\n\x0b\x41renaTicket\x10\t\x12\x0b\n\x07\x44ungeon\x10\n\x12\t\n\x05Guild\x10\x0b\x12\x0b\n\x07Release\x10\x0c\x12\t\n\x05\x41rena\x10\r\x12\n\n\x06Relics\x10\x0e\x12\n\n\x06Silver\x10\x10\x12\x12\n\x0eSingleRaidCoin\x10\x12\x12\x15\n\x11PickupGachaTicket\x10\x13\x12\t\n\x05Sign1\x10\x14\x12\t\n\x05Sign2\x10\x15\x12\r\n\tSignHuman\x10\x16\x12\r\n\tSignFurry\x10\x17\x12\x0b\n\x07SignElf\x10\x18\x12\x0e\n\nSignUndead\x10\x19\x12\r\n\tSignAngel\x10\x1a\x12\r\n\tSignDemon\x10\x1b\x12\x10\n\x0cNormalTicket\x10\x1c\x12\x0e\n\nRaceTicket\x10\x1d\x12\x11\n\rRareSoulstone\x10\x1e\x12\x11\n\rEpicSoulstone\x10\x1f\x12\x0c\n\x08\x45quipExp\x10 \x12\x1d\n\x19\x43ollaborationSummonTicket\x10!\x12\n\n\x06PayDia\x10*\x12\x13\n\x0fTeamarenaTicket\x10,\x12\x18\n\x14SignatureGachaTicket\x10-\x12\x16\n\x12PremiumGachaTicket\x10.\x12\x1a\n\x16MonthlyHeroResetTicket\x10/\x12\x12\n\x0e\x45quipExpMiddle\x10\x30\x12\x10\n\x0c\x45quipExpHigh\x10\x31\x12\r\n\tZodiacExp\x10\x32\x12\x13\n\x0fLabyrinthTicket\x10\x33\x12\x15\n\x11TranscendentStone\x10\x34\x12\x14\n\x10SingleRaidTicket\x10\x35\x12\x12\n\x0eSetItemEngrave\x10\x36\x12\x19\n\x15RotationDungeonTicket\x10\x37\x12\x0c\n\x08\x45\x64\x65nCoin\x10\x39\x12\x19\n\x15TypeBarrierGateTicket\x10:\x12\x15\n\x11OriginTowerTicket\x10;\x12\x1a\n\x16\x44oubleGateNormalTicket\x10<\x12 \n\x1c\x44oubleGateNormalTicketCharge\x10>\x12\x19\n\x15SignatureEnhanceStone\x10@\x12\x19\n\x15HeroOptionChangeStone\x10\x41\x12\x13\n\x0fWishGachaTicket\x10\x42\x12\x0c\n\x08TotalDia\x10\x64\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'AchievementAllReceive_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_E_CURRENCY']._serialized_start=2283
  _globals['_E_CURRENCY']._serialized_end=3248
  _globals['_ACHIEVEMENTALLRECEIVE']._serialized_start=38
  _globals['_ACHIEVEMENTALLRECEIVE']._serialized_end=471
  _globals['_SACHIEVEMENT']._serialized_start=473
  _globals['_SACHIEVEMENT']._serialized_end=559
  _globals['_SHERO']._serialized_start=561
  _globals['_SHERO']._serialized_end=684
  _globals['_SHEROREPUTATION']._serialized_start=687
  _globals['_SHEROREPUTATION']._serialized_end=971
  _globals['_SCURRENCYALL']._serialized_start=973
  _globals['_SCURRENCYALL']._serialized_end=1025
  _globals['_SCURRENCY']._serialized_start=1027
  _globals['_SCURRENCY']._serialized_end=1085
  _globals['_SITEMEQUIP']._serialized_start=1087
  _globals['_SITEMEQUIP']._serialized_end=1140
  _globals['_SITEMETC']._serialized_start=1142
  _globals['_SITEMETC']._serialized_end=1181
  _globals['_STASKDAILY']._serialized_start=1183
  _globals['_STASKDAILY']._serialized_end=1287
  _globals['_STASKVALUE']._serialized_start=1289
  _globals['_STASKVALUE']._serialized_end=1314
  _globals['_STASKRECEIVE']._serialized_start=1316
  _globals['_STASKRECEIVE']._serialized_end=1343
  _globals['_STASKWEEKLY']._serialized_start=1345
  _globals['_STASKWEEKLY']._serialized_end=1451
  _globals['_SMISSIONPASS']._serialized_start=1454
  _globals['_SMISSIONPASS']._serialized_end=1587
  _globals['_SGUILD']._serialized_start=1590
  _globals['_SGUILD']._serialized_end=1908
  _globals['_SGUILDMEMBER']._serialized_start=1911
  _globals['_SGUILDMEMBER']._serialized_end=2180
  _globals['_STHUMBNAIL']._serialized_start=2182
  _globals['_STHUMBNAIL']._serialized_end=2280
# @@protoc_insertion_point(module_scope)
