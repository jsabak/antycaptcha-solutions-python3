import logging as log
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# locators of web elements
ID_T14 = 't14'
ID_SOLUTION = 'solution'
X_TRAIL = '//pre[@id="trail"]/code'
ID_BUTTON1 = 'btnButton1'
ID_T14 = 't14'

EXERCISE_URL = 'exercises/exercise2'


def test_exercise1_ok(driver, environment):
    url = environment.base_url + EXERCISE_URL + '?seed=' + environment.seed
    log.info('url: ' + url)
    driver.get(url)
    assert driver.title == "AntyCaptcha"

    TEXT = 'Do on teacher.'
    driver.find_element_by_id(ID_T14).clear()
    driver.find_element_by_id(ID_T14).send_keys(TEXT)
    driver.find_element_by_id(ID_BUTTON1).click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, X_TRAIL), 't14:Do on teacher.b1'))
    text = driver.find_element(By.XPATH, X_TRAIL).text
    log.info('trail: ' + text)

    driver.find_element(By.ID, ID_SOLUTION).click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, X_TRAIL), 'OK. Good answer'))
    text = driver.find_element(By.XPATH, X_TRAIL).text
    assert 'OK. Good answer' in text


def test_exercise1_ok_without_wait(driver, environment):
    url = environment.base_url + EXERCISE_URL + '?seed=' + environment.seed
    log.info('url: ' + url)
    driver.get(url)
    assert driver.title == 'AntyCaptcha'

    TEXT = 'Do on teacher.'
    driver.find_element_by_id(ID_T14).clear()
    driver.find_element_by_id(ID_T14).send_keys(TEXT)
    driver.find_element_by_id(ID_BUTTON1).click()
    text = driver.find_element(By.XPATH, X_TRAIL).text
    log.info('trail: ' + text)

    driver.find_element_by_id(ID_SOLUTION).click()
    text = driver.find_element(By.XPATH, X_TRAIL).text
    assert 'OK. Good answer' in text


def test_exercise1_not_ok(driver, environment):
    url = environment.base_url + EXERCISE_URL + '?seed=' + environment.seed
    log.info('url: ' + url)
    driver.get(url)
    assert driver.title == "AntyCaptcha"

    TEXT = 'Blah blah.'
    driver.find_element_by_id(ID_T14).clear()
    driver.find_element_by_id(ID_T14).send_keys(TEXT)
    driver.find_element_by_id(ID_BUTTON1).click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, X_TRAIL), 't14:' + TEXT + 'b1'))
    text = driver.find_element(By.XPATH, X_TRAIL).text
    log.info('trail: ' + text)
    assert TEXT in text

    driver.find_element(By.ID, ID_SOLUTION).click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, X_TRAIL), 'NOT OK.'))
    text = driver.find_element(By.XPATH, X_TRAIL).text
    assert 'NOT OK.' in text
