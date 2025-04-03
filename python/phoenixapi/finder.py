import json
from win32gui import EnumWindows, GetWindowText
from re import search
from ctypes.wintypes import HWND, LPARAM
from time import sleep
from phoenixapi import phoenix

_ports: list[int] = []

def find_all_api_ports() -> list[int]:
    """Find all ports of the current bot windows."""
    _ports.clear()
    EnumWindows(_enum_windows_callback, 0)
    return _ports.copy()

def create_apis_from_names(character_names: list[str]) -> list[tuple[str, phoenix.Api]]:
    """
    Create API instances from a list of character names.

    Returns:
        list[tuple[str, phoenix.Api]]: A list of tuples containing character names and their corresponding API instances.
    
    Raises:
        RuntimeError: If no bots are running or not all bots with the given character names are found.
    """

    ports = find_all_api_ports()
    apis = []

    if len(ports) == 0:
        raise RuntimeError("No bot windows found.")
    
    for port in ports:
        api = phoenix.Api(port)

        # Ask the bot to give us the player info
        api.query_player_information()

        # Wait for the bot to respond
        while api.working():
            if api.empty():
                sleep(0.01)
                continue

            msg = api.get_message()
            json_msg = json.loads(msg)

            if json_msg["type"] == phoenix.Type.query_player_info.value:
                if json_msg["player_info"]["name"] in character_names:
                    character_names.remove(json_msg["player_info"]["name"])
                    apis.append((json_msg["player_info"]["name"], api))
                    break
                else:
                    api.close()

    if (len(character_names) != 0):
        raise RuntimeError("Could not find all bots with the given character names.")
    
    return apis

def create_api_from_name(character_name: str) -> phoenix.Api:
    """
    Create an instance of the API class from the character's name.

    Returns:
        phoenix.Api: An instance of the API class.
    
    Raises:
        RuntimeError: If no bot with that name is found or no bots are running.
    """

    ports = find_all_api_ports()

    if len(ports) == 0:
        raise RuntimeError("No bot windows found.")

    for port in ports:
        api = phoenix.Api(port)

        # Ask the bot to give us the player info
        api.query_player_information()

        # Wait for the bot to respond
        while api.working():
            if api.empty():
                sleep(0.01)
                continue

            msg = api.get_message()
            json_msg = json.loads(msg)

            if json_msg["type"] == phoenix.Type.query_player_info.value:
                if json_msg["player_info"]["name"] == character_name:
                    return api
                else:
                    api.close()

    raise RuntimeError(f"Could not find bot with character name: {character_name}")

def _enum_windows_callback(hwnd: HWND, lparam: LPARAM) -> bool:
    """Callback function to enumerate windows and check if it is a bot window."""
    window_title = GetWindowText(hwnd)

    if "- Phoenix Bot" in window_title:
        match: str = search(r"Bot:(\d+)", window_title)

        if match:
            port = (int)(match.group(1))
            _ports.append(port)

    return True