from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common import expected_conditions as EC1
from config import Config
import logging as log

_driver = None
_wait = None


def set_driver(driver):
    global _driver
    _driver = driver


def open_page():
    global _wait
    url = f'{Config.MAIN_URL}/{Config.EXERCISES_URL}/exercise2?{Config.SEED_PARAM}'
    log.info(url)
    _driver.get(url)
    _wait = WebDriverWait(_driver, 30)
    log.info('Exercise 1 opened.')


def enter_text_to_t14_editbox(text):
    elt = _driver.find_element_by_id('t14')
    elt.clear()
    elt.send_keys(text)


def press_b1_button():
    prev_text = _driver.find_element_by_class_name('wrap').text
    btn = _driver.find_element(By.ID, 'btnButton1')
    btn.click()
    _wait.until(EC1.text_changed((By.CLASS_NAME, 'wrap'), prev_text))


def click_check_soluition():
    prev_text = _driver.find_element_by_class_name('wrap').text
    btn = _driver.find_element(By.ID, 'solution')
    btn.click()
    _wait.until(EC1.text_changed((By.CLASS_NAME, 'wrap'), prev_text))


def get_trail_text():
    return _driver.find_element_by_class_name('wrap').text
