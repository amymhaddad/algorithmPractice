from selection import selection


def test_selection_sort():
    assert selection([8, 5, 2, 9]) == [2, 5, 8, 9]
    assert selection([8, 5, 2, 9, 5, 6, 3]) == [2, 3, 5, 5, 6, 8, 9]
    assert selection([8, 5, 5, 2]) == [2, 5, 5, 8]
    assert selection([8, 5, 2, 5]) == [2, 5, 5, 8]
