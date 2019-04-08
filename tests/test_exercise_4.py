from config import Config

from page_objects.exercises.po_exercise_4 import *


def test_positive(driver):
    set_driver(driver)
    open_page()

    check_radio_button_in_a_group(0, "Pink Kong")
    check_radio_button_in_a_group(1, "Beluga Brown")
    check_radio_button_in_a_group(2, "Pink Kong")
    check_radio_button_in_a_group(3, "Mango Orange")

    click_check_solution()
    assert get_trail_text() == Config.TEST_PASS_TEXT


def test_negative(driver):
    set_driver(driver)
    open_page()

    check_radio_button_in_a_group(0, "Pink Kong")
    check_radio_button_in_a_group(1, "Pink Kong")
    check_radio_button_in_a_group(2, "Pink Kong")
    check_radio_button_in_a_group(3, "Mango Orange")

    click_check_solution()
    assert get_trail_text() == Config.TEST_FAIL_TEXT


__author__ = 'GiSDeCain'
