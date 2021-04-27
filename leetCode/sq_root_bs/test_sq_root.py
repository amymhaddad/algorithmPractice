from sq_root import v2_sq_root


def test_sq_root():
    assert v2_sq_root(4) == 2
    assert v2_sq_root(9) == 3
    assert v2_sq_root(8) == 2
    assert v2_sq_root(0) == 0
