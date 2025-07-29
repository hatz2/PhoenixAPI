from phoenixapi.protos import position_pb2 as _position_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIRECTION_UP: _ClassVar[Direction]
    DIRECTION_RIGHT: _ClassVar[Direction]
    DIRECTION_DOWN: _ClassVar[Direction]
    DIRECTION_LEFT: _ClassVar[Direction]
    DIRECTION_UP_LEFT: _ClassVar[Direction]
    DIRECTION_UP_RIGHT: _ClassVar[Direction]
    DIRECTION_DOWN_RIGHT: _ClassVar[Direction]
    DIRECTION_DOWN_LEFT: _ClassVar[Direction]

class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTITY_TYPE_UNSPECIFIED: _ClassVar[EntityType]
    ENTITY_TYPE_PLAYER: _ClassVar[EntityType]
    ENTITY_TYPE_MONSTER: _ClassVar[EntityType]
    ENTITY_TYPE_NPC: _ClassVar[EntityType]
    ENTITY_TYPE_ITEM: _ClassVar[EntityType]
DIRECTION_UP: Direction
DIRECTION_RIGHT: Direction
DIRECTION_DOWN: Direction
DIRECTION_LEFT: Direction
DIRECTION_UP_LEFT: Direction
DIRECTION_UP_RIGHT: Direction
DIRECTION_DOWN_RIGHT: Direction
DIRECTION_DOWN_LEFT: Direction
ENTITY_TYPE_UNSPECIFIED: EntityType
ENTITY_TYPE_PLAYER: EntityType
ENTITY_TYPE_MONSTER: EntityType
ENTITY_TYPE_NPC: EntityType
ENTITY_TYPE_ITEM: EntityType

class BaseEntity(_message.Message):
    __slots__ = ("type", "id", "position")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    type: EntityType
    id: int
    position: _position_pb2.Position
    def __init__(self, type: _Optional[_Union[EntityType, str]] = ..., id: _Optional[int] = ..., position: _Optional[_Union[_position_pb2.Position, _Mapping]] = ...) -> None: ...

class MovableEntity(_message.Message):
    __slots__ = ("base_entity", "direction", "animation_status", "speed", "is_in_combat", "health_percent", "mana_percent", "level", "champion_level", "is_partner", "owner_id", "current_map_id")
    BASE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ANIMATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    IS_IN_COMBAT_FIELD_NUMBER: _ClassVar[int]
    HEALTH_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MANA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHAMPION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_PARTNER_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MAP_ID_FIELD_NUMBER: _ClassVar[int]
    base_entity: BaseEntity
    direction: Direction
    animation_status: int
    speed: int
    is_in_combat: bool
    health_percent: int
    mana_percent: int
    level: int
    champion_level: int
    is_partner: bool
    owner_id: int
    current_map_id: int
    def __init__(self, base_entity: _Optional[_Union[BaseEntity, _Mapping]] = ..., direction: _Optional[_Union[Direction, str]] = ..., animation_status: _Optional[int] = ..., speed: _Optional[int] = ..., is_in_combat: bool = ..., health_percent: _Optional[int] = ..., mana_percent: _Optional[int] = ..., level: _Optional[int] = ..., champion_level: _Optional[int] = ..., is_partner: bool = ..., owner_id: _Optional[int] = ..., current_map_id: _Optional[int] = ...) -> None: ...

class Player(_message.Message):
    __slots__ = ("movable_entity", "sp", "name", "title", "family", "is_gm", "reputation")
    MOVABLE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    SP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    IS_GM_FIELD_NUMBER: _ClassVar[int]
    REPUTATION_FIELD_NUMBER: _ClassVar[int]
    movable_entity: MovableEntity
    sp: int
    name: str
    title: str
    family: str
    is_gm: bool
    reputation: int
    def __init__(self, movable_entity: _Optional[_Union[MovableEntity, _Mapping]] = ..., sp: _Optional[int] = ..., name: _Optional[str] = ..., title: _Optional[str] = ..., family: _Optional[str] = ..., is_gm: bool = ..., reputation: _Optional[int] = ...) -> None: ...

class Monster(_message.Message):
    __slots__ = ("movable_entity", "vnum", "name", "race", "skin_id", "is_boss")
    MOVABLE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VNUM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RACE_FIELD_NUMBER: _ClassVar[int]
    SKIN_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BOSS_FIELD_NUMBER: _ClassVar[int]
    movable_entity: MovableEntity
    vnum: int
    name: str
    race: int
    skin_id: int
    is_boss: bool
    def __init__(self, movable_entity: _Optional[_Union[MovableEntity, _Mapping]] = ..., vnum: _Optional[int] = ..., name: _Optional[str] = ..., race: _Optional[int] = ..., skin_id: _Optional[int] = ..., is_boss: bool = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("base_entity", "vnum", "quantity", "owner_id", "is_quest_item", "name")
    BASE_ENTITY_FIELD_NUMBER: _ClassVar[int]
    VNUM_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    IS_QUEST_ITEM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    base_entity: BaseEntity
    vnum: int
    quantity: int
    owner_id: int
    is_quest_item: bool
    name: str
    def __init__(self, base_entity: _Optional[_Union[BaseEntity, _Mapping]] = ..., vnum: _Optional[int] = ..., quantity: _Optional[int] = ..., owner_id: _Optional[int] = ..., is_quest_item: bool = ..., name: _Optional[str] = ...) -> None: ...

class Npc(_message.Message):
    __slots__ = ("monster", "name")
    MONSTER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    monster: Monster
    name: str
    def __init__(self, monster: _Optional[_Union[Monster, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...
