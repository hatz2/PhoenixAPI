from phoenixapi.api import PhoenixApi
from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api: PhoenixApi = create_api_from_name(os.environ.get("CHAR_NAME"))
    #api = PhoenixApi(56325)

    #api.login_manager.select_language(5)
    #api.login_manager.select_server(0)
    # api.login_manager.select_channel(6)
    # api.login_manager.select_character(3)

    # print(api.login_manager.get_character_slots())

    # print(api.login_manager.is_character_selection_visible())
    # print(api.login_manager.is_server_selection_visible())

    # print(api.login_manager.relog(1, 5, 3))

    print(api.login_manager.logout())