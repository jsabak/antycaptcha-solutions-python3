from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import expected_conditions as EC1 # ConSelenium rules OK
from config import Config
import logging as log

_driver = None


def set_driver(driver):
    global _driver
    _driver = driver


def open_page():
    url = f'{Config.MAIN_URL}/{Config.EXERCISES_URL}/exercise1?{Config.SEED_PARAM}'
    log.info(url)
    _driver.get(url)
    log.info('Exercise 1 opened.')


def click_button1():
    prev_text = _driver.find_element_by_class_name('wrap').text
    wait = WebDriverWait(_driver, 3)
    btn = wait.until(EC.element_to_be_clickable((By.ID, 'btnButton1')))
    btn.click()
    wait.until(EC1.text_changed((By.CLASS_NAME, 'wrap'), prev_text))


def click_button2():
    prev_text = _driver.find_element_by_class_name('wrap').text
    wait = WebDriverWait(_driver, 3)
    btn = wait.until(EC.element_to_be_clickable((By.ID, 'btnButton2')))
    btn.click()
    wait.until(text_changed((By.CLASS_NAME, 'wrap'), prev_text))


def check_right_solution():
    wait = WebDriverWait(_driver, 3)
    wait.until(EC.element_to_be_clickable((By.ID, 'solution'))).click()
    return wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'wrap'), Config.TEST_PASS_TEXT))


def check_wrong_solution():
    wait = WebDriverWait(_driver, 3)
    wait.until(EC.element_to_be_clickable((By.ID, 'solution'))).click()
    return wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'wrap'), Config.TEST_FAIL_TEXT))
