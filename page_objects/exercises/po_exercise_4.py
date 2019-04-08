import logging as log

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import page_objects.exercises
from common import expected_conditions as EC1
from config import Config

_driver = None
_wait = None


def set_driver(driver):
    global _driver, _wait
    _driver = driver
    _wait = WebDriverWait(_driver, 30)


def open_page():
    url = f'{Config.MAIN_URL}/{Config.EXERCISES_URL}/exercise4?{Config.SEED_PARAM}'
    log.info(url)
    _driver.get(url)
    page_objects.exercises._wait = WebDriverWait(_driver, 30)
    log.info('Exercise 3 opened.')

def check_radio_button_in_a_group(group_no, radio_label):
    prev_text = _driver.find_element_by_class_name('wrap').text
    radio = _driver.find_element_by_xpath(f'((//div[./h5[text() = "Group {group_no}:"]]//text())[.="{radio_label}"]/preceding-sibling::*)[last()]')
    radio.click()
    _wait.until(EC1.text_changed((By.CLASS_NAME, 'wrap'), prev_text))

def click_check_solution():
    prev_text = _driver.find_element_by_class_name('wrap').text
    btn = _driver.find_element(By.ID, 'solution')
    btn.click()
    _wait.until(EC1.text_changed((By.CLASS_NAME, 'wrap'), prev_text))


def get_trail_text():
    return _driver.find_element_by_class_name('wrap').text
