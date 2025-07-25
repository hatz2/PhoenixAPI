from google.protobuf import empty_pb2 as _empty_pb2
from phoenixapi.protos.game import entities_pb2 as _entities_pb2
from phoenixapi.protos import position_pb2 as _position_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerObjManager(_message.Message):
    __slots__ = ("position", "dest_position", "state", "player", "id", "is_resting")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    DEST_POSITION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_RESTING_FIELD_NUMBER: _ClassVar[int]
    position: _position_pb2.Position
    dest_position: _position_pb2.Position
    state: int
    player: _entities_pb2.Player
    id: int
    is_resting: bool
    def __init__(self, position: _Optional[_Union[_position_pb2.Position, _Mapping]] = ..., dest_position: _Optional[_Union[_position_pb2.Position, _Mapping]] = ..., state: _Optional[int] = ..., player: _Optional[_Union[_entities_pb2.Player, _Mapping]] = ..., id: _Optional[int] = ..., is_resting: bool = ...) -> None: ...
