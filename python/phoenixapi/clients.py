from phoenixapi.protos.game.playermanager_pb2_grpc import PlayerManagerStub
from phoenixapi.protos.game.playermanager_pb2 import PlayerObjManager
from phoenixapi.protos.position_pb2 import Position
from google.protobuf.empty_pb2 import Empty

class PlayerManagerClient:
    """Allows querying data from your character and performing actions with it"""
    
    def __init__(self, channel):
        self._stub = PlayerManagerStub(channel)

    def get_player_obj_manager(self) -> PlayerObjManager:
        """Returns data about the game player manager struct"""
        return self._stub.GetPlayerObjManager(Empty())
    
    def walk(self, x: int, y: int) -> None:
        """Only your player walks to coords (x, y)"""
        pos = Position()
        pos.x = x
        pos.y = y
        return self._stub.Walk(pos)
    
    def reset_player_state(self) -> None:
        """Resets your player state as if you would click the ground"""
        return self._stub.ResetPlayerState(Empty())