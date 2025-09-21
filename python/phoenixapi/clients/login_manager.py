from .client_socket import ClientSocket, Request, Response
from .base_client import Client
from typing import TypedDict
from enum import Enum

class Job(int, Enum):
    ADVENTURER = 0
    SWORDSMAN = 1
    ARCHER = 2
    MAGE = 3
    FIGHTER = 4


class CharacterSelectSlot(TypedDict):
    is_created: bool
    name: str
    job: Job


class LoginClient(Client):
    """This services allows you to logout from the game aswell as log back in."""

    def __init__(self, socket: ClientSocket):
        super().__init__("LoginService", socket)

    def logout(self) -> Response:
        """Allows you to logout from the world server and go back to the server selection screen."""
        request: Request = {
            "service": self._service_name,
            "method": "logout",
            "params": {}
        }
        return self._socket.request(request)

    def is_server_selection_visible(self) -> bool:
        """Returns true if the server selection screen is visible, false otherwise."""
        request: Request = {
            "service": self._service_name,
            "method": "isServerSelectionVisible",
            "params": {}
        }
        response = self._socket.request(request)
        return response["result"]["visible"]

    def is_character_selection_visible(self) -> bool:
        """Returns true if the character selection screen is visible, false otherwise."""
        request: Request = {
            "service": self._service_name,
            "method": "isCharacterSelectionVisible",
            "params": {}
        }
        response = self._socket.request(request)
        return response["result"]["visible"]

    def get_character_slots(self) -> list[CharacterSelectSlot]:
        """Returns a list with your character slots information."""
        request: Request = {
            "service": self._service_name,
            "method": "getCharacterSlots",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["character_slots"])

    def select_language(self, lang_index: int) -> Response:
        """Choose a language server from the server selection screen. The lang_index parameter starts from 0."""
        request: Request = {
            "service": self._service_name,
            "method": "selectLanguage",
            "params": {
                "lang_index": lang_index
            }
        }
        return self._socket.request(request)

    def select_server(self, server_index: int) -> Response:
        """Choose a server from the server selection screen. The server_index parameter starts from 0"""
        request: Request = {
            "service": self._service_name,
            "method": "selectServer",
            "params": {
                "server_index": server_index
            }
        }
        return self._socket.request(request)

    def select_channel(self, channel_index: int) -> Response:
        """Choose a channel from the server selection screen. The channel_index parameter starts from 0."""
        request: Request = {
            "service": self._service_name,
            "method": "selectChannel",
            "params": {
                "channel_index": channel_index
            }
        }
        return self._socket.request(request)

    def select_character(self, character_index: int) -> Response:
        """Choose a character from the character selection screen and starts the game. The character_index parameter starts from 0."""
        request: Request = {
            "service": self._service_name,
            "method": "selectCharacter",
            "params": {
                "character_index": character_index
            }
        }
        return self._socket.request(request)

    def relog(self, server_index: int, channel_index: int, character_index: int = -1) -> Response:
        """
        This method is an all in one, it will perform the following actions:

        1. Logout your character
        2. Selects the specified server
        3. Selects the specified channel
        4. Selects the specified character

        This method will block your current thread and will only return once the entire process has been completed. If the channel you are attempting to join is full the method will keep trying to join it indefinetly. If you want to stay at the character selection screen you can use a value of -1 for the character_index parameter.
        """
        request: Request = {
            "service": self._service_name,
            "method": "relog",
            "params": {
                "server_index": server_index,
                "channel_index": channel_index,
                "character_index": character_index
            }
        }
        return self._socket.request(request)