import queue
import socket
import threading
import json
import enum

class Type(enum.Enum):
    packet_send = 0
    packet_recv = 1
    attack = 2
    player_skill = 3
    player_walk = 4
    pet_skill = 5
    partner_skill = 6
    pets_walk = 7
    pick_up = 8
    collect = 9
    start_bot = 10
    stop_bot = 11
    continue_bot = 12
    load_settings = 13
    start_minigame_bot = 14
    stop_minigame_bot = 15
    query_player_info = 16
    query_inventory = 17
    query_skills_info = 18
    query_map_entities = 19
    target_entity = 20

class Api:
    HOST = "127.0.0.1"

    def __init__(self, port : int) -> None:
        self._socket = socket.socket()
        self._socket.connect((Api.HOST, port))

        self._do_work = True
        self._messages = queue.Queue()
        self._worker = threading.Thread(target = self._work)
        self._worker.start()

    def _send_data(self, data : str) -> int:
        buffer = data + '\1'
        return self._socket.send(buffer.encode())


    def _work(self) -> None:
        buffer_size = 4096
        data = b''
        delim_char = b'\1'

        while self._do_work:
            buffer = self._socket.recv(buffer_size)

            if (len(buffer) <= 0):
                break

            data += buffer
            delim_pos = data.find(delim_char)

            while delim_pos != -1:
                msg = data[0:delim_pos]
                data = data[delim_pos + 1:]
                decoded_msg = msg.decode()
                self._messages.put(decoded_msg)
                delim_pos = data.find(delim_char)

    def working(self) -> bool:
        return self._worker.is_alive()

    def close(self) -> None:
        if self.working():
            self._do_work = False
            self._worker.join()  

    def get_message(self) -> str:
        if self._messages.empty():
            return ""

        return self._messages.get()

    def empty(self) -> bool:
        return self._messages.empty()

    def send_packet(self, packet : str) -> bool:
        data = {
            "type" : Type.packet_send.value,
            "packet" : packet
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def recv_packet(self, packet : str) -> bool:
        data = {
            "type" : Type.packet_recv.value,
            "packet" : packet
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def attack_monster(self, monster_id : int) -> bool:
        data = {
            "type" : Type.attack.value,
            "monster_id" : monster_id
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def use_player_skill(self, monster_id : int, skill_id : int) -> bool:
        data = {
            "type" : Type.player_skill.value,
            "monster_id" : monster_id,
            "skill_id" : skill_id
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def player_walk(self, x : int, y : int) -> bool:
        data = {
            "type" : Type.player_walk.value,
            "x" : x,
            "y" : y
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def use_pet_skill(self, monster_id : int, skill_id : int) -> bool:
        data = {
            "type" : Type.pet_skill.value,
            "monster_id" : monster_id,
            "skill_id" : skill_id
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def use_partner_skill(self, monster_id : int, skill_id : int) -> bool:
        data = {
            "type" : Type.partner_skill.value,
            "monster_id" : monster_id,
            "skill_id" : skill_id
        }

        json_data = json.dumps(data)
        
        return self._send_data(json_data) == len(json_data) + 1

    def pets_walk(self, x : int, y : int) -> bool:
        data = {
            "type" : Type.pets_walk.value,
            "x" : x,
            "y" : y
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def pick_up(self, item_id : int) -> bool:
        data = {
            "type" : Type.pick_up.value,
            "item_id" : item_id
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def collect(self, npc_id : int) -> bool:
        data = {
            "type" : Type.collect.value,
            "npc_id" : npc_id
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def start_bot(self) -> bool:
        data = {
            "type" : Type.start_bot.value
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def stop_bot(self) -> bool:
        data = {
            "type" : Type.stop_bot.value
        }
            
        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def continue_bot(self) -> bool:
        data = {
            "type" : Type.continue_bot.value
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def load_settings(self, settings_path : str) -> bool:
        data = {
            "type" : Type.load_settings.value,
            "path" : settings_path
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def start_minigame_bot(self) -> bool:
        data = {
            "type" : Type.start_minigame_bot.value
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def stop_minigame_bot(self) -> bool:
        data = {
            "type" : Type.stop_minigame_bot.value
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def query_player_information(self) -> bool:
        data = {
            "type" : Type.query_player_info.value
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def query_inventory(self) -> bool:
        data = {
            "type" : Type.query_inventory.value
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) +  1

    def query_skills_info(self) -> bool:
        data = {
            "type" : Type.query_skills_info.value
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1

    def query_map_entities(self) -> bool:
        data = {
            "type" : Type.query_map_entities.value
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1
    
    def target_entity(self, entity_id : int, entity_type: int):
        data = {
            "type" : Type.target_entity.value,
            "entity_id" : entity_id,
            "entity_type" : entity_type
        }

        json_data = json.dumps(data)

        return self._send_data(json_data) == len(json_data) + 1