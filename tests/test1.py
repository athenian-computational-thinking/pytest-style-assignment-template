import src.fix_code_1


def test_inc():
    assert 5 == src.fix_code_1.name_length("Yulia")
    assert 4 == src.fix_code_1.name_length("Juan")
    assert 9 == src.fix_code_1.name_length("Yvonne Li")