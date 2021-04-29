from peak import peak


def test_peak():
    assert peak([1, 2, 3, 1]) == 2
    assert peak([1, 2, 1, 3, 5, 6, 4]) == 2
