from .framework.object_factory import ObjectFactory

class LoggingServiceProvider(ObjectFactory):
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)

services = LoggingServiceProvider()
