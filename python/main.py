from tests import *

if __name__ == "__main__":
    try:
        bot_controller.run()
    except RuntimeError as e:
        print(e)
