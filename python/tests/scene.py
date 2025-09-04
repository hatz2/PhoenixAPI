from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api = create_api_from_name(os.environ.get("CHAR_NAME"))

    players = api.scene_manager.get_players()
    print("Players:")
    for player in players:
        print(f"\t- {player.name} ({player.movable_entity.base_entity.id}) [{player.family}]")

    monsters = api.scene_manager.get_monsters()
    print("Monsters:")
    for monster in monsters:
        print(f"\t-{monster.name} ({monster.movable_entity.base_entity.id})")

    items = api.scene_manager.get_items()
    print("Items")
    for item in items:
        print(f"\t-{item.name} ({item.base_entity.id})")

    npcs = api.scene_manager.get_npcs()
    print("Npcs:")
    for npc in npcs:
        print(f"\t-{npc.name} ({npc.monster.movable_entity.base_entity.id})")


    player = api.scene_manager.find_player(7646330)
    print(f"{player.name} - ({player.movable_entity.base_entity.id})")

    monster = api.scene_manager.find_monster(3058)
    print(f"{monster.name} - ({monster.movable_entity.base_entity.id})")

    item = api.scene_manager.find_item(9463508)
    print(f"{item.name} - ({item.base_entity.id})")

    npc = api.scene_manager.find_npc(2849293)
    print(f"{npc.monster.movable_entity.base_entity.id} - ({npc.name})")

    bosses = api.scene_manager.get_all_bosses()
    print("Bosses:")
    for boss in bosses:
        print(f"\t-{boss.name} ({boss.movable_entity.base_entity.id})")

    grid = api.scene_manager.get_map_grid()

    for row in grid.rows:
        s = str()
        for cell in row.cells:
            s += f"{cell} "

        print(s)
