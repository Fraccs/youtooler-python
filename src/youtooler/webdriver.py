from random import randint
from selenium.common.exceptions import *
from selenium.webdriver import Firefox, DesiredCapabilities, FirefoxOptions
from time import sleep

from .logs import get_warning_message, get_log_message
from .utils import get_video_title, stderr

class YoutoolerWebdriver(Firefox):
    '''
    Firefox webdriver adapted to Youtooler needs

    Args:
    - url: str (The url of the video)
    - video_duration: int (The duration in seconds of the video)
    
    Optionals:
    - width: int=500 (The width of the Firefox window)
    - height: int=300 (The height of the Firefox window)
    '''

    def __init__(self, headless: bool, url: str, video_duration: int, width: int=500, height: int=300):
        self.headless = headless
        self.url = url
        self.video_duration = video_duration
        self.width = width
        self.height = height
        self.capabilities = DesiredCapabilities.FIREFOX

    def set_socks_proxy(self, address: str='localhost', port: int=9150) -> None:
        # Firefox options
        self.capabilities['proxy'] = {
            'proxyType': 'MANUAL',
            'socksProxy': f'{address}:{port}',
            'socksVersion': 5
        }

    def start(self) -> None:
        '''Starts the Webdriver'''
        options = FirefoxOptions()

        if not self.headless:
            options.headless = True

        # Firefox startup
        super().__init__(options=options)
        self.set_window_size(self.width, self.height)

    def require_video(self) -> None:
        '''Requires the video with a random time parameter value'''

        try:
            self.get(f'{self.url}&t={randint(1, self.video_duration)}s')  
        except:
            print(get_warning_message('REQUEST-FAILED', f'', f''), file=stderr)
        else:
            print(get_log_message('REQUEST-SUCCESSFUL', f'', f''))

    def accept_cookies(self) -> None:
        '''Accepts the YouTube cookies'''

        sleep(6)

        # Accepting cookies
        cookie_buttons = self.find_elements_by_css_selector('.yt-simple-endpoint.style-scope.ytd-button-renderer')

        for button in cookie_buttons:
            if button.text == 'ACCEPT ALL':
                try:
                    button.click()
                except StaleElementReferenceException:
                    print(get_warning_message('PLAY-BTN-UNREACHABLE'), file=stderr)

    def start_video(self) -> None:
        '''Searches the start button and starts the video'''

        sleep(6)

        try:
            self.find_element_by_css_selector('.ytp-large-play-button.ytp-button').click()
        except NoSuchElementException:
            print(get_warning_message('PLAY-BTN-NOT-FOUND'), file=stderr)
        except ElementClickInterceptedException:
            print(get_warning_message('PLAY-BTN-UNREACHABLE'), file=stderr)
        except ElementNotInteractableException:
            print(get_warning_message('PLAY-BTN-UNSCROLLABLE'), file=stderr)
        else:
            print(get_log_message('VIDEO-STARTED', get_video_title(self.url)))
