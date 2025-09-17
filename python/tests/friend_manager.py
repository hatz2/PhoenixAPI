from phoenixapi.api import PhoenixApi
from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api: PhoenixApi = create_api_from_name(os.environ.get("CHAR_NAME"))

    friend = api.friend_manager.get_friend_list()[0]

    print(friend)

    api.friend_manager.join_miniland(friend["id"])