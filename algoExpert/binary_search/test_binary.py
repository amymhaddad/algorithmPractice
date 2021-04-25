from binary import binary

def test_binary():
    assert binary([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],33) == 3
    assert binary([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0) == 0
