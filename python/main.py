from tests import *

if __name__ == "__main__":
    try:
        login.run()
    except RuntimeError as e:
        print(e)
