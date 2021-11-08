import src.fix_code_2


def test_write_code_2():
    assert 8 == src.fix_code_2.power_it(2, 3)
    assert 27 == src.fix_code_2.power_it(3, 3)
    assert 100 == src.fix_code_2.power_it(10, 2)