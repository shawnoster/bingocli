from .interfaces.logging import LoggerInterface
from .framework.object_factory import ObjectFactory
from .provider import services

class FileLogger(LoggerInterface):
    def __init__(self, file_path) -> None:
        self._file_path = file_path

    def log(self, message: str):
        print(f'Warning: {message}')


class FileLoggerBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, file_path, **_ignored):
        if not self._instance:
            self._instance = FileLogger(file_path)
        return self._instance        
  