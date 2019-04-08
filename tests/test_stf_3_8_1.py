from config import Config


def test_stf_3_8_1_pos(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-8-1', seed)
    fixture.stf.click_alert_button()
    fixture.stf.paste_alert_text(fixture.stf.switch_to_alert_and_copy_text())
    fixture.common.click_check_solution()
    assert fixture.stf.get_solution() == Config.TEST_PASS_TEXT
    fixture.common.back_to_main_page()


def test_stf_3_8_1_neg(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-8-1', seed)
    fixture.stf.click_alert_button()
    fixture.stf.switch_to_alert_and_copy_text()
    fixture.stf.paste_alert_text('test')
    fixture.common.click_check_solution()
    assert fixture.stf.get_solution() == Config.TEST_FAIL_TEXT
    fixture.common.back_to_main_page()


__author__ = 'GiSDeCain'
