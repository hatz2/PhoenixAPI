from .client_socket import ClientSocket, Request, Response
from .base_client import Client
from typing import TypedDict

class Friend(TypedDict):
    id: int
    name: str

class FriendManagerClient(Client):

    def __init__(self, socket: ClientSocket):
        super().__init__("FriendManagerService", socket)

    def get_friend_list(self) -> list[Friend]:
        request: Request = {
            "service": self._service_name,
            "method": "getFriendList",
            "params": {}
        }
        response = self._socket.request(request)
        return list(response["result"]["friends"])
    
    def join_miniland(self, friend_id: int) -> Response:
        request: Request = {
            "service": self._service_name,
            "method": "joinMiniland",
            "params": {
                "friend_id": friend_id
            }
        }
        return self._socket.request(request)