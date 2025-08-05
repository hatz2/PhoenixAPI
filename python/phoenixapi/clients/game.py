import uuid
from grpc import Channel
from grpc._channel import _MultiThreadedRendezvous
from phoenixapi.protos.position_pb2 import Position
from google.protobuf.empty_pb2 import Empty
from phoenixapi.protos.game.entities_pb2 import EntityType, Player, Monster, Item, Npc
from phoenixapi.protos.game.playermanager_pb2_grpc import PlayerManagerStub
from phoenixapi.protos.game.playermanager_pb2 import PlayerObjManager, AttackRequest, PickUpRequest, CollectRequest, TargetRequest
from phoenixapi.protos.game.packetmanager_pb2_grpc import PacketManagerStub
from phoenixapi.protos.game.packetmanager_pb2 import Identifier, Packet
from phoenixapi.protos.game.skillmanager_pb2_grpc import SkillManagerStub
from phoenixapi.protos.game.skillmanager_pb2 import Skill, FindSkillFromIdRequest, FindSkillFromVnumRequest
from phoenixapi.protos.game.scenemanager_pb2_grpc import SceneManagerStub
from phoenixapi.protos.game.scenemanager_pb2 import FindRequest, MapGrid
from phoenixapi.protos.game.inventorymanager_pb2_grpc import InventoryManagerStub
from phoenixapi.protos.game.inventorymanager_pb2 import InvSlot, InvSlotList, InventorySlotRequest, GoldResponse, InventoryTabType, FindItemRequest, UseItemResponseType, UseItemRequest, UseItemResponse, UseItemOnTargetRequest
from phoenixapi.protos.game.petmanager_pb2_grpc import PetManagerStub
from phoenixapi.protos.game.petmanager_pb2 import PetObjManager, PetStateRequest, PetState, PetObjManagerList, AutoAttackRequest

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

    def target(self, entity_type: EntityType, entity_id: int) -> None:
        request = TargetRequest()
        request.entity_type = entity_type
        request.entity_id = entity_id
        self._stub.Target(request)
    

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
    
    def get_pending_send_packets(self) -> _MultiThreadedRendezvous:
        """Returns the pending send packets that haven't been processed yet as an iterable object"""
        return self._stub.GetPendingSendPackets(self.identifier)
    
    def get_pending_recv_packets(self) -> _MultiThreadedRendezvous:
        """Returns the pending recv packets that haven't been processed yet as an iterable object"""
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
        skill_list = self._stub.GetSkills(Empty())
        return list(skill_list.skills)
    
    def find_skill_from_vnum(self, vnum: int) -> Skill:
        request = FindSkillFromVnumRequest()
        request.vnum = vnum
        return self._stub.FindSkillFromVnum(request)
    
    def find_skill_from_id(self, id: int) -> Skill:
        request = FindSkillFromIdRequest()
        request.id = id
        return self._stub.FindSkillFromId(request)
    
    def get_pet_skills(self) -> list[Skill]:
        skill_list = self._stub.GetPetSkills(Empty())
        return list(skill_list.skills)
    
    def find_pet_skill_from_vnum(self, vnum: int) -> Skill:
        request = FindSkillFromVnumRequest()
        request.vnum = vnum
        return self._stub.FindPetSkillFromVnum(request)
    
    def find_pet_skill_from_id(self, id: int) -> Skill:
        request = FindSkillFromIdRequest()
        request.id = id
        return self._stub.FindPetSkillFromId(request)
    
    def get_partner_skills(self) -> list[Skill]:
        skill_list = self._stub.GetPartnerSkills(Empty())
        return list(skill_list.skills)
    
    def find_partner_skill_from_vnum(self, vnum: int) -> Skill:
        request = FindSkillFromVnumRequest()
        request.vnum = vnum
        return self._stub.FindPartnerSkillFromVnum(request)
    
    def find_partner_skill_from_id(self, id: int) -> Skill:
        request = FindSkillFromIdRequest()
        request.id = id
        return self._stub.FindPartnerSkillFromId(request)
    

