from .client_socket import ClientSocket, Request, Response
from .base_client import Client
from ..entities import EntityType


class BotControllerClient(Client):
    """This client allows you to interact with the bot directly. It has methods to start and stop the farming and minigame bot and also allows you to load custom settings."""
    def __init__(self, socket: ClientSocket):
        super().__init__("BotControllerService", socket)

    def start_farming_bot(self) -> Response:
        """Starts the farming bot as if you press the Start button in the bot."""
        request: Request = {
            "service": self._service_name,
            "method": "startFarmingBot",
            "params": {}
        }
        return self._socket.request(request)

    def stop_farming_bot(self) -> Response:
        """Stops the farming bot as if you press the Stop button in the bot."""
        request: Request = {
            "service": self._service_name,
            "method": "stopFarmingBot",
            "params": {}
        }
        return self._socket.request(request)

    def continue_farming_bot(self) -> Response:
        """Continues the farming bot as if you press the Continue button in the bot."""
        request: Request = {
            "service": self._service_name,
            "method": "continueFarmingBot",
            "params": {}
        }
        return self._socket.request(request)

    def start_minigame_bot(self) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "startMinigameBot",
            "params": {}
        }
        return self._socket.request(request)

    def stop_minigame_bot(self) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "stopMinigameBot",
            "params": {}
        }
        return self._socket.request(request)

    def load_settings(self, ini_file_path: str) -> Response:
        """Loads a specific settings file into the bot."""
        request: Request = {
            "service": self._service_name,
            "method": "loadSettings",
            "params": {
                "ini_file_path": ini_file_path
            }
        }
        return self._socket.request(request)
    
    def attack(self, entity_type: EntityType, entity_id: int):
        """Attacks the desired entity using the skills configured in the bot."""
        request: Request = {
            "service": self._service_name,
            "method": "attack",
            "params": {
                "entity_type": entity_type,
                "entity_id": entity_id,
            }
        }
        return self._socket.request(request)