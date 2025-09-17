from phoenixapi.api import PhoenixApi
from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api: PhoenixApi = create_api_from_name(os.environ.get("CHAR_NAME"))

    # print(api.inventory_manager.get_equip_tab())
    # print(api.inventory_manager.get_main_tab())
    # print(api.inventory_manager.get_etc_tab())

    # print(api.inventory_manager.find_item(2083))
    # print(api.inventory_manager.get_gold())
    # print(api.inventory_manager.use_item(2071))