import atexit
import shutil
import os
from sys import stderr
from .logs import get_error_message, get_log_message
from .thread import YoutoolerThread
from .utils import get_video_duration

class Youtooler:
    def __init__(self):
        self.__exit_handler = atexit.register(self.stop)
        self.__storage_dir = self.__create_storage_dir__()
        self.socks_ports = [9050, 9052, 9054, 9056, 9058]
        self.threads = []

    def start(self, url: str):
        '''
        Starts 5 threads with one TOR subprocess each
        Default socks_ports: 9050, 9052, 9054, 9056, 9058
        '''

        video_duration = get_video_duration(url)

        for port in self.socks_ports:
            self.threads.append(YoutoolerThread(url, video_duration, port))
        
        for thread in self.threads:
            thread.setDaemon(True)
            thread.start()

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
            shutil.rmtree('/tmp/youtooler')
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
