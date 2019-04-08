__author__ = 'GiSDeCain'
from page_objects.exercises.po_exercise_3 import *


def test_positive(driver):
    set_driver(driver)
    open_page()

    select_colour('Pink Kong')

    click_check_solution()
    assert get_trail_text() == Config.TEST_PASS_TEXT


def test_negative(driver):
    set_driver(driver)
    open_page()

    select_colour('Beluga Brown')

    click_check_solution()
    assert get_trail_text() == Config.TEST_FAIL_TEXT
