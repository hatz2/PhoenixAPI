from tests import *

if __name__ == "__main__":
    try:
        packet_manager.run()
    except RuntimeError as e:
        print(e)
