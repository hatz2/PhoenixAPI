from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api = create_api_from_name(os.environ.get("CHAR_NAME"))
    api.packet_manager.subscribe()

    try:
        while True:
            pending_send = api.packet_manager.get_pending_send_packets()

            for packet in pending_send:
                print(f"[SEND]: {packet.data}")

            pending_recv = api.packet_manager.get_pending_recv_packets()

            for packet in pending_recv:
                print(f"[RECV]: {packet.data}")
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        api.packet_manager.unsubscribe()
