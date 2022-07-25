from random import randint
from selenium.common.exceptions import *
from selenium.webdriver import Firefox, DesiredCapabilities
from .logs import get_warning_message, get_log_message
from .utils import get_video_title, stderr
from .tor import Tor

class YoutoolerWebdriver(Firefox):
    def __init__(self, tor: Tor):
        self.tor = tor

    def start(self) -> Firefox:
        # Firefox options
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['proxy'] = {
            'proxyType': 'MANUAL',
            'socksProxy': f'localhost:{self.tor.socks_port}',
            'socksVersion': 5
        }
        
        # Firefox startup
        super().__init__(capabilities=firefox_capabilities)
        self.set_window_size(500, 300)

    def require_video(self, url: str, video_duration: int) -> None:
        try:
            self.get(f'{url}&t={randint(1, video_duration)}s')  
        except:
            print(get_warning_message('REQUEST-FAILED', f'{self.name}-{self.tor.socks_port}', self.tor.get_external_address()), file=stderr)
        else:
            print(get_log_message('REQUEST-SUCCESSFUL', f'{self.name}-{self.tor.socks_port}', self.tor.get_external_address()))

    def accept_cookies(self) -> None:
        # Accepting cookies
        cookie_buttons = self.find_elements_by_css_selector('.yt-simple-endpoint.style-scope.ytd-button-renderer')

        for button in cookie_buttons:
            if button.text == 'ACCEPT ALL':
                button.click()

    def start_video(self, url: str) -> None:
        try:
            self.find_element_by_css_selector('.ytp-large-play-button.ytp-button').click()
        except NoSuchElementException:
            print(get_warning_message('PLAY-BTN-NOT-FOUND'), file=stderr)
        except ElementClickInterceptedException:
            print(get_warning_message('PLAY-BTN-UNREACHABLE'), file=stderr)
        except ElementNotInteractableException:
            print(get_warning_message('PLAY-BTN-UNSCROLLABLE'), file=stderr)
        else:
            print(get_log_message('VIDEO-STARTED', get_video_title(url)))
