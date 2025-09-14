from .clients.client_socket import ClientSocket
from .clients.player_manager import PlayerObjManagerClient
from .clients.scene_manager import SceneManagerClient


    
class PhoenixApi:
    def __init__(self, port: int):
        socket = ClientSocket(port)
        
        self.player_obj_manager = PlayerObjManagerClient(socket)
        self.scene_manager = SceneManagerClient(socket)



