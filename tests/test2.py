import src.write_code_2


def test_write_code_2():
    assert 6 == src.write_code_2.concat('cat', 'dog')
    assert 8 == src.write_code_2.concat('aaaa', 'bbbb')
    assert 18 == src.write_code_2.concat('Athenian', 'The School')