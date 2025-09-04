from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api = create_api_from_name(os.environ.get("CHAR_NAME"))

    skills = api.skill_manager.get_skills()

    for skill in skills:
        print(f"vnum[{skill.vnum}] id[{skill.id}] name[{skill.name}]")

    print("----------------------------------------------------")

    skill = api.skill_manager.find_skill_from_id(0)
    print(f"vnum[{skill.vnum}] id[{skill.id}] name[{skill.name}]")

    skill = api.skill_manager.find_skill_from_vnum(262)
    print(f"vnum[{skill.vnum}] id[{skill.id}] name[{skill.name}]")
