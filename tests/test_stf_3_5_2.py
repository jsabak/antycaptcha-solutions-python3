from config import Config


def test_stf_3_5_2_pos(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-5-2', seed)
    fixture.stf.click_button_by_class_name(fixture.stf.find_attribute_value())
    fixture.common.click_check_solution()
    assert fixture.common.check_trail() == Config.TEST_PASS_TEXT
    fixture.common.back_to_main_page()


def test_stf_3_5_2_neg(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-5-2', seed)
    fixture.common.click_check_solution()
    assert fixture.common.check_trail() == Config.TEST_FAIL_TEXT
    fixture.common.back_to_main_page()


__author__ = 'GiSDeCain'
