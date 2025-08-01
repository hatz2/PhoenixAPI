from google.protobuf import empty_pb2 as _empty_pb2
from phoenixapi.protos.game import entities_pb2 as _entities_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InventoryTabType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVENTORY_TAB_TYPE_EQUIP: _ClassVar[InventoryTabType]
    INVENTORY_TAB_TYPE_MAIN: _ClassVar[InventoryTabType]
    INVENTORY_TAB_TYPE_ETC: _ClassVar[InventoryTabType]

class UseItemResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USE_ITEM_RESPONSE_TYPE_UNSPECIFIED: _ClassVar[UseItemResponseType]
    USE_ITEM_RESPONSE_TYPE_USED: _ClassVar[UseItemResponseType]
    USE_ITEM_RESPONSE_TYPE_NOT_FOUND: _ClassVar[UseItemResponseType]
    USE_ITEM_RESPONSE_TYPE_TARGET_NOT_FOUND: _ClassVar[UseItemResponseType]
    USE_ITEM_RESPONSE_TYPE_WRONG_PARAMETERS: _ClassVar[UseItemResponseType]
INVENTORY_TAB_TYPE_EQUIP: InventoryTabType
INVENTORY_TAB_TYPE_MAIN: InventoryTabType
INVENTORY_TAB_TYPE_ETC: InventoryTabType
USE_ITEM_RESPONSE_TYPE_UNSPECIFIED: UseItemResponseType
USE_ITEM_RESPONSE_TYPE_USED: UseItemResponseType
USE_ITEM_RESPONSE_TYPE_NOT_FOUND: UseItemResponseType
USE_ITEM_RESPONSE_TYPE_TARGET_NOT_FOUND: UseItemResponseType
USE_ITEM_RESPONSE_TYPE_WRONG_PARAMETERS: UseItemResponseType

class GoldResponse(_message.Message):
    __slots__ = ("gold",)
    GOLD_FIELD_NUMBER: _ClassVar[int]
    gold: int
    def __init__(self, gold: _Optional[int] = ...) -> None: ...

class InvSlot(_message.Message):
    __slots__ = ("inv_tab", "index", "vnum", "quantity", "name")
    INV_TAB_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    VNUM_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    inv_tab: InventoryTabType
    index: int
    vnum: int
    quantity: int
    name: str
    def __init__(self, inv_tab: _Optional[_Union[InventoryTabType, str]] = ..., index: _Optional[int] = ..., vnum: _Optional[int] = ..., quantity: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class InventorySlotRequest(_message.Message):
    __slots__ = ("inv_tab_type", "index")
    INV_TAB_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    inv_tab_type: InventoryTabType
    index: int
    def __init__(self, inv_tab_type: _Optional[_Union[InventoryTabType, str]] = ..., index: _Optional[int] = ...) -> None: ...

class FindItemRequest(_message.Message):
    __slots__ = ("vnum",)
    VNUM_FIELD_NUMBER: _ClassVar[int]
    vnum: int
    def __init__(self, vnum: _Optional[int] = ...) -> None: ...

class InvSlotList(_message.Message):
    __slots__ = ("inv_slots",)
    INV_SLOTS_FIELD_NUMBER: _ClassVar[int]
    inv_slots: _containers.RepeatedCompositeFieldContainer[InvSlot]
    def __init__(self, inv_slots: _Optional[_Iterable[_Union[InvSlot, _Mapping]]] = ...) -> None: ...

class UseItemRequest(_message.Message):
    __slots__ = ("vnum",)
    VNUM_FIELD_NUMBER: _ClassVar[int]
    vnum: int
    def __init__(self, vnum: _Optional[int] = ...) -> None: ...

class UseItemOnTargetRequest(_message.Message):
    __slots__ = ("vnum", "target_id", "target_type")
    VNUM_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    vnum: int
    target_id: int
    target_type: _entities_pb2.EntityType
    def __init__(self, vnum: _Optional[int] = ..., target_id: _Optional[int] = ..., target_type: _Optional[_Union[_entities_pb2.EntityType, str]] = ...) -> None: ...

class UseItemResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: UseItemResponseType
    def __init__(self, response: _Optional[_Union[UseItemResponseType, str]] = ...) -> None: ...
