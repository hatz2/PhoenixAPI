
import grpc
from phoenixapi.clients import *


class Phoenix:
    """Main API Class. Contains all posible clients that you can interact with."""

    def __init__(self, port):
        channel = grpc.insecure_channel(f"localhost:{port}")

        self.player_manager = PlayerManagerClient(channel)
        self.packet_manager = PacketManagerClient(channel)
        self.skill_manager = SkillManagerClient(channel)
        self.scene_manager = SceneManagerClient(channel)
        self.inventory = InventoryManagerClient(channel)
