# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [phoenixapi/protos/bot/controller.proto](#phoenixapi_protos_bot_controller-proto)
    - [LoadSettingsRequest](#phoenix-bot-LoadSettingsRequest)
  
    - [Controller](#phoenix-bot-Controller)
  
- [phoenixapi/protos/game/entities.proto](#phoenixapi_protos_game_entities-proto)
    - [BaseEntity](#phoenix-game-entities-BaseEntity)
    - [Item](#phoenix-game-entities-Item)
    - [Monster](#phoenix-game-entities-Monster)
    - [MovableEntity](#phoenix-game-entities-MovableEntity)
    - [Npc](#phoenix-game-entities-Npc)
    - [Player](#phoenix-game-entities-Player)
  
    - [Direction](#phoenix-game-entities-Direction)
    - [EntityType](#phoenix-game-entities-EntityType)
  
- [phoenixapi/protos/game/inventorymanager.proto](#phoenixapi_protos_game_inventorymanager-proto)
    - [FindItemRequest](#phoenix-game-FindItemRequest)
    - [GoldResponse](#phoenix-game-GoldResponse)
    - [InvSlot](#phoenix-game-InvSlot)
    - [InvSlotList](#phoenix-game-InvSlotList)
    - [InventorySlotRequest](#phoenix-game-InventorySlotRequest)
    - [UseItemOnTargetRequest](#phoenix-game-UseItemOnTargetRequest)
    - [UseItemRequest](#phoenix-game-UseItemRequest)
    - [UseItemResponse](#phoenix-game-UseItemResponse)
  
    - [InventoryTabType](#phoenix-game-InventoryTabType)
    - [UseItemResponseType](#phoenix-game-UseItemResponseType)
  
    - [InventoryManager](#phoenix-game-InventoryManager)
  
- [phoenixapi/protos/game/packetmanager.proto](#phoenixapi_protos_game_packetmanager-proto)
    - [Identifier](#phoenix-game-Identifier)
    - [Packet](#phoenix-game-Packet)
  
    - [PacketManager](#phoenix-game-PacketManager)
  
- [phoenixapi/protos/game/petmanager.proto](#phoenixapi_protos_game_petmanager-proto)
    - [AutoAttackRequest](#phoenix-game-AutoAttackRequest)
    - [PetObjManager](#phoenix-game-PetObjManager)
    - [PetObjManagerList](#phoenix-game-PetObjManagerList)
    - [PetStateRequest](#phoenix-game-PetStateRequest)
  
    - [PetState](#phoenix-game-PetState)
  
    - [PetManager](#phoenix-game-PetManager)
  
- [phoenixapi/protos/game/playermanager.proto](#phoenixapi_protos_game_playermanager-proto)
    - [AttackRequest](#phoenix-game-AttackRequest)
    - [CollectRequest](#phoenix-game-CollectRequest)
    - [PickUpRequest](#phoenix-game-PickUpRequest)
    - [PlayerObjManager](#phoenix-game-PlayerObjManager)
    - [TargetRequest](#phoenix-game-TargetRequest)
  
    - [PlayerManager](#phoenix-game-PlayerManager)
  
- [phoenixapi/protos/game/scenemanager.proto](#phoenixapi_protos_game_scenemanager-proto)
    - [FindRequest](#phoenix-game-FindRequest)
    - [ItemList](#phoenix-game-ItemList)
    - [MapGrid](#phoenix-game-MapGrid)
    - [MonsterList](#phoenix-game-MonsterList)
    - [NpcList](#phoenix-game-NpcList)
    - [PlayerList](#phoenix-game-PlayerList)
    - [Row](#phoenix-game-Row)
  
    - [CellType](#phoenix-game-CellType)
  
    - [SceneManager](#phoenix-game-SceneManager)
  
- [phoenixapi/protos/game/skillmanager.proto](#phoenixapi_protos_game_skillmanager-proto)
    - [FindSkillFromIdRequest](#phoenix-game-FindSkillFromIdRequest)
    - [FindSkillFromVnumRequest](#phoenix-game-FindSkillFromVnumRequest)
    - [Skill](#phoenix-game-Skill)
    - [SkillList](#phoenix-game-SkillList)
  
    - [SkillType](#phoenix-game-SkillType)
    - [TargetType](#phoenix-game-TargetType)
  
    - [SkillManager](#phoenix-game-SkillManager)
  
- [phoenixapi/protos/position.proto](#phoenixapi_protos_position-proto)
    - [Position](#phoenix-Position)
  
- [Scalar Value Types](#scalar-value-types)



<a name="phoenixapi_protos_bot_controller-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## phoenixapi/protos/bot/controller.proto
Service and messages to control and interact with phoenix bot.


<a name="phoenix-bot-LoadSettingsRequest"></a>

### LoadSettingsRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ini_file_path | [string](#string) |  |  |





 

 

 


<a name="phoenix-bot-Controller"></a>

### Controller
Service that allows you to interact with the bot.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| StartFarmingBot | [.google.protobuf.Empty](#google-protobuf-Empty) | [.google.protobuf.Empty](#google-protobuf-Empty) |  |
| StopFarmingBot | [.google.protobuf.Empty](#google-protobuf-Empty) | [.google.protobuf.Empty](#google-protobuf-Empty) |  |
| ContinueFarmingBot | [.google.protobuf.Empty](#google-protobuf-Empty) | [.google.protobuf.Empty](#google-protobuf-Empty) |  |
| StartMinigameBot | [.google.protobuf.Empty](#google-protobuf-Empty) | [.google.protobuf.Empty](#google-protobuf-Empty) |  |
| StopMinigameBot | [.google.protobuf.Empty](#google-protobuf-Empty) | [.google.protobuf.Empty](#google-protobuf-Empty) |  |
| LoadSettings | [LoadSettingsRequest](#phoenix-bot-LoadSettingsRequest) | [.google.protobuf.Empty](#google-protobuf-Empty) |  |

 



<a name="phoenixapi_protos_game_entities-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## phoenixapi/protos/game/entities.proto
Entities related messages and enums


<a name="phoenix-game-entities-BaseEntity"></a>

### BaseEntity
The base entity class for every entity in the game.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [EntityType](#phoenix-game-entities-EntityType) |  | The type of entity. |
| id | [sint32](#sint32) |  | The unique ID of this entity. |
| position | [phoenix.Position](#phoenix-Position) |  | The 2D position of the entity. |






<a name="phoenix-game-entities-Item"></a>

### Item
Contains item related data. It inherits from BaseEntity as items in the ground doesn&#39;t move.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| base_entity | [BaseEntity](#phoenix-game-entities-BaseEntity) |  | Parent. |
| vnum | [int32](#int32) |  | Identifier for the type of item. |
| quantity | [int32](#int32) |  | Number of items stacked together. |
| owner_id | [int32](#int32) |  | ID of the object that owns this item. |
| is_quest_item | [bool](#bool) |  | Controls wether this item is for a quest or not. |
| name | [string](#string) |  | Name of the item. |






<a name="phoenix-game-entities-Monster"></a>

### Monster
Contains monster related data. It inherits from MovableEntity.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| movable_entity | [MovableEntity](#phoenix-game-entities-MovableEntity) |  | Parent. |
| vnum | [int32](#int32) |  | Identifier for the type of monster. |
| name | [string](#string) |  | Name of the monster. |
| race | [int32](#int32) |  | Number of the race rank. It is represented as an int32 but this should be an enum. |
| skin_id | [int32](#int32) |  | Identifier of the skin texture of the monster. |
| is_boss | [bool](#bool) |  | Controls wether this monster is a boss or not (green dot in the minimap). |






<a name="phoenix-game-entities-MovableEntity"></a>

### MovableEntity
Contains the data of every movable entity in the game. It is a child of BaseEntity. The parent is the field base_entity as protoc doesn&#39;t support inheritance.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| base_entity | [BaseEntity](#phoenix-game-entities-BaseEntity) |  | Parent. |
| direction | [Direction](#phoenix-game-entities-Direction) |  | Direction where the entity is facing. |
| animation_status | [int32](#int32) |  | The current animation state. It is represented as an int32 but this should be an enum. |
| speed | [int32](#int32) |  | Walking speed. |
| is_in_combat | [bool](#bool) |  | Controls wether the entity is in combat or not. |
| health_percent | [int32](#int32) |  | Health percent from 0 to 100. |
| mana_percent | [int32](#int32) |  | Mana percent from 0 to 100. |
| level | [int32](#int32) |  | Normal level. |
| champion_level | [int32](#int32) |  | Champion level. |
| is_partner | [bool](#bool) |  | Controls wether the entity is a partner or not. |
| owner_id | [sint32](#sint32) |  | The ID of the entity that owns this object. Mainly used in dropped items. |
| current_map_id | [sint32](#sint32) |  | The current map ID. |






<a name="phoenix-game-entities-Npc"></a>

### Npc
Contains npc related data. It inherits from Monster. Apart from common npcs as you are used to see in the game, other objects like ice flowers, lettuce and time-spaces are also from the Npc type.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| monster | [Monster](#phoenix-game-entities-Monster) |  | Parent. |
| name | [string](#string) |  | Name of the NPC. |






<a name="phoenix-game-entities-Player"></a>

### Player
Contains player related data. It inherits from MovableEntity.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| movable_entity | [MovableEntity](#phoenix-game-entities-MovableEntity) |  | Parent. |
| sp | [sint32](#sint32) |  | Number of the SP that the player is wearing. It is represented as an int32 but this should be an enum. |
| name | [string](#string) |  | Name of the player. |
| title | [string](#string) |  | Title the player is using. |
| family | [string](#string) |  | The family the player belongs to. |
| is_gm | [bool](#bool) |  | Controls wether this player is a GM with purple nickname or not |
| reputation | [int32](#int32) |  | Number of the reputation rank. It is represented as an int32 but this should be an enum. |





 


<a name="phoenix-game-entities-Direction"></a>

### Direction
Direction where an entity is facing to.

| Name | Number | Description |
| ---- | ------ | ----------- |
| DIRECTION_UP | 0 |  |
| DIRECTION_RIGHT | 1 |  |
| DIRECTION_DOWN | 2 |  |
| DIRECTION_LEFT | 3 |  |
| DIRECTION_UP_LEFT | 4 |  |
| DIRECTION_UP_RIGHT | 5 |  |
| DIRECTION_DOWN_RIGHT | 6 |  |
| DIRECTION_DOWN_LEFT | 7 |  |



<a name="phoenix-game-entities-EntityType"></a>

### EntityType
All entity types in the game.

| Name | Number | Description |
| ---- | ------ | ----------- |
| ENTITY_TYPE_UNSPECIFIED | 0 |  |
| ENTITY_TYPE_PLAYER | 1 |  |
| ENTITY_TYPE_MONSTER | 2 |  |
| ENTITY_TYPE_NPC | 3 |  |
| ENTITY_TYPE_ITEM | 4 |  |


 

 

 



<a name="phoenixapi_protos_game_inventorymanager-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## phoenixapi/protos/game/inventorymanager.proto
Inventory related service and messages.


<a name="phoenix-game-FindItemRequest"></a>

### FindItemRequest
Message request to find an item in the inventory.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vnum | [int32](#int32) |  |  |






<a name="phoenix-game-GoldResponse"></a>

### GoldResponse
Response with the gold in the inventory.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| gold | [int32](#int32) |  |  |






<a name="phoenix-game-InvSlot"></a>

### InvSlot
Contains information about an inventory slot.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| inv_tab | [InventoryTabType](#phoenix-game-InventoryTabType) |  | The inventory tab. |
| index | [int32](#int32) |  | The index of the slot within the tab (starts at 0). |
| vnum | [int32](#int32) |  | The unique ID that identifies the type of item. |
| quantity | [int32](#int32) |  | The number of items in the slot. |
| name | [string](#string) |  | The name of the item in the slot. |






<a name="phoenix-game-InvSlotList"></a>

### InvSlotList
A list of inventory slots.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| inv_slots | [InvSlot](#phoenix-game-InvSlot) | repeated | List of inventory slots. |






<a name="phoenix-game-InventorySlotRequest"></a>

### InventorySlotRequest
Message to request a specific inventory slot.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| inv_tab_type | [InventoryTabType](#phoenix-game-InventoryTabType) |  | The inventory tab. |
| index | [int32](#int32) |  | The index withing the tab. |






<a name="phoenix-game-UseItemOnTargetRequest"></a>

### UseItemOnTargetRequest
Message request for using an item in a specific target.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vnum | [int32](#int32) |  | The unique ID that identifies the type of item. |
| target_id | [int32](#int32) |  | The ID of the target. |
| target_type | [entities.EntityType](#phoenix-game-entities-EntityType) |  | The entity type of the target. |






<a name="phoenix-game-UseItemRequest"></a>

### UseItemRequest
Message request for using an item.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vnum | [int32](#int32) |  | The unique ID that identifies the type of item. |






<a name="phoenix-game-UseItemResponse"></a>

### UseItemResponse
Response message received when using an item as confirmation or error code.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response | [UseItemResponseType](#phoenix-game-UseItemResponseType) |  |  |





 


<a name="phoenix-game-InventoryTabType"></a>

### InventoryTabType
Represents the inventory tabs.

| Name | Number | Description |
| ---- | ------ | ----------- |
| INVENTORY_TAB_TYPE_EQUIP | 0 |  |
| INVENTORY_TAB_TYPE_MAIN | 1 |  |
| INVENTORY_TAB_TYPE_ETC | 2 |  |



<a name="phoenix-game-UseItemResponseType"></a>

### UseItemResponseType
Message received when using an item.

| Name | Number | Description |
| ---- | ------ | ----------- |
| USE_ITEM_RESPONSE_TYPE_UNSPECIFIED | 0 | Unknown error. |
| USE_ITEM_RESPONSE_TYPE_USED | 1 | Used correctly. |
| USE_ITEM_RESPONSE_TYPE_NOT_FOUND | 2 | Not enough quantity to use the item. |
| USE_ITEM_RESPONSE_TYPE_TARGET_NOT_FOUND | 3 | Target entity not found. |
| USE_ITEM_RESPONSE_TYPE_WRONG_PARAMETERS | 4 | Wrong parameters. |


 

 


<a name="phoenix-game-InventoryManager"></a>

### InventoryManager
Service for interacting with the inventory.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetGold | [.google.protobuf.Empty](#google-protobuf-Empty) | [GoldResponse](#phoenix-game-GoldResponse) | Returns the gold that you have in your inventory. |
| GetEquipTab | [.google.protobuf.Empty](#google-protobuf-Empty) | [InvSlotList](#phoenix-game-InvSlotList) | Returns all the slots in the inventory EQUIP tab. |
| GetMainTab | [.google.protobuf.Empty](#google-protobuf-Empty) | [InvSlotList](#phoenix-game-InvSlotList) | Returns all the slots in the inventory MAIN tab. |
| GetEtcTab | [.google.protobuf.Empty](#google-protobuf-Empty) | [InvSlotList](#phoenix-game-InvSlotList) | Returns all the slots in the inventory ETC tab. |
| GetInventorySlot | [InventorySlotRequest](#phoenix-game-InventorySlotRequest) | [InvSlot](#phoenix-game-InvSlot) | Returns a specific slot from the specified inventory tab and index. |
| FindItem | [FindItemRequest](#phoenix-game-FindItemRequest) | [InvSlot](#phoenix-game-InvSlot) | Searchs for the specified item and return its slot if the item was found. |
| UseItem | [UseItemRequest](#phoenix-game-UseItemRequest) | [UseItemResponse](#phoenix-game-UseItemResponse) | Use the specified item and returns a status. |
| UseItemOnTarget | [UseItemOnTargetRequest](#phoenix-game-UseItemOnTargetRequest) | [UseItemResponse](#phoenix-game-UseItemResponse) | Use the specified item on the specified target and returs a status. |

 



<a name="phoenixapi_protos_game_packetmanager-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## phoenixapi/protos/game/packetmanager.proto
Service and messages to interact with the packets that the game sends and receives from the server.


<a name="phoenix-game-Identifier"></a>

### Identifier
Identifier request for some of the packet manager service methods.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [string](#string) |  | This identifier can be any random string, I recommend to use some form of uuid. |






<a name="phoenix-game-Packet"></a>

### Packet
Message that represents a packet.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| data | [string](#string) |  | The packet string itself. |





 

 

 


<a name="phoenix-game-PacketManager"></a>

### PacketManager
Service that allows you to read and send packets.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| Subscribe | [Identifier](#phoenix-game-Identifier) | [.google.protobuf.Empty](#google-protobuf-Empty) | This method notifies the bot that you want to start reading packets so that it can allocate resources for you. An unique identifier is needed for the request so that the bot knows which allocated resources are yours. |
| Unsubscribe | [Identifier](#phoenix-game-Identifier) | [.google.protobuf.Empty](#google-protobuf-Empty) | This method let the bot know that you don&#39;t want to read packets anymore so that it can free the previously allocated resources. |
| GetPendingSendPackets | [Identifier](#phoenix-game-Identifier) | [Packet](#phoenix-game-Packet) stream | Returns a stream of the SEND packets that haven&#39;t been processed yet by your application. |
| GetPendingRecvPackets | [Identifier](#phoenix-game-Identifier) | [Packet](#phoenix-game-Packet) stream | Returns a stream of the RECV packets that haven&#39;t been processed yet by your application. |
| Send | [Packet](#phoenix-game-Packet) | [.google.protobuf.Empty](#google-protobuf-Empty) | Sends a packet to the game server. |
| Recv | [Packet](#phoenix-game-Packet) | [.google.protobuf.Empty](#google-protobuf-Empty) | Fake receive a packet in the game client. |

 



<a name="phoenixapi_protos_game_petmanager-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## phoenixapi/protos/game/petmanager.proto
Service and messages to interact with your pets.


<a name="phoenix-game-AutoAttackRequest"></a>

### AutoAttackRequest
Message request to autoattack a target.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| entity_type | [entities.EntityType](#phoenix-game-entities-EntityType) |  | The type of entity. |
| entity_id | [sint32](#sint32) |  | The ID of the entity. |






<a name="phoenix-game-PetObjManager"></a>

### PetObjManager
Message that contains pet related information.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [phoenix.Position](#phoenix-Position) |  | The 2D position of the pet. |
| dest_position | [phoenix.Position](#phoenix-Position) |  | The 2D destiny position where the pet is walking to. |
| state | [PetState](#phoenix-game-PetState) |  | The current state of the pet. |
| npc | [entities.Npc](#phoenix-game-entities-Npc) |  | The NPC object of this pet. |






<a name="phoenix-game-PetObjManagerList"></a>

### PetObjManagerList
Message that contains a list of pets.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pets | [PetObjManager](#phoenix-game-PetObjManager) | repeated | The list of pets. |






<a name="phoenix-game-PetStateRequest"></a>

### PetStateRequest
Message request to change the state of a pet.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| pet_id | [sint32](#sint32) |  | The ID of your pet. |
| new_state | [PetState](#phoenix-game-PetState) |  | The state you want the pet to be. |





 


<a name="phoenix-game-PetState"></a>

### PetState
The state of your pet.

| Name | Number | Description |
| ---- | ------ | ----------- |
| PET_STATE_D | 0 |  |
| PET_STATE_S | 5 | In this state your pet shouldn&#39;t attack any move neither move. |
| PET_STATE_F | 7 |  |
| PET_STATE_WALK_AFTER_F | 8 |  |
| PET_STATE_A | 12 |  |
| PET_STATE_AFTER_A_CLICK | 15 |  |
| PET_STATE_S_AFTER_A_F | 17 | I believe in this state if a monster attack your pet it will attack back even if he is in S mode. |


 

 


<a name="phoenix-game-PetManager"></a>

### PetManager
Services that allows you to read your pet information aswell as performing actions with them.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetPets | [.google.protobuf.Empty](#google-protobuf-Empty) | [PetObjManagerList](#phoenix-game-PetObjManagerList) | Returns a list with your current pets and partners. While in the miniland it will returns a list with all your pets. |
| GetCurrentPet | [.google.protobuf.Empty](#google-protobuf-Empty) | [PetObjManager](#phoenix-game-PetObjManager) | Returns the current pet. |
| GetCurrentPartner | [.google.protobuf.Empty](#google-protobuf-Empty) | [PetObjManager](#phoenix-game-PetObjManager) | Returns the current partner. |
| SetPetState | [PetStateRequest](#phoenix-game-PetStateRequest) | [.google.protobuf.Empty](#google-protobuf-Empty) | Changes the state of the specified pet. |
| Walk | [.phoenix.Position](#phoenix-Position) | [.google.protobuf.Empty](#google-protobuf-Empty) | Move both your pet and partner to the specified 2D position. |
| AutoAttack | [AutoAttackRequest](#phoenix-game-AutoAttackRequest) | [.google.protobuf.Empty](#google-protobuf-Empty) | Autoattack with your pets. |
| PetAttack | [AttackRequest](#phoenix-game-AttackRequest) | [.google.protobuf.Empty](#google-protobuf-Empty) | Use a skill with your pet. |
| PartnerAttack | [AttackRequest](#phoenix-game-AttackRequest) | [.google.protobuf.Empty](#google-protobuf-Empty) | Use a skill with your partner. |

 



<a name="phoenixapi_protos_game_playermanager-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## phoenixapi/protos/game/playermanager.proto
Player related service and messages.


<a name="phoenix-game-AttackRequest"></a>

### AttackRequest
Message request to attack.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| entity_type | [entities.EntityType](#phoenix-game-entities-EntityType) |  | The entity type you want to attack. |
| entity_id | [sint32](#sint32) |  | The entity ID you want to attack. |
| skill_id | [sint32](#sint32) |  | The skill ID you want to use. |






<a name="phoenix-game-CollectRequest"></a>

### CollectRequest
Message request to collect an NPC.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| npc_id | [sint32](#sint32) |  | The NPC ID. |






<a name="phoenix-game-PickUpRequest"></a>

### PickUpRequest
Message request to pick up an item.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| item_id | [sint32](#sint32) |  | The item ID. |






<a name="phoenix-game-PlayerObjManager"></a>

### PlayerObjManager
Message that contains the player information.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [phoenix.Position](#phoenix-Position) |  | Current 2D position of the player. |
| dest_position | [phoenix.Position](#phoenix-Position) |  | Destiny 2D position the player is walking towards. |
| state | [int32](#int32) |  | The state of the player. It is represented as an int32 but this should be an enum. |
| player | [entities.Player](#phoenix-game-entities-Player) |  | The Player object of your character. |
| id | [sint32](#sint32) |  | The ID of your character. |
| is_resting | [bool](#bool) |  | Controls wether the character is resting or not. |






<a name="phoenix-game-TargetRequest"></a>

### TargetRequest
Message request to target an entity.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| entity_type | [entities.EntityType](#phoenix-game-entities-EntityType) |  | The entity type. |
| entity_id | [sint32](#sint32) |  | The entity ID. |





 

 

 


<a name="phoenix-game-PlayerManager"></a>

### PlayerManager
Services that allos you to read information about your player and perform actions with it.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetPlayerObjManager | [.google.protobuf.Empty](#google-protobuf-Empty) | [PlayerObjManager](#phoenix-game-PlayerObjManager) | Returns informatin about your player. |
| ResetPlayerState | [.google.protobuf.Empty](#google-protobuf-Empty) | [.google.protobuf.Empty](#google-protobuf-Empty) | Resets the current player state (same as walking while you are attacking). |
| Walk | [.phoenix.Position](#phoenix-Position) | [.google.protobuf.Empty](#google-protobuf-Empty) | Walks your player to the specified 2D position. |
| Attack | [AttackRequest](#phoenix-game-AttackRequest) | [.google.protobuf.Empty](#google-protobuf-Empty) | Attack a target using a skill. |
| PickUp | [PickUpRequest](#phoenix-game-PickUpRequest) | [.google.protobuf.Empty](#google-protobuf-Empty) | Picks up an item in the ground. |
| Collect | [CollectRequest](#phoenix-game-CollectRequest) | [.google.protobuf.Empty](#google-protobuf-Empty) | Collect an NPC like ice flower, lettuce, etc. |
| Target | [TargetRequest](#phoenix-game-TargetRequest) | [.google.protobuf.Empty](#google-protobuf-Empty) | Target an entity. |

 



<a name="phoenixapi_protos_game_scenemanager-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## phoenixapi/protos/game/scenemanager.proto
Service and messages related to the game scene.


<a name="phoenix-game-FindRequest"></a>

### FindRequest
Message request to find an entity within the map.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [sint32](#sint32) |  | The ID of the entity. |






<a name="phoenix-game-ItemList"></a>

### ItemList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| items | [entities.Item](#phoenix-game-entities-Item) | repeated | List of items. |






<a name="phoenix-game-MapGrid"></a>

### MapGrid
Message that contains the map grid information.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| width | [sint32](#sint32) |  | Width of the map grid. |
| height | [sint32](#sint32) |  | Height of the map grid. |
| rows | [Row](#phoenix-game-Row) | repeated | List of rows of the grid. |






<a name="phoenix-game-MonsterList"></a>

### MonsterList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| monsters | [entities.Monster](#phoenix-game-entities-Monster) | repeated | List of monsters. |






<a name="phoenix-game-NpcList"></a>

### NpcList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| npcs | [entities.Npc](#phoenix-game-entities-Npc) | repeated | List of npcs. |






<a name="phoenix-game-PlayerList"></a>

### PlayerList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| players | [entities.Player](#phoenix-game-entities-Player) | repeated | List of players. |






<a name="phoenix-game-Row"></a>

### Row
A row is a list of cells.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| cells | [CellType](#phoenix-game-CellType) | repeated | The list of cells for the row. |





 


<a name="phoenix-game-CellType"></a>

### CellType
The type of cells in the map grid.

| Name | Number | Description |
| ---- | ------ | ----------- |
| CELL_TYPE_WALKABLE | 0 | You can walk in this type of cells. |
| CELL_TYPE_OBSTACLE | 1 | You can&#39;t walk in this type of cells. |
| CELL_TYPE_OBSTACLE_2 | 2 | You can&#39;t walk in this type of cells. |


 

 


<a name="phoenix-game-SceneManager"></a>

### SceneManager
Services that allows you to read information about the map you are in.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetPlayers | [.google.protobuf.Empty](#google-protobuf-Empty) | [PlayerList](#phoenix-game-PlayerList) | Returns a list of the players in the map. |
| GetMonsters | [.google.protobuf.Empty](#google-protobuf-Empty) | [MonsterList](#phoenix-game-MonsterList) | Returns a list of monsters in the map. |
| GetItems | [.google.protobuf.Empty](#google-protobuf-Empty) | [ItemList](#phoenix-game-ItemList) | Returns a list of items in the map. |
| GetNpcs | [.google.protobuf.Empty](#google-protobuf-Empty) | [NpcList](#phoenix-game-NpcList) | Returns a list of npcs in the map. |
| FindPlayer | [FindRequest](#phoenix-game-FindRequest) | [entities.Player](#phoenix-game-entities-Player) | Search for the specified player within the map. |
| FindMonster | [FindRequest](#phoenix-game-FindRequest) | [entities.Monster](#phoenix-game-entities-Monster) | Search for the specified monster within the map. |
| FindItem | [FindRequest](#phoenix-game-FindRequest) | [entities.Item](#phoenix-game-entities-Item) | Search for the specified item within the map. |
| FindNpc | [FindRequest](#phoenix-game-FindRequest) | [entities.Npc](#phoenix-game-entities-Npc) | Search for the specified npc within the map. |
| GetAllBosses | [.google.protobuf.Empty](#google-protobuf-Empty) | [MonsterList](#phoenix-game-MonsterList) | Returns a list of all the bosses within the map. |
| GetMapGrid | [.google.protobuf.Empty](#google-protobuf-Empty) | [MapGrid](#phoenix-game-MapGrid) | Returns the map grid. |

 



<a name="phoenixapi_protos_game_skillmanager-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## phoenixapi/protos/game/skillmanager.proto
Skill related service and messages.


<a name="phoenix-game-FindSkillFromIdRequest"></a>

### FindSkillFromIdRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [sint32](#sint32) |  |  |






<a name="phoenix-game-FindSkillFromVnumRequest"></a>

### FindSkillFromVnumRequest



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vnum | [sint32](#sint32) |  |  |






<a name="phoenix-game-Skill"></a>

### Skill
Message that contains the skill information.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| vnum | [sint32](#sint32) |  | Unique ID that represents this skill. Different for every skill in the game. |
| name | [string](#string) |  | Name of the skill. |
| id | [sint32](#sint32) |  | ID of the skill in the skill inventory. |
| type | [SkillType](#phoenix-game-SkillType) |  | The type of the skill. |
| range | [int32](#int32) |  | The range of the skill. |
| area | [int32](#int32) |  | The hit area of the skill. |
| cast_time | [int32](#int32) |  | The cast time of the skill. |
| cool_time | [int32](#int32) |  | The cooldown time of the skill. |
| mana_cost | [int32](#int32) |  | The mana cost of the skill. |






<a name="phoenix-game-SkillList"></a>

### SkillList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| skills | [Skill](#phoenix-game-Skill) | repeated | List of skills. |





 


<a name="phoenix-game-SkillType"></a>

### SkillType
The type of skill.

| Name | Number | Description |
| ---- | ------ | ----------- |
| SKILL_TYPE_DAMAGE | 0 | The skill deals damage to the target. |
| SKILL_TYPE_DEBUFF | 1 | The skill puts a debuff on the target. |
| SKILL_TYPE_BUFF | 2 | The skill is a buff for players. |



<a name="phoenix-game-TargetType"></a>

### TargetType
The type of skill target.

| Name | Number | Description |
| ---- | ------ | ----------- |
| TARGET_TYPE_TARGET | 0 | Needs a target to be casted. |
| TARGET_TYPE_SELF | 1 | Skill is casted on yourself. |
| TARGET_TYPE_SELF_OR_TARGET | 2 | Skill can be casted on yourself or on a target. |
| TARGET_TYPE_NO_TARGET | 3 | No target needed for the skill. |


 

 


<a name="phoenix-game-SkillManager"></a>

### SkillManager
Service that allows reading your character skills.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetSkills | [.google.protobuf.Empty](#google-protobuf-Empty) | [SkillList](#phoenix-game-SkillList) | Returns a list with all your skills. |
| FindSkillFromId | [FindSkillFromIdRequest](#phoenix-game-FindSkillFromIdRequest) | [Skill](#phoenix-game-Skill) | Search for a skill using its ID. |
| FindSkillFromVnum | [FindSkillFromVnumRequest](#phoenix-game-FindSkillFromVnumRequest) | [Skill](#phoenix-game-Skill) | Search for a skill using its VNUM. |
| GetPetSkills | [.google.protobuf.Empty](#google-protobuf-Empty) | [SkillList](#phoenix-game-SkillList) | Returns a list with your pet skills. |
| FindPetSkillFromId | [FindSkillFromIdRequest](#phoenix-game-FindSkillFromIdRequest) | [Skill](#phoenix-game-Skill) | Search for your pet skill using its ID. |
| FindPetSkillFromVnum | [FindSkillFromVnumRequest](#phoenix-game-FindSkillFromVnumRequest) | [Skill](#phoenix-game-Skill) | Search for your pet skill using its VNUM. |
| GetPartnerSkills | [.google.protobuf.Empty](#google-protobuf-Empty) | [SkillList](#phoenix-game-SkillList) | Returns a list with your partner skills. |
| FindPartnerSkillFromId | [FindSkillFromIdRequest](#phoenix-game-FindSkillFromIdRequest) | [Skill](#phoenix-game-Skill) | Search for your partner skill using its ID. |
| FindPartnerSkillFromVnum | [FindSkillFromVnumRequest](#phoenix-game-FindSkillFromVnumRequest) | [Skill](#phoenix-game-Skill) | Search for your partner skill using its VNUM. |

 



<a name="phoenixapi_protos_position-proto"></a>
<p align="right"><a href="#top">Top</a></p>

## phoenixapi/protos/position.proto



<a name="phoenix-Position"></a>

### Position
2D position starting at (0, 0) top left of the map.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| x | [int32](#int32) |  |  |
| y | [int32](#int32) |  |  |





 

 

 

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

