import pytest

from prefix import longestCommonPrefix

def test_longestCommonPrefix():
    assert longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
    # assert longestCommonPrefix(['dog', 'racecar', 'car']) == ''
    # assert longestCommonPrefix([]) == ''
    # assert longestCommonPrefix(['']) == ''
    # assert longestCommonPrefix(['a']) == 'a'
    # assert longestCommonPrefix(['', '']) == ''
    # assert longestCommonPrefix(['aa', 'a']) == 'a'
