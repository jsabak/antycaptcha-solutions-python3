from config import Config


def test_positive(fixture):
    step = fixture.common
    seed = step.get_seed()
    step.open_exercise(3, seed)
    text = step.copy_text(1)
    step.select_from_dropdown_list(text)
    step.click_check_solution()
    assert step.check_trail() == Config.TEST_PASS_TEXT
    step.back_to_main_page()


def test_negative(fixture):
    step = fixture.common
    seed = step.get_seed()
    step.open_exercise(3, seed)
    step.click_check_solution()
    assert step.check_trail() == Config.TEST_FAIL_TEXT
    step.back_to_main_page()


__author__ = 'GiSDeCain'
