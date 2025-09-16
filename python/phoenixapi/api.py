from .clients.client_socket import ClientSocket
from .clients.player_manager import PlayerObjManagerClient
from .clients.scene_manager import SceneManagerClient
from .clients.packet_manager import PacketManagerClient
from .clients.skill_manager import SkillManagerClient
from .clients.pet_manager import PetManagerClient
from .clients.inventory_manager import InventoryManagerClient
from .clients.bot_controller import BotControllerClient
from .clients.friend_manager import FriendManagerClient
    
class PhoenixApi:
    def __init__(self, port: int):
        socket = ClientSocket(port)
        
        self.player_obj_manager = PlayerObjManagerClient(socket)
        self.scene_manager = SceneManagerClient(socket)
        self.packet_manager = PacketManagerClient(socket)
        self.skill_manager = SkillManagerClient(socket)
        self.pet_manager = PetManagerClient(socket)
        self.inventory_manager = InventoryManagerClient(socket)
        self.bot_controller = BotControllerClient(socket)
        self.friend_manager = FriendManagerClient(socket)