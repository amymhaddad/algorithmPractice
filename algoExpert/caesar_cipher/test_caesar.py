from caesar import caesar_rotation, caesar


def test_caesar_rotation():
    assert caesar_rotation("xyz", 2) == "zab"
    assert caesar_rotation("iwufqnkqkqoolxzzlzihqfm", 25) == "hvtepmjpjpnnkwyykyhgpel"
    assert caesar_rotation("abc", 52) == "abc"

def test_caesar():
    assert caesar("xyz", 2) == "zab"
    # assert caesar("iwufqnkqkqoolxzzlzihqfm", 25) == "hvtepmjpjpnnkwyykyhgpel"
    # assert caesar("abc", 52) == "abc"


