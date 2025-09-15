from phoenixapi.api import PhoenixApi
from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api: PhoenixApi = create_api_from_name(os.environ.get("CHAR_NAME"))

    #api.bot_controller.start_farming_bot()
    #api.bot_controller.stop_farming_bot()
    #api.bot_controller.continue_farming_bot()
    # api.bot_controller.start_minigame_bot()
    api.bot_controller.stop_minigame_bot()