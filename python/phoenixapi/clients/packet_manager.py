from .client_socket import ClientSocket, Request, Response
from .base_client import Client
from uuid import uuid4

class PacketManager(Client):
    def __init__(self, socket: ClientSocket):
        super().__init__("PacketManagerService", socket)
        self._id = str(uuid4())
        self._subscribed = False

    def __del__(self):
        if self._subscribed:
            self.unsubscribe()

    def subscribe(self) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "subscribe",
            "params": {
                "id": self._id
            }
        }
        response = self._socket.request(request)
        self._subscribed = response["status"] == "ok"
        return response

    def unsubscribe(self) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "unsubscribe",
            "params": {
                "id": self._id
            }
        }
        return self._socket.request(request)

    def get_pending_send_packets(self) -> list[str]:
        request: Request = {
            "service": self._service_name,
            "method": "getPendingSendPackets",
            "params": {
                "id": self._id
            }
        }
        response = self._socket.request(request)
        return list(response["result"]["packets"])
        

    def get_pending_recv_packets(self) -> list[str]:
        request: Request = {
            "service": self._service_name,
            "method": "getPendingRecvPackets",
            "params": {
                "id": self._id
            }
        }
        response = self._socket.request(request)
        return list(response["result"]["packets"])

    def send(self, packet: str) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "send",
            "params": {
                "packet": packet
            }
        }
        return self._socket.request(request)

    def recv(self, packet: str) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "recv",
            "params": {
                "packet": packet
            }
        }
        return self._socket.request(request)