import uuid
from grpc import Channel
from phoenixapi.protos.position_pb2 import Position
from google.protobuf.empty_pb2 import Empty
from phoenixapi.protos.game.entities_pb2 import EntityType, Player, Monster, Item, Npc
from phoenixapi.protos.game.playermanager_pb2_grpc import PlayerManagerStub
from phoenixapi.protos.game.playermanager_pb2 import PlayerObjManager, AttackRequest, PickUpRequest, CollectRequest
from phoenixapi.protos.game.packetmanager_pb2_grpc import PacketManagerStub
from phoenixapi.protos.game.packetmanager_pb2 import Identifier, Packet
from phoenixapi.protos.game.skillmanager_pb2_grpc import SkillManagerStub
from phoenixapi.protos.game.skillmanager_pb2 import Skill, FindSkillFromIdRequest, FindSkillFromVnumRequest
from phoenixapi.protos.game.scenemanager_pb2_grpc import SceneManagerStub
from phoenixapi.protos.game.scenemanager_pb2 import FindRequest, MapGrid


class PlayerManagerClient:
    """Allows querying data from your character and performing actions with it"""
    
    def __init__(self, channel: Channel):
        self._stub = PlayerManagerStub(channel)

    def get_player_obj_manager(self) -> PlayerObjManager:
        """Returns data about the game player manager struct"""
        return self._stub.GetPlayerObjManager(Empty())
    
    def walk(self, x: int, y: int) -> None:
        """Only your player walks to coords (x, y)"""
        pos = Position()
        pos.x = x
        pos.y = y
        self._stub.Walk(pos)
    
    def reset_player_state(self) -> None:
        """Resets your player state as if you would click the ground"""
        self._stub.ResetPlayerState(Empty())
    
    def attack(self, entity_type: EntityType, entity_id: int, skill_id: int) -> None:
        request = AttackRequest()
        request.entity_type = entity_type
        request.entity_id = entity_id
        request.skill_id = skill_id
        self._stub.Attack(request)
    
    def pick_up(self, item_id: int) -> None:
        request = PickUpRequest()
        request.item_id = item_id
        self._stub.PickUp(request)

    def collect(self, npc_id: int) -> None:
        request = CollectRequest()
        request.npc_id = npc_id
        self._stub.Collect(request)
    

class PacketManagerClient:
    """Allows interacting with game packets"""

    def __init__(self, channel: Channel):
        self._stub = PacketManagerStub(channel)
        self.identifier = Identifier()
        self.identifier.id = str(uuid.uuid4())
        self.subscribed = False

    def __del__(self):
        if self.subscribed:
           self.unsubscribe()

    def subscribe(self) -> None:
        """Subscribe to receive packets from the bot"""
        self.subscribed = True
        self._stub.Subscribe(self.identifier)
    
    def unsubscribe(self) -> None:
        """Unsubscribe to free up the resources created in the bot when you subscribed"""
        self.subscribed = False
        self._stub.Unsubscribe(self.identifier)
    
    def get_pending_send_packets(self) -> list[Packet]:
        """Returns the pending send packets that haven't been processed yet"""
        return self._stub.GetPendingSendPackets(self.identifier)
    
    def get_pending_recv_packets(self) -> list[Packet]:
        """Returns the pending recv packets that haven't been processed yet"""
        return self._stub.GetPendingRecvPackets(self.identifier)
    
    def send(self, packet: str) -> None:
        """Send a packet to the game server"""
        grpc_packet = Packet()
        grpc_packet.data = packet
        self._stub.Send(grpc_packet)

    def recv(self, packet: str) -> None:
        """Fake receive a packet in the game client"""
        grpc_packet = Packet()
        grpc_packet.data = packet
        self._stub.Recv(grpc_packet)


class SkillManagerClient:
    """Allows interaction with your character skills"""

    def __init__(self, channel: Channel):
        self._stub = SkillManagerStub(channel)

    def get_skills(self) -> list[Skill]:
        """Return your skills in an iterable class"""
        return self._stub.GetSkills(Empty())
    
    def find_skill_from_vnum(self, vnum: int) -> Skill:
        """Returns the skill matching the vnum"""
        request = FindSkillFromVnumRequest()
        request.vnum = vnum
        return self._stub.FindSkillFromVnum(request)
    
    def find_skill_from_id(self, id: int) -> Skill:
        """Returns the skill matching the id"""
        request = FindSkillFromIdRequest()
        request.id = id
        return self._stub.FindSkillFromId(request)
    

class SceneManagerClient:
    """Allows interaction with the game scene"""

    def __init__(self, channel: Channel):
        self._stub = SceneManagerStub(channel)

    def get_players(self) -> list[Player]:
        return self._stub.GetPlayers(Empty())
    
    def get_monsters(self) -> list[Monster]:
        return self._stub.GetMonsters(Empty())
    
    def get_items(self) -> list[Item]:
        return self._stub.GetItems(Empty())
    
    def get_npcs(self) -> list[Npc]:
        return self._stub.GetNpcs(Empty())
    
    def find_player(self, player_id: int) -> Player:
        request = FindRequest()
        request.id = player_id
        return self._stub.FindPlayer(request)
    
    def find_monster(self, monster_id: int) -> Monster:
        request = FindRequest()
        request.id = monster_id
        return self._stub.FindMonster(request)
    
    def find_npc(self, npc_id: int) -> Npc:
        request = FindRequest()
        request.id = npc_id
        return self._stub.FindNpc(request)
    
    def find_item(self, item_id: int) -> Item:
        request = FindRequest()
        request.id = item_id
        return self._stub.FindItem(request)
    
    def get_all_bosses(self) -> list[Monster]:
        return self._stub.GetAllBosses(Empty())
    
    def get_map_grid(self) -> MapGrid:
        return self._stub.GetMapGrid(Empty())
