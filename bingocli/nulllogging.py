from .interfaces.logging import LoggerInterface
from .framework.object_factory import ObjectFactory
from .provider import services

class NullLogger(LoggerInterface):
    def log(self, message: str):
        print(f'Warning: {message}')

class NullLoggerBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = NullLogger()
        return self._instance        

services.register_builder('null', NullLoggerBuilder())
  