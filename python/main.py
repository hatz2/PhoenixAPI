from tests import *

if __name__ == "__main__":
    try:
        inventory_manager.run()
    except RuntimeError as e:
        print(e)
