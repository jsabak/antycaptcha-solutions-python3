from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging as log
from config import Config

log.basicConfig(level=log.INFO)


class Common:

    def __init__(self, app):
        self.app = app



    # def check_right_solution(self):  # This one is an experiment and it's not working yet.
    #     driver = self.app.driver
    #     table = driver.find_elements_by_xpath('//tbody/tr/td')
    #     len_tabel = len(table) / 3
    #     for i in range(int(len_tabel)):
    #         i += 2
    #         solution = driver.find_element_by_xpath('//tbody/tr[' + str(i) + ']/td[3]').text
    #         solution = solution[14:20]
    #         print(solution)  # I have no idea why it's print correctly but if I return it to method it gives "None"

    def copy_text(self, step_number):
        driver = self.app.driver
        text_to_paste = driver.find_element_by_xpath('//tbody/tr[' + str(step_number + 1) + ']/td[2]/code[1]').text
        return text_to_paste

    def paste_text(self, input_id, text_to_paste):
        driver = self.app.driver
        textbox = driver.find_element_by_id(str(input_id))
        textbox.clear()
        textbox.send_keys(text_to_paste)

    def click_check_solution(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 3)
        wait.until(EC.element_to_be_clickable((By.ID, 'solution'))).click()
        log.info('Checking solution...')

    def check_trail(self):
        driver = self.app.driver
        wait = WebDriverWait(driver, 3)
        steps_table = driver.find_elements_by_xpath('//tbody/tr/td')
        len_tabel = len(steps_table) / 3
        solution_text = ''
        control_element = driver.find_element_by_class_name('wrap').text
        for i in range(int(len_tabel)):
            i += 2
            solution_text = driver.find_element_by_xpath('//tbody/tr[' + str(i) + ']/td[3]').text
            solution_text = solution_text[14:20]
        try:
            if solution_text == control_element:
                wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'wrap'), Config.TEST_PASS_TEXT))
            else:
                wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'wrap'), Config.TEST_FAIL_TEXT))
        finally:
            return driver.find_element_by_class_name('wrap').text

    def back_to_main_page(self):
        Common.open_main_page(self)

    def click_button_ex2(self, step_number):  # Thia one is here, because click button not works in ex 2. Dunno why.
        driver = self.app.driver
        btn = driver.find_element_by_xpath('//tbody/tr[' + str(step_number + 1) + ']/td[2]/code')
        if "B1" in btn.text:
            driver.find_element_by_xpath('//*[@id="btnButton1"]').click()
        else:
            driver.find_element_by_xpath('//*[@id="btnButton2"]').click()
        log.info('Button clicked: ' + btn.text)

    def select_from_dropdown_list(self, text_to_past):
        driver = self.app.driver
        element = Select(driver.find_element_by_id('s13'))
        element.select_by_visible_text(text_to_past)
        log.info('Element selected form dropdown list: ' + text_to_past)

    def select_radio_button(self, group_number, text):
        driver = self.app.driver
        driver.find_element_by_xpath("((//div[./h5[text() = 'Group " + str(group_number) + ":']]//text())[.='" + text + "']/preceding-sibling::*)[last()]").click()
        log.info("Selected radio element in group: " + str(group_number))

    def check_steps_and_click_radio_buttons(self):
        driver = self.app.driver
        steps_number = len(driver.find_elements_by_xpath('//tbody/tr'))
        for i in range(steps_number - 1):
            text = Common.copy_text(self, i+1)
            Common.select_radio_button(self, i, text)

    def click_all_buttons(self, buttons_number):
        for i in range(1, buttons_number + 1):
            Common.click_button(self, i)


__author__ = 'GiSDeCain'
