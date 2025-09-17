from phoenixapi.api import PhoenixApi
from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api: PhoenixApi = create_api_from_name(os.environ.get("CHAR_NAME"))

    #print(api.skill_manager.get_skills())

    #print(api.skill_manager.find_skill_from_id(0))

    #print(api.skill_manager.find_skill_from_vnum(276))

    print(api.skill_manager.find_skill_from_id(11111110))