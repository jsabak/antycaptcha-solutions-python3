import logging as log

from selenium.webdriver.support.wait import WebDriverWait

from config import Config

_driver = None
_wait = None


def set_driver(driver):
    global _driver, _wait
    _driver = driver
    _wait = WebDriverWait(_driver, 30)


def open_exercise_page():
    url = f'{Config.MAIN_URL}/{Config.STF_URL}/3-2-1?{Config.SEED_PARAM}'
    log.info(url)
    _driver.get(url)


def open_solution_page():
    url = f'{Config.MAIN_URL}/{Config.STF_URL}/3-2-1/solution?{Config.SEED_PARAM}'
    log.info(url)
    _driver.get(url)


def get_trail_text():
    return _driver.find_element_by_id('trail').text
