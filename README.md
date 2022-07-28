# PhoenixAPI

## General explanation

This API example has been made for C++ but you can use the API with any programming language that supports TCP sockets and JSON. This example basicaly provides a function to find all the running bot ports and a class that holds the socket that will be connected to a specific port and receive all the data from the bot.

**Important:** Messages are terminated with `'\1'` character or `0x01` byte. This examples already manages that so you should not worrie about it, however if you plan to use the API with other language you need to handle that correctly.

The messages received from the bot and sent to the bot are in JSON format and they match the following syntax:

```js
{
    "type": 0, // The type of the message

    // [...]
    // Further parameters of the message, depends on the type
}
```

The type is just a numerical value and it must be a valid type. In the C++ example it is represented by an enum for easier access:

```cpp
enum class Type
{
    packet_send,        // 0
    packet_recv,        // 1
    attack,             // 2
    player_skill,       // 3
    player_walk,        // 4
    pet_skill,          // 5
    partner_skill,      // 6
    pets_walk,          // 7
    pick_up,            // 8
    collect,            // 9
    start_bot,          // 10
    stop_bot,           // 11
    continue_bot,       // 12
    load_settings,      // 13
    start_minigame_bot, // 14
    stop_minigame_bot,  // 15
    query_player_info,  // 16
    query_inventory,    // 17
    query_skills_info   // 18

}
```

## Messages sent from the BOT to the CLIENT

The bot will constantly send you messages of type 0 and 1 which are send and recv packets. These 2 types of messages also have the field `packet` with the full packet.

Examples:

* Send packet
  
  ```json
  {
    "type": 0,
    "packet": "u_s 0 3 2432"
  }
  ```

___

* Recv packet
  
  ```json
  {
    "type": 1,
    "packet": "mv 3 2389 70 11 5"
  }
  ```

You can also query the player infomation, the inventory and the skills information using the messages with type 16, 17 and 18.

Examples:

* Player information
 
  ```json
  {
    "type": 16,
    "player_info": {
        "name": "Hatz",
        "id": 123123,
        "x": 5,
        "y": 8,
        "level": 99,
        "champion_level": 80,
        "hp_percent": 100,
        "mp_percent": 100,
        "map_id": 1,
        "is_resting": false
    }
  }
  ```

* Inventory
 
  ```json
  {
    "type": 17,
    "inventory": {
        "equip": [
            {
                "cuantity": 1,
                "name": "Beast King's Crossbow",
                "position": 0,
                "vnum": 4465
            },
            {
                "cuantity": 1,
                "name": "Great Leader's Crossbow",
                "position": 1,
                "vnum": 4007
            }
        ],
        "main": [
            {
                "cuantity": 70,
                "name": "Gillion Stone",
                "position": 0,
                "vnum": 1013
            },
            {
                "cuantity": 311,
                "name": "Seed of Power",
                "position": 1,
                "vnum": 1012
            }
        ],
        "etc": [
            {
                "cuantity": 999,
                "name": "Pearl of Darkness",
                "position": 0,
                "vnum": 2094
            },
            {
                "cuantity": 112,
                "name": "Small Bean",
                "position": 5,
                "vnum": 2016
            }
        ]
    }
  }
  ```

* Skills information
  
  ```json
  {
    "type": 18,
    "skills": [
        {
            "name": "Shuriken Attack",
            "vnum": 880,
            "id": 0,
            "range": 3,
            "area": 0,
            "mana_cost": 0,
            "is_ready": true
        },
        {
            "name": "Summon Kamapakun",
            "vnum": 886,
            "id": 6,
            "area": 3,
            "mana_cost": 0,
            "is_ready": true
        }
    ]
  }
  ```

## Messages sent from the CLIENT to the BOT

You can send multiple messages to the bot to send or receive a packet and also do some actions like attacking, walking, picking up an item, etc. All this actions are performed by calling game functions in the main game thread to guarantee thread safety.

Examples:

