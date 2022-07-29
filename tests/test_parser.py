from pytest import raises
from youtooler.exceptions import InvalidUrl, LevelNotInRange
from youtooler.parser import YoutoolerParser

class TestYoutoolerParser:
    parser = YoutoolerParser()

    def test_parser_parse(self) -> None:
        args_dict = self.parser.parse(['https://www.youtube.com/watch?v=dQw4w9WgXcQ', '--level', '5'])

        for arg in args_dict:
            assert args_dict.get(arg) is not None

    def test_parser_check_values(self) -> None:
        with raises(InvalidUrl):
            self.parser.parse(['https://www.youtube.com/watch?v=notvalid'])

        with raises(LevelNotInRange):
            self.parser.parse(['https://www.youtube.com/watch?v=dQw4w9WgXcQ', '--level', '11'])
            