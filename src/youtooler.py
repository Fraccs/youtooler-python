from youtooler.app import Youtooler
from youtooler.logs import get_error_message
from youtooler import utils

def main():
    utils.print_logo()

    app = Youtooler()
    args = utils.get_arguments() # Parsing CLI args

    if utils.verify_youtube_url(args.url):
        app.start(args.url)
    else:
        print(get_error_message('INVALID-URL'), file=utils.stderr)

if __name__ == '__main__':
    main()
