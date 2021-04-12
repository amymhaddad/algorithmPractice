from max import maxDepth


def test_maxDepth():
    assert maxDepth([3, 9, 20, None, None, 15, 7]) == 3
    assert maxDepth([]) == 0
    assert maxDepth([0]) == 1
