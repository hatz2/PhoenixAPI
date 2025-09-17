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


class InventoryManagerClient(Client):
    """This client allows you to get information about your inventory aswell as using items."""

    def __init__(self, socket: ClientSocket):
        super().__init__("InventoryManagerService", socket)
        
    
    def get_gold(self) -> int:
        """Returns the gold you have in the inventory."""
        request: Request = {
            "service": self._service_name,
            "method": "getGold",
            "params": {}
        }
        response = self._socket.request(request)
        return response["result"]["gold"]

    def get_equip_tab(self) -> list[InvSlot]:
        """Returns a list of the inventory slots from your EQUIP tab."""
        request: Request = {
            "service": self._service_name,
            "method": "getEquipTab",
            "params": {}
        }
        response = self._socket.request(request)
        return response["result"]["inv_slots"]

    def get_main_tab(self) -> list[InvSlot]:
        """Returns a list of the inventory slots from your MAIN tab."""
        request: Request = {
            "service": self._service_name,
            "method": "getMainTab",
            "params": {}
        }
        response = self._socket.request(request)
        return response["result"]["inv_slots"]

    def get_etc_tab(self) -> list[InvSlot]:
        """Returns a list of the inventory slots from your ETC tab."""
        request: Request = {
            "service": self._service_name,
            "method": "getEtcTab",
            "params": {}
        }
        response = self._socket.request(request)
        return response["result"]["inv_slots"]

    def get_inventory_slot(self, inv_tab: InventoryTab, slot_index: int) -> InvSlot:
        """Returns an inventory slot from the specified tab and index."""
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
        """Searchs for the item with the given vnum. Returns the inventory slot if found, otherwise returns an error."""
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
        """Uses an item from the inventory with the given vnum. If the item is not found it returns an error."""
        request: Request = {
            "service": self._service_name,
            "method": "useItem",
            "params": {
                "vnum": vnum
            }
        }
        return self._socket.request(request)

    def use_item_on_target(self, vnum: int, entity_type: EntityType, entity_id: int) -> Response:
        """Uses an item from the inventory with the given vnum on the specified target. If the item is not found or the target is not found it returns an error."""
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