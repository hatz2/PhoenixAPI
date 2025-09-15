from .clients.client_socket import ClientSocket
from .clients.player_manager import PlayerObjManagerClient
from .clients.scene_manager import SceneManagerClient
from .clients.packet_manager import PacketManager
from .clients.skill_manager import SkillManager
from .clients.pet_manager import PetManager
    
class PhoenixApi:
    def __init__(self, port: int):
        socket = ClientSocket(port)
        
        self.player_obj_manager = PlayerObjManagerClient(socket)
        self.scene_manager = SceneManagerClient(socket)
        self.packet_manager = PacketManager(socket)
        self.skill_manager = SkillManager(socket)
        self.pet_manager = PetManager(socket)