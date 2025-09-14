from .client_socket import ClientSocket
from phoenixapi.clients import PlayerObjManagerClient


    
class PhoenixApi:
    def __init__(self, port: int):
        socket = ClientSocket(port)
        
        self.player_obj_manager = PlayerObjManagerClient(socket)

        # TODO: Instantiate client service consumers



