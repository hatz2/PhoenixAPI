from phoenixapi.api import PhoenixApi
from phoenixapi.finder import create_api_from_name

def handle_send(client: PhoenixApi, packet: str):
    if packet == "say ping":
        client.packet_manager.recv("spk 1 1 5 Hatz pong")

def handle_recv(client: PhoenixApi, packet: str):
    pass

def run():
    CHAR_NAME = "Insert your character name here"
    client: PhoenixApi = create_api_from_name(CHAR_NAME)

    client.packet_manager.subscribe()

    send_filter = ("ncif", "ptctl")
    recv_filter = ("mv", "eff", "pst", "st", "cond")

    try:
        while True:
            pending_send = client.packet_manager.get_pending_send_packets()

            for packet in pending_send:
                handle_send(client, packet)

                if packet.data.startswith(send_filter):
                    continue

                print(f"[SEND]: {packet}")

            pending_recv = client.packet_manager.get_pending_recv_packets()

            for packet in pending_recv:
                handle_recv(client, packet)

                if packet.data.startswith(recv_filter):
                    continue

                print(f"[RECV]: {packet}")
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        client.packet_manager.unsubscribe()