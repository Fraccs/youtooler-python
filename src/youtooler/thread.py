from random import uniform
from time import sleep
from threading import Thread
from .logs import get_log_message, get_error_message
from .tor import Tor
from .utils import stderr
from .exceptions import TorStartFailedException
from .webdriver import YoutoolerWebdriver

class YoutoolerThread(Thread):
    '''
    Extends threading.Thread

    Takes the target YouTube url and the socks_port for TOR as parameters.
    '''

    def __init__(self, url: str, video_duration: int, socks_port: int):
        Thread.__init__(self)
        self.socks_port = socks_port
        self.url = url
        self.video_duration = video_duration

    def run(self):
        # TOR startup
        tor = Tor(self.socks_port)

        try:
            tor.start()
        except TorStartFailedException:
            print(get_error_message('TOR-NOT-STARTED', tor.socks_port, tor.control_port), file=stderr)
            exit()
        else:
            print(get_log_message('TOR-STARTED', tor.socks_port, tor.control_port))
        
        # WD startup
        driver = YoutoolerWebdriver(tor)
        driver.start()

        while True:
            driver.require_video(self.url, self.video_duration)
            driver.accept_cookies()
            driver.start_video(self.url)

            tor.renew_circuit()
            driver.delete_all_cookies()

            sleep(uniform(10, 15))
