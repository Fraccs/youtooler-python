from random import uniform
from time import sleep
from threading import Thread

from .exceptions import TorStartFailedException
from .logs import get_log_message, get_error_message
from .tor import Tor
from .utils import stderr
from .webdriver import YoutoolerWebdriver

class YoutoolerThread(Thread):
    '''
    Responsible for starting both the Webdriver and TOR

    Args:
    - webdriver: YoutoolerWebdriver (YoutoolerWebdriver object)
    - tor: Tor (Tor object)
    '''

    def __init__(self, webdriver: YoutoolerWebdriver, tor: Tor):
        Thread.__init__(self)
        self.tor = tor
        self.webdriver = webdriver

    def run(self) -> None:
        try:
            self.tor.start()
        except TorStartFailedException:
            print(get_error_message('TOR-NOT-STARTED', self.tor.socks_port, self.tor.control_port), file=stderr)
            exit()
        else:
            print(get_log_message('TOR-STARTED', self.tor.socks_port, self.tor.control_port))
        
        # WD startup
        self.webdriver.start()

        while True:
            self.webdriver.require_video()
            self.webdriver.accept_cookies()
            self.webdriver.start_video()

            self.tor.renew_circuit()
            self.webdriver.delete_all_cookies()

            sleep(uniform(10, 15))
