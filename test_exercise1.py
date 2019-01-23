import logging as log
from time import sleep
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXERCISE_URL: str = 'exercises/exercise1'

def test_exercise1_ok(driver, prod_environment):
    log.info('url:' + prod_environment.base_url + EXERCISE_URL)
    driver.get(prod_environment.base_url + EXERCISE_URL)
    assert driver.title == "Ćwiczenie 1"

    wait = WebDriverWait(driver,10)
    driver.find_element_by_id('btnButton1').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH,'//pre[@id="trail"]/code'), 'b1'))
    # sleep(1)
    driver.find_element_by_id('btnButton2').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH,'//pre[@id="trail"]/code'), 'b1b2'))
    # sleep(1)
    driver.find_element_by_id('btnButton1').click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH,'//pre[@id="trail"]/code'), 'b1b2b1'))
    # sleep(1)
    text = driver.find_element(By.XPATH, '//pre[@id="trail"]/code').text
    log.info('trail: ' + text)

    driver.find_element(By.ID, 'end').click()
    sleep(1)
    text = driver.find_element(By.XPATH, '//pre[@id="trail"]/code').text
    assert 'OK. Good answer' in text

def test_exercise1_ok_without_wait(driver, local_environment):
    log.info('url:' + local_environment.base_url + EXERCISE_URL)
    driver.get(local_environment.base_url + EXERCISE_URL)
    assert driver.title == "Ćwiczenie 1"

    driver.find_element_by_id('btnButton1').click()
    driver.find_element_by_id('btnButton2').click()
    driver.find_element_by_id('btnButton1').click()
    text = driver.find_element(By.XPATH, '//pre[@id="trail"]/code').text
    log.info('trail: ' + text)

    driver.find_element(By.ID, 'end').click()
    text = driver.find_element(By.XPATH, '//pre[@id="trail"]/code').text
    assert 'OK. Good answer' in text


def test_petla(driver, local_environment):
    driver.get(local_environment.base_url + EXERCISE_URL)
    assert driver.title == "Ćwiczenie 1"

    for i in range(100):
        driver.find_element_by_id('btnButton1').click()
        text = driver.find_element(By.XPATH, '//pre[@id="trail"]/code').text
        log.info('trail:' + text)

    assert 'b1'*100 in text


def test_exercise1_not_ok(driver, local_environment):
    log.info('url:' + local_environment.base_url + EXERCISE_URL)
    driver.get(local_environment.base_url + EXERCISE_URL)
    assert driver.title == "Ćwiczenie 1"

    driver.find_element_by_id('btnButton1').click()
    driver.find_element_by_id('btnButton1').click()
    driver.find_element_by_id('btnButton1').click()
    text = driver.find_element(By.XPATH, '//pre[@id="trail"]/code').text
    log.info('trail: ' + text)

    driver.find_element(By.ID, 'end').click()
    text = driver.find_element(By.XPATH, '//pre[@id="trail"]/code').text
    assert 'NOT OK.' in text
