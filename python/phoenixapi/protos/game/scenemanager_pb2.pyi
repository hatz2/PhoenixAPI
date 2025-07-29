from google.protobuf import empty_pb2 as _empty_pb2
from phoenixapi.protos.game import entities_pb2 as _entities_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CellType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CELL_TYPE_WALKABLE: _ClassVar[CellType]
    CELL_TYPE_OBSTACLE: _ClassVar[CellType]
    CELL_TYPE_OBSTACLE_2: _ClassVar[CellType]
CELL_TYPE_WALKABLE: CellType
CELL_TYPE_OBSTACLE: CellType
CELL_TYPE_OBSTACLE_2: CellType

class FindRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class MapGrid(_message.Message):
    __slots__ = ("width", "height", "rows")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    rows: _containers.RepeatedCompositeFieldContainer[Row]
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., rows: _Optional[_Iterable[_Union[Row, _Mapping]]] = ...) -> None: ...

class Row(_message.Message):
    __slots__ = ("cells",)
    CELLS_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedScalarFieldContainer[CellType]
    def __init__(self, cells: _Optional[_Iterable[_Union[CellType, str]]] = ...) -> None: ...
