import sys
from youtooler.app import Youtooler
from youtooler.exceptions import InvalidUrl, LevelNotInRange
from youtooler.logs import get_error_message
from youtooler.parser import YoutoolerParser
from youtooler.utils import print_logo, stderr

def main():
    print_logo()

    parser = YoutoolerParser()
    
    try:
        args = parser.parse(sys.argv[1:])
    except InvalidUrl:
        print(get_error_message('URL-NOT-VALID'), file=stderr)
        exit()
    except LevelNotInRange:
        print(get_error_message('LEVEL-NOT-VALID'), file=stderr)
        exit()
    
    app = Youtooler(**args)
    app.start()

if __name__ == '__main__':
    main()
