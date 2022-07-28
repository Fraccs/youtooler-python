import atexit
import shutil
import os
from sys import stderr
from .logs import get_error_message, get_log_message
from .thread import YoutoolerThread
from .utils import get_video_duration

SOCKS_PORT = 9150
CONTROL_PORT = 9151

class Youtooler:
    def __init__(self, url: str, level: int):
        self.__storage_directory_path = self.__create_storage_dir__()
        self.threads = []
        self.level = level
        self.url = url
        self.socks_ports = [port for port in range(SOCKS_PORT, SOCKS_PORT + (level * 2), 2)]
        self.control_ports = [port for port in range(CONTROL_PORT, CONTROL_PORT + (level * 2), 2)]

    def start(self):
        video_duration = get_video_duration(self.url)

        for port in self.socks_ports:
            self.threads.append(YoutoolerThread(self.url, video_duration, port))
        
        for thread in self.threads:
            thread.setDaemon(True)
            thread.start()
        
        atexit.register(self.stop)

    def stop(self):
        '''
        Stops the execution of the threads and their subprocesses
        '''
        try:
            for thread in self.threads:
                thread.join()
        except AttributeError:
            pass

        self.__clean__()

    def __clean__(self):
        '''
        Removes the temporary storage directory and its subdirectories
        '''

        try:
            shutil.rmtree(self.__storage_directory_path)
        except OSError:
            pass

    def __create_storage_dir__(self) -> str:
        '''
        Creates the temporary storage directory of the program ('/tmp/youtooler') and returns its path
        '''

        PATH = '/tmp/youtooler'

        try:
            os.mkdir(PATH)
        except FileExistsError:
            print(get_error_message('STORAGE-NOT-CREATED'), file=stderr)
            exit()
        else:
            print(get_log_message('STORAGE-CREATED'))

        return PATH
