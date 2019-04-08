from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging as log
from config import Config
import time

log.basicConfig(level=log.INFO)


class Stf:

    def __init__(self, app):
        self.app = app

    def open_stf_exercise(self, number, seed):
        driver = self.app.driver
        wait = WebDriverWait(driver, 10)
        sub_locator = Config.STF_URL + str(number) + Config.SEED_PARAM + str(seed)  # It is a string for main_page_title xpath locator.
        main_page_title = driver.find_element_by_xpath('//a[@href="/' + sub_locator + '"]').text  # find anchor text using anchor href. It is title of exercise on main page for later assertion.
        url = Config.MAIN_URL + Config.STF_URL + str(number) + Config.SEED_PARAM + str(seed)  # Exercise URL
        driver.get(url)
        stf_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'title'))).text  # Exercise title on exercise page. collected for assertion.
        print(main_page_title.lower() == stf_title.lower())
        # assert main_page_title.lower() in stf_title.lower()
        log.info('STF exercise ' + str(number) + ' opened successful')

    def open_solution_url(self, seed):
        driver = self.app.driver
        url = Config.MAIN_URL + Config.STF_URL + '3-2-1/solution' + Config.SEED_PARAM + str(seed)
        driver.get(url)
        log.info('Opened solution page using url: ' + url)

    def get_solution(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 3)
        time.sleep(1)
        trail = wait.until(EC.presence_of_element_located((By.ID, 'trail'))).text
        log.info('Trail answer is: ' + trail)
        return trail

    def find_attribute_value(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 3)
        btn_locator = wait.until(EC.presence_of_element_located((By.XPATH, '//ol/li[1]/em')))
        log.info('Button id is: ' + btn_locator.text)
        return btn_locator.text

    def click_button_by_id(self, btn_id):
        driver = self.app.driver
        wait = WebDriverWait(driver, 3)
        btn = wait.until(EC.element_to_be_clickable((By.ID, btn_id)))
        btn.click()
        log.info('Text of located button is: ' + btn.text)

    def click_button_by_class_name(self, btn_class):
        driver = self.app.driver
        wait = WebDriverWait(driver, 3)
        btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, btn_class)))
        btn.click()
        log.info('Text of located button is: ' + btn.text)

    def click_button_by_tag_name(self, btn_tag):
        driver = self.app.driver
        wait = WebDriverWait(driver, 3)
        btn_tag = btn_tag[1:3]
        btn = wait.until(EC.visibility_of_element_located((By.TAG_NAME, str(btn_tag))))
        btn.click()

    def fake_click_button_by_tag_name(self, btn_tag):
        driver = self.app.driver
        wait = WebDriverWait(driver, 3)
        btn_tag = btn_tag[1:3]
        if btn_tag == 'h1':
            btn_tag = 'h2'
        elif btn_tag == 'h2':
            btn_tag = 'h3'
        elif btn_tag == 'h3':
            btn_tag = 'h4'
        elif btn_tag == 'h4':
            btn_tag = 'h5'
        elif btn_tag == 'h5':
            btn_tag = 'h6'
        elif btn_tag == 'h6':
            btn_tag = 'h7'
        elif btn_tag == 'h7':
            btn_tag = 'h1'
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, str(btn_tag)))).click()

    def click_alert_button(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 3)
        wait.until(EC.element_to_be_clickable((By.ID, 'showAlert'))).click()

        log.info('Alert button clicked.')

    def switch_to_alert_and_copy_text(self):
        driver = self.app.driver
        time.sleep(1)
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def paste_alert_text(self, alert_text):
        driver = self.app.driver
        textbox = driver.find_element_by_id('alertText')
        textbox.clear()
        textbox.send_keys(alert_text)
        log.info('Alert text is: ' + alert_text)


__author__ = 'GiSDeCain'
