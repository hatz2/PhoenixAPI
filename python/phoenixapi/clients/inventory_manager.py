from .client_socket import ClientSocket, Request, Response
from .base_client import Client
from enum import Enum
from typing import TypedDict
from ..entities import EntityType

class InventoryTab(int, Enum):
    EQUIP = 0
    MAIN = 1
    ETC = 2


class InvSlot(TypedDict):
    inv_tab: InventoryTab
    index: int
    vnum: int
    quantity: int
    name: str


class InventoryManager(Client):
    def __init__(self, socket: ClientSocket):
        super().__init__("InventoryManagerService", socket)
        
    
    def get_gold(self) -> int:
        request: Request = {
            "service": self._service_name,
            "method": "getGold",
            "params": {}
        }
        response = self._socket.request(request)
        return response["result"]["gold"]

    def get_equip_tab(self) -> list[InvSlot]:
        request: Request = {
            "service": self._service_name,
            "method": "getEquipTab",
            "params": {}
        }
        response = self._socket.request(request)
        return response["result"]["inv_slots"]

    def get_main_tab(self) -> list[InvSlot]:
        request: Request = {
            "service": self._service_name,
            "method": "getMainTab",
            "params": {}
        }
        response = self._socket.request(request)
        return response["result"]["inv_slots"]

    def get_etc_tab(self) -> list[InvSlot]:
        request: Request = {
            "service": self._service_name,
            "method": "getEtcTab",
            "params": {}
        }
        response = self._socket.request(request)
        return response["result"]["inv_slots"]

    def get_inventory_slot(self, inv_tab: InventoryTab, slot_index: int) -> InvSlot:
        request: Request = {
            "service": self._service_name,
            "method": "getInventorySlot",
            "params": {
                "inv_tab": inv_tab,
                "slot_index": slot_index
            }
        }
        response = self._socket.request(request)
        return InvSlot(response["result"])

    def find_item(self, vnum: int) -> InvSlot:
        request: Request = {
            "service": self._service_name,
            "method": "findItem",
            "params": {
                "vnum": vnum
            }
        }
        response = self._socket.request(request)
        return InvSlot(response["result"])

    def use_item(self, vnum: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "useItem",
            "params": {
                "vnum": vnum
            }
        }
        return self._socket.request(request)

    def use_item_on_target(self, vnum: int, entity_type: EntityType, entity_id: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "useItemOnTarget",
            "params": {
                "vnum": vnum,
                "entity_type": entity_type,
                "entity_id": entity_id
            }
        }
        return self._socket.request(request)