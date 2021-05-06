from tandem import v2_tandem

def test_tandem():
    assert v2_tandem([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True) == 32
    assert v2_tandem([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False) == 32
