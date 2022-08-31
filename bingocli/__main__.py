import argparse
from .funky import get_funky
from .logging import services

def main():
    parser = argparse.ArgumentParser(description='Bingo CLI')
    args = parser.parse_args()
    
    get_funky('uncle at a wedding')
    logger = services.get('console')
    logger.log('Hello World!')
    

if __name__ == '__main__':
    main()