* `Description`: Send a packet to the game server.
* `packet`: The packet to send to the game server, in this case it uses an item from the inventory
  
  ```json
  {
    "type": 0,
    "packet": "u_i 1 1234 2 15 0 0"
  }
  ```

___

* `Description`: Simulates a received packet from the game server.
* `packet`: The packet to get received, in this case it simulates client side getting 1kkk of gold.
  
  ```json
  {
    "type": 1,
    "packet": "gold 1000000000 0"
  }
  ```

___

* `Description`: Attack a monster by using the top ready skill that you've set in the bot for the player, pet and partner.
* `monster_id`: ID of the monster you want to attack.
  
  ```json
  {
    "type": 2,
    "monster_id": 2307
  }
  ```

___

* `Description`: Attack a monster with the given skill.
* `monster_id`: ID of the monster you want to attack
* `skill_id`: ID of the skill you want to use.
  
  ```json
  {
    "type": 3,
    "monster_id": 2307,
    "skill_id": 0
  }
  ```

___

* `Description`: Character walks to coordiantes (x, y).
  
  ```json
  {
    "type": 4,
    "x": 34,
    "y": 68,
  }
  ```

___

* `Description`: Attack a monster with the given pet skill.
* `monster_id`: ID of the monster you want to attack
* `skill_id`: ID of the pet skill you want to use.
  
  ```json
  {
    "type": 5,
    "monster_id": 2307,
    "skill_id": 0
  }
  ```

___

* `Description`: Attack a monster with the given partner skill.
* `monster_id`: ID of the monster you want to attack
* `skill_id`: ID of the partner skill you want to use.
  
  ```json
  {
    "type": 6,
    "monster_id": 2307,
    "skill_id": 1
  }
  ```

___

* `Description`: Pet and partner walks to coordinates (x, y).
  
  ```json
  {
    "type": 7,
    "x": 120,
    "y": 46
  }
  ```

___

* `Description`: Walk and pick up the given item.
* `item_id`: ID of the item you want to pick up.
  
  ```json
  {
    "type": 8,
    "item_id": 1234
  }
  ```

____

* `Description`: Walk and collect a npc (ice flowers and that kind of stuff).
* `npc_id`: ID of the npc you want to collect.
  
  ```json
  {
    "type": 9,
    "npc_id": 4321
  }
  ```

___

* `Description`: Start the farming bot
  
  ```json
  {
    "type": 10
  }
  ```

___

* `Description`: Stop the farming bot
  
  ```json
  {
    "type": 11
  }
  ```

___

* `Description`: Continue the farming bot
  
  ```json
  {
    "type": 12
  }
  ```

___

* `Description`: Load existing bot settings/profile

* `path`: Full path of the .ini file
  
  ```json
  {
    "type": 13,
    "path": "C:/Program Files (x86)/Nostale/mysettings.ini"
  }
  ```

___

* `Description`: Starts the minigame bot

  ```json
  {
    "type": 14
  }
  ```

___

* `Description`: Stops the minigame bot

  ```json
  {
    "type": 15
  }
  ```

___

* `Description`: Query information from the player
  
  ```json
  {
    "type": 16
  }
  ```

___

* `Description`: Query the inventory information from the player
  
  ```json
  {
    "type": 17
  }
  ```

___

* `Description`: Query the skill information from the player
  
  ```json
  {
    "type": 18
  }
  ```

___
  
## About the C++ API

To use this API you just need to add the following files into your project and `#include "Api.h"` where you want to use it:

* `Api.h`

* `Api.cpp`

* `Port_finder.h`

* `Port_finder.cpp`

* `Safe_queue.h`

* `Safe_queue.cpp`

This example was made using Microsoft Visual Studio Community 2019 and C++14.

Since C++ doesn't support JSON natively you'll need to use a third party library to use it. In this example I've used [nlohmann json](https://github.com/nlohmann/json). To handle the dependencies I've used [vcpkg](https://github.com/microsoft/vcpkg).

In the file [main.cpp](PhoenixAPI/main.cpp) you have an example of a packetlogger that will connect to the first port found and print to the standard output every send/recv packet that comes from the bot.
