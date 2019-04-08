from config import Config


def test_positive(fixture):
    step = fixture.common
    seed = step.get_seed()
    step.open_exercise(2, seed)
    text = step.copy_text(1)
    step.paste_text('t14', text)
    step.click_button_ex2(2)
    step.click_check_solution()
    step.check_trail()
    assert step.check_trail() == Config.TEST_PASS_TEXT
    step.back_to_main_page()


def test_negative(fixture):
    step = fixture.common
    seed = step.get_seed()
    step.open_exercise(2, seed)
    step.paste_text('t14', 'test')
    step.click_button_ex2(2)
    step.click_check_solution()
    step.check_trail()
    assert step.check_trail() == Config.TEST_FAIL_TEXT
    step.back_to_main_page()


__author__ = 'GiSDeCain'
