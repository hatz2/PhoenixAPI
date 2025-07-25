
from clients import PlayerManagerClient
import grpc

class Phoenix:
    """Main API Class. Contains all posible clients that you can interact with."""

    def __init__(self, port):
        with grpc.insecure_channel(f"localhost:{port}") as channel:
            self.player_manager_client = PlayerManagerClient(channel)
