from abc import ABC
from .client_socket import ClientSocket

class Client(ABC):
    def __init__(self, service_name: str, socket: ClientSocket):
        self._service_name = service_name
        self._socket = socket