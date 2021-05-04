from arrays_with_duplicates import get_first_index

def test_get_first_index():
    assert get_first_index([1, 2, 3, 4, 4, 4], 9) == -1
    assert get_first_index([1, 2, 3, 4, 4, 4], 4) == 3
    assert get_first_index([1, 1, 2, 3], 1) == 0

