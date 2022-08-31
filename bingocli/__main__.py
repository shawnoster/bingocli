import argparse
from logging import NullHandler

from bingocli.filelogging import FileLoggerBuilder

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
    services.register_builder('null', FileLoggerBuilder())

    logger = services.get('null', file_path='bingo.log')
    logger.log('Hello World!')
    

if __name__ == '__main__':
    main()
