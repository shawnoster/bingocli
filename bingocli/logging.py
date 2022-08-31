import abc

from .object_factory import ObjectFactory

class LoggerInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'log') and
                callable(subclass.log))

    @abc.abstractmethod
    def log(self, message: str):
        raise NotImplementedError

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

class LoggingServiceProvider(ObjectFactory):
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)

services = LoggingServiceProvider()
services.register_builder('console', ConsoleLoggerBuilder())
services.register_builder('null', NullLoggerBuilder())
   