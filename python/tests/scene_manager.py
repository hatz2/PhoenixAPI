from phoenixapi.api import PhoenixApi
from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api: PhoenixApi = create_api_from_name(os.environ.get("CHAR_NAME"))

    # print(api.scene_manager.get_players())
    # print(api.scene_manager.get_monsters())
    # print(api.scene_manager.get_items())
    # print(api.scene_manager.get_npcs())

    # print(api.scene_manager.find_player(1237518))
    # print(api.scene_manager.find_monster(3108))
    # print(api.scene_manager.find_npc(3125))

    # print(api.scene_manager.get_all_bosses())

    print(api.scene_manager.get_map_grid())