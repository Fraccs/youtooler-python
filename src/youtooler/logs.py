from colorama import Fore, Style
from .exceptions import LogMessageException

def get_log_message(log: str, *args) -> str:
    '''
    Returns the log message corresponding to the passed log code
    
    Raises:
    - LogMessageException
    '''

    log_messages = {
        'REQUEST-SUCCESSFUL': 'Successful request made by {} | Tor IP: {}',
        'STORAGE-CREATED': 'Successfully created the storage directory',
        'TOR-STARTED': 'Started TOR on SocksPort {}, ControlPort {}',
        'VIDEO-STARTED': '{} started successfully'
    }

    if log_messages.get(log) is None:
        raise LogMessageException

    if args:
        return f'{Style.BRIGHT}{Fore.GREEN}[log] {log_messages[log].format(*args)}{Style.RESET_ALL}'
    else:
        return f'{Style.BRIGHT}{Fore.GREEN}[log] {log_messages[log]}{Style.RESET_ALL}'

def get_warning_message(warn: str, *args) -> str:
    '''
    Returns the warning message corresponding to the passed warning code
    
    Raises:
    - LogMessageException
    '''

    warning_messages = {
        'PLAY-BTN-NOT-FOUND': 'Could not start the video, the play button could not be found',
        'PLAY-BTN-UNREACHABLE': 'Could not start the video, another element is obscuring the play button',
        'PLAY-BTN-UNSCROLLABLE': 'Could not start the video, the start button could not be scrolled into view',
        'REQUEST-FAILED': 'Unsuccessful request made by {} | Tor IP: {}'
    }

    if warning_messages.get(warn) is None:
        raise LogMessageException

    if args:
        return f'{Style.BRIGHT}{Fore.YELLOW}[warn] {warning_messages[warn].format(*args)}{Style.RESET_ALL}'
    else:
        return f'{Style.BRIGHT}{Fore.YELLOW}[warn] {warning_messages[warn]}{Style.RESET_ALL}'

def get_error_message(err: str, *args) -> str:
    '''
    Returns the error message corresponding to the passed error code
    
    Raises:
    - LogMessageException
    '''

    error_messages = {
        'DATA-NOT-CREATED': 'Could not create the data directory, run the program again',
        'LEVEL-NOT-VALID': 'The passed level is not valid',
        'STORAGE-NOT-CREATED': 'Could not create the storage directory, run the program again',
        'TOR-NOT-STARTED': 'Could not start TOR on SocksPort {}, ControlPort {}',
        'URL-NOT-VALID': 'The passed url is not valid'
    }

    if error_messages.get(err) is None:
        raise LogMessageException
    
    if args:
        return f'{Style.BRIGHT}{Fore.RED}[err] {error_messages[err].format(*args)}{Style.RESET_ALL}'
    else:
        return f'{Style.BRIGHT}{Fore.RED}[err] {error_messages[err]}{Style.RESET_ALL}'
