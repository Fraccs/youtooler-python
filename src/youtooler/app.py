import atexit
import shutil
import os
import signal
from sys import stderr

from .logs import get_error_message, get_log_message
from .thread import YoutoolerThread
from .tor import Tor
from .utils import get_secure_password, get_video_duration
from .webdriver import YoutoolerWebdriver

class Youtooler:
    '''
    Entrypoint of the app, the args should be passed as an unpacked dict

    Args:
    - url: str (The url of the video)
    - level: int (The number of threads to start)
    '''

    __BASE_SOCKS_PORT = 9150
    __BASE_CONTROL_PORT = 9151
    __STORAGE_DIRECTORY_PATH = '/tmp/youtooler'

    def __init__(self, url: str, level: int, dev: bool):
        self.url = url
        self.level = level
        self.dev = dev

        self.__threads: list[YoutoolerThread] = []
        self.__SOCKS_PORTS = [port for port in range(self.__BASE_SOCKS_PORT, self.__BASE_SOCKS_PORT + (level * 2), 2)]
        self.__CONTROL_PORTS = [port for port in range(self.__BASE_CONTROL_PORT, self.__BASE_CONTROL_PORT + (level * 2), 2)]
        self.__PORT_RANGE = [(self.__SOCKS_PORTS[i], self.__CONTROL_PORTS[i]) for i in range(len(self.__SOCKS_PORTS))]

        self.__start()

    def __start(self) -> None:
        '''Starts the application'''

        # Register cleanup handlers
        signal.signal(signal.SIGINT, self.__clean)
        signal.signal(signal.SIGTERM, self.__clean)
        atexit.register(self.__clean)

        self.__create_storage_dir()

        for (socks_port, control_port) in self.__PORT_RANGE:
            tor = Tor(socks_port, control_port, get_secure_password(), self.__STORAGE_DIRECTORY_PATH)
            webdriver = YoutoolerWebdriver(self.dev, self.url, get_video_duration(self.url))
            webdriver.set_socks_proxy(port=socks_port)

            self.__threads.append(YoutoolerThread(webdriver, tor))
        
        for thread in self.__threads:
            thread.start()

    def __clean(self, *args) -> None:
        '''Removes the app's storage directory'''

        try:
            for thread in self.__threads:
                thread.webdriver.quit()
                thread.tor.stop()
        except AttributeError:
            pass

        try:
            shutil.rmtree(self.__STORAGE_DIRECTORY_PATH)
        except OSError:
            pass

    def __create_storage_dir(self) -> None:
        '''Creates the app's storage directory and returns its path'''

        try:
            os.mkdir(self.__STORAGE_DIRECTORY_PATH)
        except FileExistsError:
            print(get_error_message('STORAGE-NOT-CREATED'), file=stderr)
            exit()
        else:
            print(get_log_message('STORAGE-CREATED'))
