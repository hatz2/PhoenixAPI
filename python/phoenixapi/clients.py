from abc import ABC
from .client_socket import ClientSocket, Request, Response
from typing import TypedDict
from .entities import Position, Player, EntityType

class Client(ABC):
    def __init__(self, service_name: str, socket: ClientSocket):
        self._service_name = service_name
        self._socket = socket



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
        request_data: Request = {
            "service": self._service_name,
            "method": "getPlayerObjManager",
            "params": {}
        }

        response = self._socket.request(request_data)

        return PlayerObjManager(response["result"])

    def walk(self, x: int, y: int) -> Response:
        request_data: Request = {
            "service": self._service_name,
            "method": "walk",
            "params": {
                "x": x,
                "y": y
            }
        }

        return self._socket.request(request_data)
    
    def reset_player_state(self) -> None:
        request_data: Request = {
            "service": self._service_name,
            "method": "resetPlayerState",
            "params": {}
        }

        self._socket.request(request_data)

    def attack(self, entity_type: EntityType, entity_id: int, skill_id: int) -> Response:
        request_data: Request = {
            "service": self._service_name,
            "method": "attack",
            "params": {
                "entity_type": entity_type,
                "entity_id": entity_id,
                "skill_id": skill_id
            }
        }

        return self._socket.request(request_data)
    
    def pickup(self, item_id: int) -> Response:
        request_data: Request = {
            "service": self._service_name,
            "method": "pickup",
            "params": {
                "item_id": item_id
            }
        }

        return self._socket.request(request_data)
    
    def collect(self, npc_id: int) -> Response:
        request_data: Request = {
            "service": self._service_name,
            "method": "collect",
            "params": {
                "npc_id": npc_id
            }
        }

        return self._socket.request(request_data)
    
    def target(self, entity_type: EntityType, entity_id: int) -> Response:
        request_data: Request = {
            "service": self._service_name,
            "method": "target",
            "params": {
                "entity_type": entity_type,
                "entity_id": entity_id
            }
        }

        return self._socket.request(request_data)