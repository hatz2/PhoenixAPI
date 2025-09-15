from .client_socket import ClientSocket, Request, Response
from .base_client import Client


class BotController(Client):
    def __init__(self, socket: ClientSocket):
        super().__init__("BotControllerService", socket)

    def start_farming_bot(self) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "startFarmingBot",
            "params": {}
        }
        return self._socket.request(request)

    def stop_farming_bot(self) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "stopFarmingBot",
            "params": {}
        }
        return self._socket.request(request)

    def continue_farming_bot(self) -> Response:
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
            "method": "stopFarmingBot",
            "params": {}
        }
        return self._socket.request(request)

    def load_settings(self, ini_file_path: str) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "loadSettings",
            "params": {
                "ini_file_path": ini_file_path
            }
        }
        return self._socket.request(request)