class SceneManagerClient:
    """Allows interaction with the game scene"""

    def __init__(self, channel: Channel):
        self._stub = SceneManagerStub(channel)

    def get_players(self) -> list[Player]:
        player_list = self._stub.GetPlayers(Empty())
        return list(player_list.players)
    
    def get_monsters(self) -> list[Monster]:
        monster_list = self._stub.GetMonsters(Empty())
        return list(monster_list.monsters)
    
    def get_items(self) -> list[Item]:
        item_list = self._stub.GetItems(Empty())
        return list(item_list.items)
    
    def get_npcs(self) -> list[Npc]:
        npc_list = self._stub.GetNpcs(Empty())
        return list(npc_list.npcs)
    
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
        monster_list = self._stub.GetAllBosses(Empty())
        return list(monster_list.monsters)
    
    def get_map_grid(self) -> MapGrid:
        return self._stub.GetMapGrid(Empty())
    
class InventoryManagerClient:
    """Allows interaction with your character inventory"""

    def __init__(self, channel: Channel):
        self._stub = InventoryManagerStub(channel)

    def get_gold(self) -> int:
        response: GoldResponse = self._stub.GetGold(Empty())
        return response.gold
    
    def get_equip_tab(self) -> list[InvSlot]:
        response: InvSlotList = self._stub.GetEquipTab(Empty())
        return list(response.inv_slots)
    
    def get_main_tab(self) -> list[InvSlot]:
        response: InvSlotList = self._stub.GetMainTab(Empty())
        return list(response.inv_slots)
    
    def get_etc_tab(self) -> list[InvSlot]:
        response: InvSlotList = self._stub.GetEtcTab(Empty())
        return list(response.inv_slots)
    
    def get_inventory_slot(self, inv_tab: InventoryTabType, index: int) -> InvSlot:
        request = InventorySlotRequest()
        request.inv_tab_type = inv_tab
        request.index = index
        return self._stub.GetInventorySlot(request)
    
    def find_item(self, vnum: int) -> InvSlot:
        request = FindItemRequest()
        request.vnum = vnum
        return self._stub.FindItem(request)
    
    def use_item(self, vnum: int) -> UseItemResponseType:
        request = UseItemRequest()
        request.vnum = vnum
        response: UseItemResponse = self._stub.UseItem(request)
        return response.response
    
    def use_item_on_target(self, vnum: int, target_type: EntityType, target_id: int) -> UseItemResponseType:
        request = UseItemOnTargetRequest()
        request.vnum = vnum
        request.target_type = target_type
        request.target_id = target_id
        response = self._stub.UseItemOnTarget(request)
        return response.response
    
class PetManagerClient:
    """Allows interaction with your pets"""

    def __init__(self, channel: Channel):
        self._stub = PetManagerStub(channel)

    def get_pets(self) -> list[PetObjManager]:
        pet_list: PetObjManagerList = self._stub.GetPets(Empty())
        return list(pet_list.pets)
    
    def get_current_pet(self) -> PetObjManager:
        return self._stub.GetCurrentPet(Empty())
    
    def get_current_partner(self) -> PetObjManager:
        return self._stub.GetCurrentPartner(Empty())
    
    def set_pet_state(self, pet_id: int, state: PetState) -> None:
        request = PetStateRequest()
        request.pet_id = pet_id
        request.new_state = state
        self._stub.SetPetState(request)

    def walk(self, x: int, y: int) -> None:
        request = Position()
        request.x = x
        request.y = y
        self._stub.Walk(request)

    def auto_attack(self, entity_type: EntityType, entity_id: int) -> None:
        request = AutoAttackRequest()
        request.entity_id = entity_id
        request.entity_type = entity_type
        self._stub.AutoAttack(request)

    def pet_attack(self, entity_type: EntityType, entity_id: int, skill_id: int) -> None:
        request = AttackRequest()
        request.entity_id = entity_id
        request.entity_type = entity_type
        request.skill_id = skill_id
        self._stub.PetAttack(request)

    def partner_attack(self, entity_type: EntityType, entity_id: int, skill_id: int) -> None:
        request = AttackRequest()
        request.entity_id = entity_id
        request.entity_type = entity_type
        request.skill_id = skill_id
        self._stub.PartnerAttack(request)