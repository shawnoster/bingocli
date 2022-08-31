import argparse

from .provider import services
from .consolelogging import ConsoleLoggerBuilder
from .funky import get_funky

def main():
    parser = argparse.ArgumentParser(description='Bingo CLI')
    args = parser.parse_args()
    
    get_funky('uncle at a wedding')

    # register and configure services
    #
    # if dev use console, else datadog
    # how does the factory make this better?
    # services need to be registered before use
    services.register_builder('console', ConsoleLoggerBuilder())

    logger = services.get('console')
    logger.log('Hello World!')
    

if __name__ == '__main__':
    main()
