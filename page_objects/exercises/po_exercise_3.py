from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    url = f'{Config.MAIN_URL}/{Config.EXERCISES_URL}/exercise3?{Config.SEED_PARAM}'
    log.info(url)
    _driver.get(url)
    _wait = WebDriverWait(_driver, 30)
    log.info('Exercise 3 opened.')

def select_colour(visible_text):
    prev_text = _driver.find_element_by_class_name('wrap').text
    element = Select(_driver.find_element_by_id('s13'))
    element.select_by_visible_text(visible_text)
    log.info(f'Element selected form dropdown list: {visible_text}')
    _wait.until(EC1.text_changed((By.CLASS_NAME, 'wrap'), prev_text))


def click_check_solution():
    prev_text = _driver.find_element_by_class_name('wrap').text
    btn = _driver.find_element(By.ID, 'solution')
    btn.click()
    _wait.until(EC1.text_changed((By.CLASS_NAME, 'wrap'), prev_text))


def get_trail_text():
    return _driver.find_element_by_class_name('wrap').text
