# PhoenixAPI

## General explanation
This API example has been made for C++ but you can use the API with any programming language that supports TCP sockets and JSON. This example basicaly provides a function to find all the running bot ports and a class that holds the socket that will be connected to a specific port and receive all the data from the bot.

**Important:** Messages are terminated with `'\1'` character or `0x01` byte. This examples already manages that so you should not worrie about it, however if you plan to use the API with other language you need to handle that correctly.

The messages received from the bot and sent to the bot are in JSON format and they match the following syntax:

```json
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
		packet_send,    // 0
		packet_recv,    // 1
		attack,         // 2
		player_skill,   // 3
		player_walk,    // 4
		pet_skill,      // 5
		partner_skill,  // 6
		pets_walk,      // 7
		pick_up,        // 8
		collect         // 9
	};
```

## Messages sent from the BOT to the CLIENT
The bot will only send you messages of type 0 and 1 which are send and recv packets. These 2 types of messages also have the field '"packet"' with the full packet.

Examples:
```json
// Send packet
{
    "type": 0,
    "packet": "u_s 0 3 2432"
}
```

```json
// Recv packet
{
    "type": 1,
    "packet": "mv 3 2389 70 11 5"
}
```

## Messages sent from the CLIENT to the BOT
You can send multiple messages to the bot to send or receive a packet and also do some actions like attacking, walking, picking up an item, etc. All this actions are performed by calling game functions in the main game thread to guarantee thread safety.

Examples:

```json
// Description: Send a packet to the game server
{
    "type": 0,
    "packet": "u_i 1 1234 2 15 0 0" // Use an item from the inventory
}
```

```json
// Description: Simulates a received packet from the game server
{
    "type": 1,
    "packet": "gold 1000000000 0" // Simulate client side getting 1kkk of gold
}
```

```json
// Description: Attack a monster by using the top ready skill that you've set in the bot for the player, pet and partner
{
    "type": 2,
    "monster_id": 2307, // ID of the monster you want to attack
}
```

```json
// Description: Attack a monster with the given skill
{
    "type": 3,
    "monster_id": 2307,
    "skill_id": 0, // ID of the skill you want to use
}
```

```json
// Description: Character walks to coordiantes (x, y)
{
    "type": 4,
    "x": 34,
    "y": 68,
}
```

```json
// Description: Attack a monster with the given pet skill
{
    "type": 5,
    "monster_id": 2307,
    "skill_id": 0 // ID of the pet skill you want to use
}
```

```json
// Description: Attack a monster with the given partner skill
{
    "type": 6,
    "monster_id": 2307,
    "skill_id": 1 // ID of the partner skill you want to use
}
```

```json
// Description: Pet and partner walks to coordinates (x, y)
{
    "type": 7,
    "x": 120,
    "y": 46
}
```

```json
// Description: Walk and pick up the given item
{
    "type": 8,
    "item_id": 1234 // ID of the item you want to pick up
}
```

```json
// Description: Walk and collect a npc (ice flowers and that kind of stuff)
{
    "type": 9,
    "npc_id": 4321 // ID of the npc you want to collect
}
```

## About the C++ API
To use this API you just need to add the following files into your project:

```
Api.h
Api.cpp
Port_finder.h
Port_finder.cpp
Safe_queue.h
Safe_queue.cpp
```

This example was made using Microsoft Visual Studio Community 2019 and C++14.

Since C++ doesn't support JSON natively you'll need to use a third party library to use it. In the case of this exapmle I've used [nlohmann json](https://github.com/nlohmann/json) and to handle the dependencies I've used [vcpkg](https://github.com/microsoft/vcpkg).

In the file [main.cpp](PhoenixAPI/main.cpp) you have an example of a packetlogger that will print to the standard output every send/recv packet that comes from the bot.