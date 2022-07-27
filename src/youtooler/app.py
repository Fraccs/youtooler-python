import atexit
import shutil
import os
from sys import stderr
from .logs import get_error_message, get_log_message
from .thread import YoutoolerThread
from .utils import get_video_duration

class Youtooler:
    def __init__(self, url: str, level: int):
        self.__storage_directory_path = self.__create_storage_dir__()
        self.__threads = []
        self.level = level
        self.url = url

    def start(self):
        video_duration = get_video_duration(self.url)
        ports = [9050, 9052, 9054, 9056, 9058, 9060, 9062, 9064, 9066, 9068]

        for i in range(self.level):
            self.__threads.append(YoutoolerThread(self.url, video_duration, ports[i]))
        
        for thread in self.__threads:
            thread.setDaemon(True)
            thread.start()
        
        atexit.register(self.stop)

    def stop(self):
        '''
        Stops the execution of the threads and their subprocesses
        '''
        try:
            for thread in self.__threads:
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
