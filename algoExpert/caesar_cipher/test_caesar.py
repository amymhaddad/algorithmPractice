from caesar import caesar_rotation


def test_caesar_rotation():
    assert caesar_rotation("xyz", 2) == "zab"
    assert caesar_rotation("iwufqnkqkqoolxzzlzihqfm", 25) == "hvtepmjpjpnnkwyykyhgpel"


