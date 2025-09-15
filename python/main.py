from tests import *

if __name__ == "__main__":
    try:
        pet_manager.run()
    except RuntimeError as e:
        print(e)
