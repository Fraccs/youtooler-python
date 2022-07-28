import atexit
import shutil
import os
import signal
from sys import stderr
from .logs import get_error_message, get_log_message
from .thread import YoutoolerThread
from .utils import get_video_duration

class Youtooler:
    '''
    Entrypoint of the app, the args should be passed as an unpacked dict

    Args:
    - url: str (The url of the video)
    - level: int (The number of threads to start)
    '''

    SOCKS_PORT = 9150
    CONTROL_PORT = 9151
    PATH = '/tmp/youtooler'

    def __init__(self, url: str, level: int):
        # Register cleanup handlers
        signal.signal(signal.SIGINT, self.__clean__)
        signal.signal(signal.SIGTERM, self.__clean__)
        atexit.register(self.__clean__)

        self.threads = []
        self.level = level
        self.url = url
        self.socks_ports = [port for port in range(self.SOCKS_PORT, self.SOCKS_PORT + (level * 2), 2)]
        self.control_ports = [port for port in range(self.CONTROL_PORT, self.CONTROL_PORT + (level * 2), 2)]
        self.__create_storage_dir__()

    def start(self) -> None:
        '''Starts the application'''

        video_duration = get_video_duration(self.url)

        for i in range(len(self.socks_ports)):
            self.threads.append(YoutoolerThread(self.url, video_duration, self.socks_ports[i], self.control_ports[i]))
        
        for thread in self.threads:
            thread.setDaemon(True)
            thread.start()

    def __clean__(self, *args) -> None:
        '''Removes the app's storage directory'''

        try:
            for thread in self.threads:
                thread.join()
        except AttributeError:
            pass

        try:
            shutil.rmtree(self.PATH)
        except OSError:
            pass

    def __create_storage_dir__(self) -> None:
        '''Creates the app's storage directory and returns its path'''

        try:
            os.mkdir(self.PATH)
        except FileExistsError:
            print(get_error_message('STORAGE-NOT-CREATED'), file=stderr)
            exit()
        else:
            print(get_log_message('STORAGE-CREATED'))
