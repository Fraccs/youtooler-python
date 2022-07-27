import isodate
import requests
import string_utils
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
from sys import stderr
from .exceptions import *

def print_logo():
    print(f'{Style.BRIGHT}')
    print(f'{Fore.MAGENTA}                         _____.___.           {Fore.CYAN}___________           .__                ')
    print(f'{Fore.MAGENTA}               />        \\__  |   | ____  __ _{Fore.CYAN}\\__    ___/___   ____ |  |   {Fore.MAGENTA}___________ ')
    print(f'{Fore.MAGENTA}  ()          //----------/   |   |/  _ \\|  |  \\{Fore.CYAN}|    | /  _ \\ /  _ \\|  | {Fore.MAGENTA}_/ __ \\_  __ \\----------\\')
    print(f'{Fore.YELLOW} (*)OXOXOXOXO(*>          \\____   (  <_> )  |  /{Fore.CYAN}|    |(  <_> |  <_> )  |_{Fore.YELLOW}\\  ___/|  | \\/           \\')
    print(f'{Fore.YELLOW}  ()          \\\\----------/ ______|\\____/|____/ {Fore.CYAN}|____| \\____/ \\____/|____/{Fore.YELLOW}\\___  >__|---------------\\   ')
    print(f'{Fore.YELLOW}               \\>         \\/                                      {Fore.YELLOW}            \\/       ')
    print(f'\n{Fore.WHITE}{Back.RED}Developers assume no liability and are not responsible for any misuse or damage caused by this program.{Style.RESET_ALL}')

def get_secure_password(length: int=20) -> str:
    '''
    Returns a secure password of at least 12 characters

    Raises UnsecureLength
    '''

    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!#$%&?@'

    characters = ascii_lowercase + ascii_uppercase + digits + symbols

    if length < 12 or length > len(characters):
        raise UnsecureLength

    shuffled = string_utils.shuffle(characters)
    
    return shuffled[:length]

def get_video_duration(url: str) -> int:
    '''
    Returns the duration in seconds of the passed video
    
    Raises DurationUnestablishedException
    '''

    for _ in range(10): # 10 retries
        try:
            html = requests.get(url)
        except ConnectionError:
            continue

        # Parsing response
        parsed_html = BeautifulSoup(markup=html.text, features='lxml')

        # Searching for the tag <meta itemprop="duration" content="">
        duration_tag = parsed_html.find('meta', {'itemprop': 'duration'})

        if duration_tag is None: # Tag not found
            raise DurationUnestablishedException

        iso_8601_duration = duration_tag.attrs['content']

        # Converting to minutes and seconds
        duration = isodate.parse_duration(iso_8601_duration)

        return duration.seconds
    
    raise DurationUnestablishedException

def get_video_title(url: str) -> str:
    '''
    Returns the title of the passed video
    '''

    for _ in range(10): # 10 retries
        try:
            html = requests.get(url)
        except ConnectionError:
            continue

        parsed_html = BeautifulSoup(markup=html.text, features='lxml')

        # Searching for the tag <meta name="title" content="">
        title_tag = parsed_html.find('meta', {'name': 'title'})
        title = title_tag.attrs['content']
    
    return title

def verify_youtube_url(url: str) -> bool:
    '''
    Returns whether the passed video url is in the correct format and is an existing video

    Format: https://www.youtube.com/watch?v=<video>
    '''
    
    if not url.find('https://www.youtube.com/watch?v=') == 0:
        return False
    
    if url == 'https://www.youtube.com/watch?v=':
        return False

    if url.find('&') != -1:
        return False

    for _ in range(10): # 10 retries
        # Checking if video exists
        try:
            html = requests.get(url)
        except ConnectionError:
            continue

        parsed_html = BeautifulSoup(markup=html.text, features='lxml')

        # Searching for the tag <meta name="title" content="">
        title_tag = parsed_html.find('meta', {'name': 'title'})
        title = title_tag.attrs['content']

        # If title is found the video exists
        return False if title == "" else True
