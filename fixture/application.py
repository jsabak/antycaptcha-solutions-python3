from selenium.webdriver.chrome.webdriver import WebDriver
from src.common import Common
from src.stf import Stf
from config import Config


class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(2)
        self.driver.get(Config.main_page)
        self.common = Common(self)
        self.stf = Stf(self)
        self.common.get_seed()
        self.common.write_seed_to_file()

    def destroy(self):
        self.driver.close()
        self.driver.quit()


__author__ = 'GiSDeCain'
