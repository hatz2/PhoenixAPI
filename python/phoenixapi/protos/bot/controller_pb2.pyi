from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoadSettingsRequest(_message.Message):
    __slots__ = ("ini_file_path",)
    INI_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    ini_file_path: str
    def __init__(self, ini_file_path: _Optional[str] = ...) -> None: ...
