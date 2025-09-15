from socket import socket, AF_INET, SOCK_STREAM
from typing import TypedDict, NotRequired
import json

class Request(TypedDict):
    service: str
    method: str
    params: dict

class Response(TypedDict):
    status: str
    error_message: NotRequired[str]
    result: NotRequired[str]

class ClientSocket:
    DELIM_CHAR = '\1'

    def __init__(self, port: int):
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.connect(("localhost", port))

    def __del__(self):
        self._socket.close()

    def request(self, request_data: Request) -> Response:
        self._send(json.dumps(request_data))
        response = Response(json.loads(self._recv()))
        self._validate_response(response)
        return response
        
    def _send(self, data: str):
        total_bytes_sent = 0
        buffer = data + ClientSocket.DELIM_CHAR

        while total_bytes_sent < len(buffer):
            bytes_sent = self._socket.send(buffer[total_bytes_sent:].encode())
            if bytes_sent == 0:
                raise RuntimeError("socket connection broken")
            total_bytes_sent += bytes_sent

    def _recv(self) -> str:
        chunks = []
        finish = False

        while not finish:
            chunk = self._socket.recv(4096)
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            finish = chunk.endswith(ClientSocket.DELIM_CHAR.encode())

        return b''.join(chunks)[:-1].decode()
    
    def _validate_response(self, response: Response) -> None:
        if response["status"] == "error":
            raise RuntimeError(response["error_message"])