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
        """Returns an object containing information about the player."""
        request: Request = {
            "service": self._service_name,
            "method": "getPlayerObjManager",
            "params": {}
        }
        response = self._socket.request(request)
        return PlayerObjManager(response["result"])
            

    def walk(self, x: int, y: int) -> Response:
        """Walks with your character to the specified coordinates."""
        request: Request = {
            "service": self._service_name,
            "method": "walk",
            "params": {
                "x": x,
                "y": y
            }
        }
        return self._socket.request(request)
    
    def reset_player_state(self) -> Response:
        """This method allows you to reset the player state as if you are clicking in the ground. This is what makes the little arrow in the target's head go from red (attacking) to yellow (not attacking)."""
        request: Request = {
            "service": self._service_name,
            "method": "resetPlayerState",
            "params": {}
        }
        return self._socket.request(request)

    def attack(self, entity_type: EntityType, entity_id: int, skill_id: int) -> Response:
        """This method allows you to use skills. If you want to cast a skill that doesn't need a target you can pass an entity_type and entity_id values of 0."""
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
        """Walks and pick up the specified item in the ground."""
        request: Request = {
            "service": self._service_name,
            "method": "pickup",
            "params": {
                "item_id": item_id
            }
        }
        return self._socket.request(request)
    
    def collect(self, npc_id: int) -> Response:
        """Walks and collects the specified npc. This is used for stuff like fragant grass, ice flowers, lettuce, etc."""
        request: Request = {
            "service": self._service_name,
            "method": "collect",
            "params": {
                "npc_id": npc_id
            }
        }
        return self._socket.request(request)
    
    def target(self, entity_type: EntityType, entity_id: int) -> Response:
        """Targets and entity to show the target widget in game. It is not strictly needed for attacking but it is recommended to use it when attacking a new entity as you would do while playing with your hands."""
        request: Request = {
            "service": self._service_name,
            "method": "target",
            "params": {
                "entity_type": entity_type,
                "entity_id": entity_id
            }
        }
        return self._socket.request(request)