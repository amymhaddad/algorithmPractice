from arrays_with_duplicates import get_first_index, get_last_index


def test_get_first_index():
    assert get_first_index([1, 2, 3, 4, 4, 4], 9) == -1
    assert get_first_index([1, 2, 3, 4, 4, 4], 4) == 3
    assert get_first_index([1, 1, 2, 3], 1) == 0
    assert get_first_index([1, 2, 3, 3, 4], 3) == 2


def test_get_last_index():
    assert get_last_index([1, 3, 8, 8, 9], 8) == 3
    assert get_last_index([8, 8, 8, 10, 12], 8) == 2
