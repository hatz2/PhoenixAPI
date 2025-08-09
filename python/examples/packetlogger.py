from phoenixapi import api, finder

CHAR_NAME = "Insert your character name here"

def handle_send(client: api.Phoenix, packet: str):
    if packet == "say ping":
        client.packet_manager.recv("spk 1 1 5 Hatz pong")


def handle_recv(client: api.Phoenix, packet: str):
    pass

if __name__ == "__main__":
    client: api.Phoenix = finder.create_api_from_name(CHAR_NAME)
    client.packet_manager.subscribe()

    send_filter = ("ncif", "ptctl")
    recv_filter = ("mv", "eff", "pst", "st", "cond")

    try:
        while True:
            pending_send = client.packet_manager.get_pending_send_packets()

            for packet in pending_send:
                handle_send(client, packet.data)

                if packet.data.startswith(send_filter):
                    continue

                print(f"[SEND]: {packet.data}")

            pending_recv = client.packet_manager.get_pending_recv_packets()

            for packet in pending_recv:
                handle_recv(client, packet.data)

                if packet.data.startswith(recv_filter):
                    continue

                print(f"[RECV]: {packet.data}")
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        client.packet_manager.unsubscribe()