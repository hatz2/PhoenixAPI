from google.protobuf import empty_pb2 as _empty_pb2
from phoenixapi.protos.game import entities_pb2 as _entities_pb2
from phoenixapi.protos import position_pb2 as _position_pb2
from phoenixapi.protos.game import playermanager_pb2 as _playermanager_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PetState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PET_STATE_D: _ClassVar[PetState]
    PET_STATE_S: _ClassVar[PetState]
    PET_STATE_F: _ClassVar[PetState]
    PET_STATE_WALK_AFTER_F: _ClassVar[PetState]
    PET_STATE_A: _ClassVar[PetState]
    PET_STATE_AFTER_A_CLICK: _ClassVar[PetState]
    PET_STATE_S_AFTER_A_F: _ClassVar[PetState]
PET_STATE_D: PetState
PET_STATE_S: PetState
PET_STATE_F: PetState
PET_STATE_WALK_AFTER_F: PetState
PET_STATE_A: PetState
PET_STATE_AFTER_A_CLICK: PetState
PET_STATE_S_AFTER_A_F: PetState

class PetObjManagerList(_message.Message):
    __slots__ = ("pets",)
    PETS_FIELD_NUMBER: _ClassVar[int]
    pets: _containers.RepeatedCompositeFieldContainer[PetObjManager]
    def __init__(self, pets: _Optional[_Iterable[_Union[PetObjManager, _Mapping]]] = ...) -> None: ...

class PetObjManager(_message.Message):
    __slots__ = ("position", "dest_position", "state", "npc")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    DEST_POSITION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NPC_FIELD_NUMBER: _ClassVar[int]
    position: _position_pb2.Position
    dest_position: _position_pb2.Position
    state: PetState
    npc: _entities_pb2.Npc
    def __init__(self, position: _Optional[_Union[_position_pb2.Position, _Mapping]] = ..., dest_position: _Optional[_Union[_position_pb2.Position, _Mapping]] = ..., state: _Optional[_Union[PetState, str]] = ..., npc: _Optional[_Union[_entities_pb2.Npc, _Mapping]] = ...) -> None: ...

class AutoAttackRequest(_message.Message):
    __slots__ = ("entity_type", "entity_id")
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    entity_type: _entities_pb2.EntityType
    entity_id: int
    def __init__(self, entity_type: _Optional[_Union[_entities_pb2.EntityType, str]] = ..., entity_id: _Optional[int] = ...) -> None: ...

class PetStateRequest(_message.Message):
    __slots__ = ("pet_id", "new_state")
    PET_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_STATE_FIELD_NUMBER: _ClassVar[int]
    pet_id: int
    new_state: PetState
    def __init__(self, pet_id: _Optional[int] = ..., new_state: _Optional[_Union[PetState, str]] = ...) -> None: ...
