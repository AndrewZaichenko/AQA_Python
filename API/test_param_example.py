import pytest


@pytest.mark.parametrize("f_num, s_num, exp_sum", [(1, 2, 3), (2, 2, 4)])
def test_check_sum(f_num, s_num, exp_sum):
    assert custom_sum(f_num, s_num) == exp_sum


def custom_sum(f_num, s_num):
    return f_num + s_num
