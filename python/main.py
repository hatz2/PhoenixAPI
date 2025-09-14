from tests import *

if __name__ == "__main__":
    try:
        player_obj_manager.run()
    except RuntimeError as e:
        print(e)
