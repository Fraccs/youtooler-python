from random import uniform
from time import sleep
from threading import Thread
from .logs import get_log_message, get_error_message
from .tor import Tor
from .utils import get_secure_password, stderr
from .exceptions import TorStartFailedException
from .webdriver import YoutoolerWebdriver

class YoutoolerThread(Thread):
    '''
    Responsible for starting both the Webdriver and TOR

    Args:
    - url: str (The url of the video)
    - video_duration: int (The duration of the video)
    - socks_port: int (The port to assign as SocksPort to TOR)
    - control_port: int (The port to assign as ControlPort to TOR)
    '''

    def __init__(self, url: str, video_duration: int, socks_port: int, control_port: int):
        Thread.__init__(self)
        self.socks_port = socks_port
        self.control_port = control_port
        self.url = url
        self.video_duration = video_duration

    def run(self) -> None:
        # TOR startup
        tor = Tor(self.socks_port, self.control_port, get_secure_password(), '/tmp/youtooler')

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
