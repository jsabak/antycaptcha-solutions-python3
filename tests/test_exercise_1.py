from time import sleep

from config import Config
from page_objects.po_exercise_1 import *


def test_positive(driver):
    set_driver(driver)
    open_page()

    click_button1()
    click_button2()
    click_button1()

    click_check_soluition()
    assert get_trail_text() == Config.TEST_PASS_TEXT


def test_negative(driver):
    set_driver(driver)
    open_page()

    click_button1()
    click_button1()
    click_button1()

    click_check_soluition()
    assert get_trail_text() == Config.TEST_FAIL_TEXT
