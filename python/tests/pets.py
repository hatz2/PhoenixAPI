from phoenixapi.finder import create_api_from_name
from phoenixapi.protos.game.petmanager_pb2 import PetObjManager, PetState
from phoenixapi.protos.game.entities_pb2 import *
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api = create_api_from_name(os.environ.get("CHAR_NAME"))

    pets = api.pet_manager.get_pets()

    print("* Pets:")
    for pet in pets:
        print(f"\t- {pet.npc.name}")

    pet: PetObjManager = api.pet_manager.get_current_pet()
    api.pet_manager.set_pet_state(pet.npc.monster.movable_entity.base_entity.id, PetState.PET_STATE_D)

    partner = api.pet_manager.get_current_partner()
    api.pet_manager.set_pet_state(partner.npc.monster.movable_entity.base_entity.id, PetState.PET_STATE_D)

    # api.pet_manager.walk(8, 10)

    target = api.scene_manager.find_monster(2661)

    # if target.movable_entity.base_entity.id > 0:
    #     api.pet_manager.auto_attack(target.movable_entity.base_entity.type, target.movable_entity.base_entity.id)

    target_id = target.movable_entity.base_entity.id
    target_type = target.movable_entity.base_entity.type
    skill_id = 2

    if target_id > 0:
        api.pet_manager.partner_attack(target_type, 0, skill_id)


    