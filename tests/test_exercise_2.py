from config import Config
from page_objects.po_exercise_2 import *


def test_positive(driver):
    set_driver(driver)
    open_page()

    enter_text_to_t14_editbox('Agree series.')
    press_b1_button()

    click_check_soluition()
    assert get_trail_text() == Config.TEST_PASS_TEXT

def test_negative(driver):
    set_driver(driver)
    open_page()

    enter_text_to_t14_editbox('Some text.')
    press_b1_button()

    click_check_soluition()
    assert get_trail_text() == Config.TEST_FAIL_TEXT


__author__ = 'GiSDeCain'
