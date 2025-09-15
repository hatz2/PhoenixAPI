from phoenixapi.api import PhoenixApi
from phoenixapi.finder import create_api_from_name
import dotenv
import os

def run():
    dotenv.load_dotenv()
    api: PhoenixApi = create_api_from_name(os.environ.get("CHAR_NAME"))

    # api.packet_manager.send("u_s 0 3 3070")
    api.packet_manager.recv("tc_info 56 LagMachine16 0 0 3 1 -1 - 11 1 1 5 7 1 5 7 1 5 7 0 0 10000 0 0 0 -1 0 0 0 0 10 0 0 0 0 0 0 0 833")

    # api.packet_manager.subscribe()

    # try:
    #     while True:
    #         for packet in api.packet_manager.get_pending_send_packets():
    #             print(f"[SEND]: {packet}")

    #         for packet in api.packet_manager.get_pending_recv_packets():
    #             print(f"[RECV]: {packet}")
    # except KeyboardInterrupt:
    #     print(f"Interrupted by user")

    # api.packet_manager.unsubscribe()