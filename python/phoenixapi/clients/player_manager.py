from .client_socket import ClientSocket, Request, Response
from .base_client import Client
from typing import TypedDict
from ..entities import Position, EntityType, Player

class PlayerObjManager(TypedDict):
    position: Position
    dest_position: Position
    state: int
    player: Player
    id: int
    is_resting: bool


class PlayerObjManagerClient(Client):
    def __init__(self, socket: ClientSocket):
        super().__init__("PlayerObjManagerService", socket)

    def get_player_obj_manager(self) -> PlayerObjManager:
        request: Request = {
            "service": self._service_name,
            "method": "getPlayerObjManager",
            "params": {}
        }
        response = self._socket.request(request)
        return PlayerObjManager(response["result"])
            

    def walk(self, x: int, y: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "walk",
            "params": {
                "x": x,
                "y": y
            }
        }
        return self._socket.request(request)
    
    def reset_player_state(self) -> None:
        request: Request = {
            "service": self._service_name,
            "method": "resetPlayerState",
            "params": {}
        }
        self._socket.request(request)

    def attack(self, entity_type: EntityType, entity_id: int, skill_id: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "attack",
            "params": {
                "entity_type": entity_type,
                "entity_id": entity_id,
                "skill_id": skill_id
            }
        }
        return self._socket.request(request)
    
    def pickup(self, item_id: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "pickup",
            "params": {
                "item_id": item_id
            }
        }
        return self._socket.request(request)
    
    def collect(self, npc_id: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "collect",
            "params": {
                "npc_id": npc_id
            }
        }
        return self._socket.request(request)
    
    def target(self, entity_type: EntityType, entity_id: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "target",
            "params": {
                "entity_type": entity_type,
                "entity_id": entity_id
            }
        }
        return self._socket.request(request)