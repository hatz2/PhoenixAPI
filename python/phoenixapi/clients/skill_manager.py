from .client_socket import ClientSocket, Request, Response
from .base_client import Client
from enum import Enum
from typing import TypedDict

class SkillType(int, Enum):
    DAMAGE = 0
    DEBUFF = 1
    BUFF = 2


class TargetType(int, Enum):
    TARGET = 0
    SELF = 1
    SELF_OR_TARGET = 2
    NO_TARGET = 3


class Skill(TypedDict):
    vnum: int
    name: str 
    id: int
    type: SkillType
    range: int
    area: int
    cast_time: int
    cool_time: int
    mana_cost: int


class SkillManager(Client):
    def __init__(self, socket: ClientSocket):
        super().__init__("SkillManagerService", socket)

    def get_skills(self) -> list[Skill]:
        request: Request = {
            "service": self._service_name,
            "method": "getSkills",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["skills"])

    def find_skill_from_id(self, skill_id: int) -> Skill:
        request: Request = {
            "service": self._service_name,
            "method": "findSkillFromId",
            "params": {
                "id": skill_id
            }
        }
        response = self._socket.request(request)
        return Skill(response["result"])

    def find_skill_from_vnum(self, vnum: int) -> Skill:
        request: Request = {
            "service": self._service_name,
            "method": "findSkillFromVnum",
            "params": {
                "vnum": vnum
            }
        }
        response = self._socket.request(request)
        return Skill(response["result"])

    def get_pet_skills(self) -> list[Skill]:
        request: Request = {
            "service": self._service_name,
            "method": "getPetSkills",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["skills"])

    def find_pet_skill_from_id(self, skill_id: int) -> Skill:
        request: Request = {
            "service": self._service_name,
            "method": "findPetSkillFromId",
            "params": {
                "id": skill_id
            }
        }
        response = self._socket.request(request)
        return Skill(response["result"])

    def find_pet_skill_from_vnum(self, vnum: int) -> Skill:
        request: Request = {
            "service": self._service_name,
            "method": "findPetSkillFromVnum",
            "params": {
                "vnum": vnum
            }
        }
        response = self._socket.request(request)
        return Skill(response["result"])

    def get_partner_skills(self) -> list[Skill]:
        request: Request = {
            "service": self._service_name,
            "method": "getPartnerSkills",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["skills"])

    def find_partner_skill_from_id(self, skill_id: int) -> Skill:
        request: Request = {
            "service": self._service_name,
            "method": "findPartnerSkillFromId",
            "params": {
                "id": skill_id
            }
        }
        response = self._socket.request(request)
        return Skill(response["result"])

    def find_partner_skill_from_vnum(self, vnum: int) -> Skill:
        request: Request = {
            "service": self._service_name,
            "method": "findPartnerSkillFromVnum",
            "params": {
                "vnum": vnum
            }
        }
        response = self._socket.request(request)
        return Skill(response["result"])