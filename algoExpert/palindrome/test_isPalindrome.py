import pytest

from palindrome import isPalindrome


def test_string_is_palindrome_odd_number_of_letters():
    string = "abcdcba"
    assert isPalindrome(string) == True


def test_string_is_palindrome_even_number_of_letters():
    string = "abba"
    assert isPalindrome(string) == True
