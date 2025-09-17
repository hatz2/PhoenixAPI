from phoenixapi.api import PhoenixApi
from phoenixapi.finder import create_api_from_name
from phoenixapi.entities import EntityType
from phoenixapi.clients.pet_manager import PetState
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api: PhoenixApi = create_api_from_name(os.environ.get("CHAR_NAME"))

    #print(api.pet_manager.get_pets())

    #api.pet_manager.auto_attack(EntityType.MONSTER, 3070)

    api.pet_manager.set_pet_state(api.pet_manager.get_current_pet()["pet"]["id"], PetState.S)