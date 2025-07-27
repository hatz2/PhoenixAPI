
import grpc
from phoenixapi.clients import PlayerManagerClient
from phoenixapi.clients import PacketManagerClient
from phoenixapi.clients import SkillManagerClient

class Phoenix:
    """Main API Class. Contains all posible clients that you can interact with."""

    def __init__(self, port):
        channel = grpc.insecure_channel(f"localhost:{port}")

        self.player_manager_client = PlayerManagerClient(channel)
        self.packet_manager_client = PacketManagerClient(channel)
        self.skill_manager_client = SkillManagerClient(channel)
