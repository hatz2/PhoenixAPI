# Phoenix API

This is the Python client for the Phoenix API.

## Installation

You can install the package using pip:

```
pip install phoenix-bot-api
```

## Usage

Here is a simple example of how to use the Phoenix API client:

```python
from phoenixapi.finder import create_api_from_name
from phoenixapi.api import PhoenixApi
from phoenixapi.clients.player_manager import PlayerObjManager

def run():
    CHAR_NAME = "Insert your character name here"
    client: PhoenixApi = create_api_from_name(CHAR_NAME)

    player_obj_manager: PlayerObjManager = client.player_obj_manager.get_player_obj_manager()

    name = player_obj_manager["player"]["name"]
    player_id = player_obj_manager["id"]
    family = player_obj_manager["player"]["family"]
    x = player_obj_manager['position']['x']
    y = player_obj_manager['position']['y']

    print(f"Name:\t\t{name}")
    print(f"ID:\t\t{player_id}")
    print(f"Family:\t\t{family}")
    print(f"Position:\t({x}, {y})")
```
