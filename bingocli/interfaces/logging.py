import abc

class LoggerInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'log') and
                callable(subclass.log))

    @abc.abstractmethod
    def log(self, message: str):
        raise NotImplementedError