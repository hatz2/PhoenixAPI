from .client_socket import ClientSocket, Request, Response
from .base_client import Client
from uuid import uuid4

class PacketManagerClient(Client):
    def __init__(self, socket: ClientSocket):
        """This service allows you to read the network traffic that is being exchanged between the game's client and the game's server. It also allows you to send your own packets and fake receive them."""
        super().__init__("PacketManagerService", socket)
        self._id = str(uuid4())
        self._subscribed = False

    def __del__(self):
        if self._subscribed:
            self.unsubscribe()

    def subscribe(self) -> Response:
        """This method lets the bot know that you want to start reading packets and allocates the resources needed for your client. It excpets an id which can be anything really but I recommend to use any kind of uuid. If you want to start reading packets you must call this function beforehand."""
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
        """This method lets the bot know that you don't want to read packets anymore and frees the resources previously allocated when you subscribed."""
        request: Request = {
            "service": self._service_name,
            "method": "unsubscribe",
            "params": {
                "id": self._id
            }
        }
        return self._socket.request(request)

    def get_pending_send_packets(self) -> list[str]:
        """Returns a list with the pending packets that the game's client has sent to the game's server. Once called the bot will remove the packets from the allocated resources for your app."""
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
        """Returns a list with the pending packets that the game's client has received from the game's server to be processed by your application. Once called the bot will remove the packets from the allocated resources for your app."""
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
        """Sends a packet to the game's server."""
        request: Request = {
            "service": self._service_name,
            "method": "send",
            "params": {
                "packet": packet
            }
        }
        return self._socket.request(request)

    def recv(self, packet: str) -> Response:
        """Fake receives a packet in the game's client."""
        request: Request = {
            "service": self._service_name,
            "method": "recv",
            "params": {
                "packet": packet
            }
        }
        return self._socket.request(request)