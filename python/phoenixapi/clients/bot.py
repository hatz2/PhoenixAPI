from grpc import Channel
from phoenixapi.protos.bot.controller_pb2 import LoadSettingsRequest
from phoenixapi.protos.bot.controller_pb2_grpc import ControllerStub
from google.protobuf.empty_pb2 import Empty

class ControllerClient:
    """Allows basic control interaction over phoenix bot"""

    def __init__(self, channel: Channel):
        self._stub = ControllerStub(channel)

    def start_farming_bot(self) -> None:
        self._stub.StartFarmingBot(Empty())

    def stop_farming_bot(self) -> None:
        self._stub.StopFarmingBot(Empty())

    def continue_farming_bot(self) -> None:
        self._stub.ContinueFarmingBot(Empty())

    def start_minigame_bot(self) -> None:
        self._stub.StartMinigameBot(Empty())

    def stop_minigame_bot(self) -> None:
        self._stub.StopMinigameBot(Empty())

    def load_settings(self, ini_file_path: str) -> None:
        request = LoadSettingsRequest()
        request.ini_file_path = ini_file_path
        self._stub.LoadSettings(request)