from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import expected_conditions as EC1  # ConSelenium rules OK
from config import Config
import logging as log

_driver = None
_wait = None


def set_driver(driver):
    global _driver

    _driver = driver


def open_page():
    global _wait

    url = f'{Config.MAIN_URL}/{Config.EXERCISES_URL}/exercise1?{Config.SEED_PARAM}'
    log.info(url)
    _driver.get(url)
    _wait = WebDriverWait(_driver, 30)
    log.info('Exercise 1 opened.')


def click_button1():
    prev_text = _driver.find_element_by_class_name('wrap').text
    btn = _driver.find_element_by_id('btnButton1')
    btn.click()
    _wait.until(EC1.text_changed((By.CLASS_NAME, 'wrap'), prev_text))


def click_button2():
    prev_text = _driver.find_element_by_class_name('wrap').text
    btn = _driver.find_element_by_id('btnButton2')
    btn.click()
    _wait.until(EC1.text_changed((By.CLASS_NAME, 'wrap'), prev_text))


def click_check_soluition():
    prev_text = _driver.find_element_by_class_name('wrap').text
    btn = _driver.find_element(By.ID, 'solution')
    btn.click()
    _wait.until(EC1.text_changed((By.CLASS_NAME, 'wrap'), prev_text))


def get_trail_text():
    return _driver.find_element_by_class_name('wrap').text
