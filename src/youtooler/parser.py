from argparse import ArgumentParser
from .exceptions import InvalidUrl, LevelNotInRange
from .utils import verify_youtube_url

class YoutoolerParser(ArgumentParser):
    '''Responsible for parsing the cli args, checking their validity and making them available to the app'''

    def __init__(self):
        ArgumentParser.__init__(self, description='YouTube viewer BOT based on TOR')
        self.add_argument('url', type=str, help='The url of the target YouTube video')
        self.add_argument('-l', '--level', type=int, default=5, help='The number of concurrent browsers to start', required=False)

    def parse(self, args: list[str]) -> dict:
        '''Returns a dict containing cli args'''

        args_dict = vars(self.parse_args(args))
        self.__check_values__(args_dict)
        
        return args_dict

    def __check_values__(self, args: dict) -> None:
        '''
        Early checks the values passed from the cli

        Raises:
        - InvalidUrl
        - LevelNotInRange
        '''

        if not verify_youtube_url(args.get('url')):
            raise InvalidUrl

        if not args.get('level') in range (1, 11):
            raise LevelNotInRange
