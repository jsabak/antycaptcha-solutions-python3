from config import Config


def test_stf_3_5_1_pos(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-5-1', seed)
    fixture.stf.click_button_by_id(fixture.stf.find_attribute_value())
    fixture.common.click_check_solution()
    assert fixture.common.check_trail() == Config.test_pass_text
    fixture.common.back_to_main_page()


def test_stf_3_5_1_neg(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-5-1', seed)
    fixture.common.click_check_solution()
    assert fixture.common.check_trail() == Config.test_fail_text
    fixture.common.back_to_main_page()


__author__ = 'GiSDeCain'
