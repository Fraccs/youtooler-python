from argparse import ArgumentParser
from .exceptions import InvalidUrl, LevelNotInRange
from .utils import verify_youtube_url

class YoutoolerParser(ArgumentParser):
    def __init__(self):
        ArgumentParser.__init__(self, description='YouTube auto-viewer BOT based on TOR')
        
        self.add_argument('url', type=str, help='The url of the target YouTube video')
        self.add_argument('-l', '--level', type=int, default=5, help='The number of concurrent browsers to start', required=False)

    def parse(self):
        args = vars(self.parse_args())
        self.__check_values__(args)
        
        return args

    def __check_values__(self, args: dict):
        if not verify_youtube_url(args.get('url')):
            raise InvalidUrl
        
        if not args.get('level') in range (1, 11):
            raise LevelNotInRange
