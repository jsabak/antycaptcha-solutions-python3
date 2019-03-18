from config import Config


def test_positive(fixture):
    step = fixture.common
    seed = step.get_seed()
    step.open_exercise(1, seed)
    step.click_all_buttons(3)
    step.click_check_solution()
    assert step.check_trail() == Config.test_pass_text
    step.back_to_main_page()


def test_negative(fixture):
    step = fixture.common
    seed = step.get_seed()
    step.open_exercise(1, seed)
    step.click_check_solution()
    assert step.check_trail() == Config.test_fail_text
    step.back_to_main_page()


__author__ = 'GiSDeCain'
