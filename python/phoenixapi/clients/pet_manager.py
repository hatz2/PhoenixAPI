from .client_socket import ClientSocket, Request, Response
from .base_client import Client
from ..entities import Npc, Position, EntityType
from enum import Enum
from typing import TypedDict

class PetState(int, Enum):
    D = 0
    S = 5
    F = 7
    WALK_AFTER_F = 8
    A = 12
    AFTER_A_CLICK = 15
    S_AFTER_A_F = 17


class PetObjManager(TypedDict):
    position: Position
    dest_position: Position
    state: PetState
    pet: Npc


class PetManager(Client):
    def __init__(self, socket: ClientSocket):
        super().__init__("PetManagerService", socket)

    def get_pets(self) -> list[PetObjManager]:
        request: Request = {
            "service": self._service_name,
            "method": "getPets",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["pets"])

    def get_current_pet(self) -> PetObjManager:
        request: Request = {
            "service": self._service_name,
            "method": "getCurrentPet",
            "params": {}
        }
        response = self._socket.request(request)
        return PetObjManager(response["result"])

    def get_current_partner(self) -> PetObjManager:
        request: Request = {
            "service": self._service_name,
            "method": "getCurrentPartner",
            "params": {}
        }
        response = self._socket.request(request)
        return PetObjManager(response["result"])

    def set_pet_state(self, pet_id: int, pet_state: PetState) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "setPetState",
            "params": {
                "pet_id": pet_id,
                "state": pet_state
            }
        }
        return self._socket.request(request)

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

    def auto_attack(self, entity_type: EntityType, entity_id: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "autoAttack",
            "params": {
                "entity_type": entity_type,
                "entity_id": entity_id
            }
        }
        return self._socket.request(request)

    def pet_attack(self, entity_type: EntityType, entity_id: int, skill_id: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "petAttack",
            "params": {
                "entity_type": entity_type,
                "entity_id": entity_id,
                "skill_id": skill_id
            }
        }
        return self._socket.request(request)

    def partner_attack(self, entity_type: EntityType, entity_id: int, skill_id: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "partnerAttack",
            "params": {
                "entity_type": entity_type,
                "entity_id": entity_id,
                "skill_id": skill_id
            }
        }
        return self._socket.request(request)