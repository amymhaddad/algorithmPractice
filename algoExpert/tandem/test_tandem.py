from tandem import tandem


def test_tandem():
    assert tandem([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True) == 32
    assert tandem([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False) == 11
    assert tandem([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False) == 25
