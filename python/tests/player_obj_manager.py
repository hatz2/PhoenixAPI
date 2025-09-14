from phoenixapi.clients import PlayerObjManager, PlayerObjManagerClient
from phoenixapi.api import PhoenixApi
from phoenixapi.entities import EntityType
from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api: PhoenixApi = create_api_from_name(os.environ.get("CHAR_NAME"))

    player_obj_manager = api.player_obj_manager.get_player_obj_manager()
    print(player_obj_manager)

    #api.player_obj_manager.walk(9, 92)

    #api.player_obj_manager.attack(EntityType.MONSTER, 2685, 0)

    #api.player_obj_manager.target(EntityType.MONSTER, 2685)

    #api.player_obj_manager.pickup(4608121)

    api.player_obj_manager.collect(3121)