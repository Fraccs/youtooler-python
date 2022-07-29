import ipaddress
import os
import re
import shutil
from youtooler.tor import Tor

class TestTor:
    TEST_DIRECTORY = '/tmp/youtooler_test'
    
    os.mkdir(TEST_DIRECTORY) # Temporary storage directory
    
    tor = Tor(9150, 9151, 'test_password_123', TEST_DIRECTORY)

    def test_tor_default(self) -> None:
        assert re.match('^16:[0-9A-F]{58}$', self.tor.hashed_password)
        assert os.path.isfile(self.tor.torrc_path) == True
        assert os.path.isdir(self.tor.data_directory_path) == True

    def test_tor_start(self) -> None:
        self.tor.start()

        assert self.tor.is_tor_started == True

    def test_tor_get_external_address(self) -> None:
        ip = self.tor.get_external_address()

        ipaddress.ip_address(ip)

    def test_tor_renew_circuit(self) -> None:
        ip_start = self.tor.get_external_address()

        self.tor.renew_circuit()

        ip_end = self.tor.get_external_address()

        assert ip_start != ip_end

    def test_tor_stop(self) -> None:
        self.tor.stop()

        assert self.tor.is_tor_started == False

        shutil.rmtree(self.TEST_DIRECTORY)
