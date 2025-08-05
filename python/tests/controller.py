from phoenixapi.finder import create_api_from_name
import dotenv
import os
from time import sleep

def run():
    dotenv.load_dotenv()
    api = create_api_from_name(os.environ.get("CHAR_NAME"))

    print("Starting farming bot...")
    api.controller.start_farming_bot()
    sleep(2)
    print("Stopping farming bot...")
    api.controller.stop_farming_bot()
    sleep(2)
    print("Continuing farming bot...")
    api.controller.continue_farming_bot()
    sleep(2)
    print("Starting minigame bot...")
    api.controller.start_minigame_bot()
    sleep(2)
    print("Stopping minigame bot...")
    api.controller.stop_minigame_bot()
    sleep(2)
    print("Loading profile...")
    api.controller.load_settings("C:/Downloads/test.ini")
