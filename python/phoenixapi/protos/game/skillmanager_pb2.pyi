from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SKILL_TYPE_DAMAGE: _ClassVar[SkillType]
    SKILL_TYPE_DEBUFF: _ClassVar[SkillType]
    SKILL_TYPE_BUFF: _ClassVar[SkillType]

class TargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TARGET_TYPE_TARGET: _ClassVar[TargetType]
    TARGET_TYPE_SELF: _ClassVar[TargetType]
    TARGET_TYPE_SELF_OR_TARGET: _ClassVar[TargetType]
    TARGET_TYPE_NO_TARGET: _ClassVar[TargetType]
SKILL_TYPE_DAMAGE: SkillType
SKILL_TYPE_DEBUFF: SkillType
SKILL_TYPE_BUFF: SkillType
TARGET_TYPE_TARGET: TargetType
TARGET_TYPE_SELF: TargetType
TARGET_TYPE_SELF_OR_TARGET: TargetType
TARGET_TYPE_NO_TARGET: TargetType

class FindSkillFromVnumRequest(_message.Message):
    __slots__ = ("vnum",)
    VNUM_FIELD_NUMBER: _ClassVar[int]
    vnum: int
    def __init__(self, vnum: _Optional[int] = ...) -> None: ...

class FindSkillFromIdRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class Skill(_message.Message):
    __slots__ = ("vnum", "name", "id", "type", "range", "area", "cast_time", "cool_time", "mana_cost")
    VNUM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    CAST_TIME_FIELD_NUMBER: _ClassVar[int]
    COOL_TIME_FIELD_NUMBER: _ClassVar[int]
    MANA_COST_FIELD_NUMBER: _ClassVar[int]
    vnum: int
    name: str
    id: int
    type: SkillType
    range: int
    area: int
    cast_time: int
    cool_time: int
    mana_cost: int
    def __init__(self, vnum: _Optional[int] = ..., name: _Optional[str] = ..., id: _Optional[int] = ..., type: _Optional[_Union[SkillType, str]] = ..., range: _Optional[int] = ..., area: _Optional[int] = ..., cast_time: _Optional[int] = ..., cool_time: _Optional[int] = ..., mana_cost: _Optional[int] = ...) -> None: ...

class SkillList(_message.Message):
    __slots__ = ("skills",)
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[Skill]
    def __init__(self, skills: _Optional[_Iterable[_Union[Skill, _Mapping]]] = ...) -> None: ...
