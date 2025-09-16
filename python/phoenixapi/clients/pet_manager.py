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


class PetManagerClient(Client):
    """This client allows you to get information about your pets and perform actions with them like walking or attacking."""

    def __init__(self, socket: ClientSocket):
        super().__init__("PetManagerService", socket)

    def get_pets(self) -> list[PetObjManager]:
        """Returns a list with your current pets."""
        request: Request = {
            "service": self._service_name,
            "method": "getPets",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["pets"])

    def get_current_pet(self) -> PetObjManager:
        """Returns your current pet information."""
        request: Request = {
            "service": self._service_name,
            "method": "getCurrentPet",
            "params": {}
        }
        response = self._socket.request(request)
        return PetObjManager(response["result"])

    def get_current_partner(self) -> PetObjManager:
        """Returns your current partner information."""
        request: Request = {
            "service": self._service_name,
            "method": "getCurrentPartner",
            "params": {}
        }
        response = self._socket.request(request)
        return PetObjManager(response["result"])

    def set_pet_state(self, pet_id: int, pet_state: PetState) -> Response:
        """Changes the pet state to the specified state."""
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
        """Walks with all your current pets unless you put them on S state."""
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
        """Auto attack with all your current pets unless you put them on S state."""
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
        """Uses a pet skill on the specified target. If you want to use a skill that doesn't need a target you can set entity_type and entity_id to 0."""
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
        """Uses a partner skill on the specified target. If you want to use a skill that doesn't need a target you can set entity_type and entity_id to 0."""
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