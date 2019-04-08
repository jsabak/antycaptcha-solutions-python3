from config import Config
from page_objects.stf.po_stf_3_2_1 import *


def test_stf_3_2_1_pos(driver):
    set_driver(driver)
    open_exercise_page()

    open_solution_page()

    assert get_trail_text() == Config.TEST_PASS_TEXT

__author__ = 'GiSDeCain'
