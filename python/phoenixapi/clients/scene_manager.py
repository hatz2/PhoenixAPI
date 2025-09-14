from .client_socket import ClientSocket, Request
from .base_client import Client
from typing import TypedDict
from ..entities import Player, Npc, Monster, Item, Npc
from enum import Enum
    
class Cell(int, Enum):
    WALKABLE = 0
    OBSTACLE = 1
    OBSTACLE_2 = 2


class MapGrid(TypedDict):
    width: int
    height: int
    grid: list[list[Cell]]


class SceneManagerClient(Client):
    def __init__(self, socket: ClientSocket):
        super().__init__("SceneManagerService", socket)

    def get_players(self) -> list[Player]:
        request: Request = {
            "service": self._service_name,
            "method": "getPlayers",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["players"])
    
    def get_monsters(self) -> list[Monster]:
        request: Request = {
            "service": self._service_name,
            "method": "getMonsters",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["monsters"])
    
    def get_items(self) -> list[Item]:
        request: Request = {
            "service": self._service_name,
            "method": "getItems",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["items"])
    
    def get_npcs(self) -> list[Npc]:
        request: Request = {
            "service": self._service_name,
            "method": "getNpcs",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["npcs"])
    
    def find_player(self, player_id: int) -> Npc:
        request: Request = {
            "service": self._service_name,
            "method": "findPlayer",
            "params": {
                "id": player_id
            }
        }
        response = self._socket.request(request)
        return Npc(response["result"])
    
    def find_monster(self, monster_id: int) -> Monster:
        request: Request = {
            "service": self._service_name,
            "method": "findMonster",
            "params": {
                "id": monster_id
            }
        }
        response = self._socket.request(request)
        return Monster(response["result"])
    
    def find_item(self, item_id: int) -> Item:
        request: Request = {
            "service": self._service_name,
            "method": "findItem",
            "params": {
                "id": item_id
            }
        }
        response = self._socket.request(request)
        return Item(response["result"])
    
    def find_npc(self, npc_id: int) -> Npc:
        request: Request = {
            "service": self._service_name,
            "method": "findNpc",
            "params": {
                "id": npc_id
            }
        }
        response = self._socket.request(request)
        return Npc(response["result"])
    
    def get_all_bosses(self) -> list[Monster]:
        request: Request = {
            "service": self._service_name,
            "method": "getAllBosses",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["bosses"])
    
    def get_map_grid(self) -> MapGrid:
        request: Request = {
            "service": self._service_name,
            "method": "getMapGrid",
            "params": {}
        }
        response = self._socket.request(request)
        return MapGrid(response["result"])