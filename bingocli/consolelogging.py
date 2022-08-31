import imp
from .interfaces.logging import LoggerInterface
from .provider import services

class ConsoleLogger(LoggerInterface):
    """Log a message."""
    def log(self, message: str):
        print(message)

class ConsoleLoggerBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = ConsoleLogger()
        return self._instance
      