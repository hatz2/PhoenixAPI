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
from phoenixapi import api, finder
from phoenixapi.protos.game.playermanager_pb2 import PlayerObjManager

CHAR_NAME = "Insert your character name here"

if __name__ == "__main__":
    client: api.Phoenix = finder.create_api_from_name(CHAR_NAME)
    player_obj_manager: PlayerObjManager = client.player_manager.get_player_obj_manager()

    print(f"Name:\t\t{player_obj_manager.player.name}")
    print(f"ID:\t\t{player_obj_manager.id}")
    print(f"Family:\t\t{player_obj_manager.player.family}")
    print(f"Position:\t({player_obj_manager.position.x}, {player_obj_manager.position.y})")
```
