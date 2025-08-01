from phoenixapi.finder import create_api_from_name
from phoenixapi.protos.game.inventorymanager_pb2 import InventoryTabType
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api = create_api_from_name(os.environ.get("CHAR_NAME"))

    gold = api.inventory.get_gold()
    print(f"Gold: {gold}")

    items = api.inventory.get_equip_tab()
    print("# EQUIP TAB")
    for item in items:
        print(f"\t- {item.name} [{item.index}] [{item.vnum}]")

    items = api.inventory.get_main_tab()
    print("# MAIN TAB")
    for item in items:
        print(f"\t- {item.name} [{item.index}] [{item.vnum}]")

    print("# ETC TAB")
    items = api.inventory.get_etc_tab()
    for item in items:
        print(f"\t- {item.name} [{item.index}] [{item.vnum}]")

    item = api.inventory.find_item(2089)
    print(f"Found item: {item.name} [{item.index}] [{item.vnum}]")

    item = api.inventory.get_inventory_slot(InventoryTabType.INVENTORY_TAB_TYPE_EQUIP, 13)
    print(f"Found item: {item.name} [{item.index}] [{item.vnum}]")

    response = api.inventory.use_item(2071)
    print(response)
    