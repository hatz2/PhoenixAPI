from typing import TypedDict
from enum import Enum

class Direction(int, Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP_LEFT = 4
    UP_RIGHT = 5
    DOWN_RIGHT = 6
    DOWN_LEFT = 7

class EntityType(int, Enum):
    PLAYER = 1
    MONSTER = 2
    NPC = 3
    ITEM = 4

class Position(TypedDict):
    x: int
    y: int

class Player(TypedDict):
    entity_type: EntityType
    id: int
    position: Position
    direction: Direction
    animation_status: int
    speed: int
    is_in_combat: bool
    health_percent: int
    mana_percent: int
    level: int
    champion_level: int
    current_map_id: int
    sp: int
    name: str
    title: str
    family: str
    is_gm: bool
    reputation_rank: int

class Monster(TypedDict):
    entity_type: EntityType
    id: int
    position: Position
    direction: Direction
    animation_status: int
    speed: int
    is_in_combat: bool
    health_percent: int
    mana_percent: int
    level: int
    champion_level: int
    current_map_id: int
    vnum: int
    name: int
    race: int
    skin_id: int
    is_boss: bool

class Item(TypedDict):
    entity_type: EntityType
    id: int
    position: Position
    vnum: int
    quantity: int
    owner_id: int
    is_quest_item: bool
    name: str

class Npc(TypedDict):
    entity_type: EntityType
    id: int
    position: Position
    direction: Direction
    animation_status: int
    speed: int
    is_in_combat: bool
    health_percent: int
    mana_percent: int
    level: int
    champion_level: int
    current_map_id: int
    vnum: int
    name: int
    race: int
    skin_id: int
    is_boss: bool
    owner_id: int