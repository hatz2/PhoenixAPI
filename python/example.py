from phoenixapi import phoenix, finder
from time import sleep
import json

if __name__ == "__main__":
    # Replace with the actual character name that you want to connect to
    api = finder.create_api_from_name("Character name") 

    # Logs all the packets that are sent/received from the client
    while api.working():
        if not api.empty():
            msg = api.get_message()
            json_msg = json.loads(msg)

            if json_msg["type"] == phoenix.Type.packet_send.value:
                print("[SEND]: " + json_msg["packet"])
            elif json_msg["type"] == phoenix.Type.packet_recv.value:
                print("[RECV]: " + json_msg["packet"])
        else:
            sleep(0.01) 

    api.close()