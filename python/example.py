from phoenixapi import phoenix
from time import sleep
import json

if __name__ == "__main__":
    # Put the port from the bot title, it should look something like
    # [Lv 99.(+80) CharacterName] - Phoenix Bot:123123
    port = 123123 
    api = phoenix.Api(port)

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