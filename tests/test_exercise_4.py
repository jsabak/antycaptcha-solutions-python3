from config import Config


def test_positive(fixture):
    step = fixture.common
    seed = step.get_seed()
    step.open_exercise(4, seed)
    step.check_steps_and_click_radio_buttons()
    step.click_check_solution()
    assert step.check_trail() == Config.TEST_PASS_TEXT
    step.back_to_main_page()


def test_negative(fixture):
    step = fixture.common
    seed = step.get_seed()
    step.open_exercise(4, seed)
    step.click_check_solution()
    assert step.check_trail() == Config.TEST_FAIL_TEXT
    step.back_to_main_page()


__author__ = 'GiSDeCain'
