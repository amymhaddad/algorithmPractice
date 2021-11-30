import pytest

from palindrome import isPalindrome

def test_palindrome():
    assert isPalindrome(121) == True
    assert isPalindrome(123) == False
    assert isPalindrome(10) == False
    assert isPalindrome(-101) == False
    assert isPalindrome(000) == True


