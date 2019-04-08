from config import Config


def test_stf_3_2_1_pos(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-2-1', seed)
    fixture.stf.open_solution_url(seed)
    assert fixture.stf.get_solution() == Config.TEST_PASS_TEXT
    fixture.common.back_to_main_page()


def test_stf_3_2_1_neg(fixture):
    seed = fixture.common.get_seed()
    fixture.stf.open_stf_exercise('3-2-1', seed)
    fixture.stf.open_solution_url('test')
    assert fixture.stf.get_solution() == Config.TEST_FAIL_TEXT
    fixture.common.back_to_main_page()


__author__ = 'GiSDeCain'
