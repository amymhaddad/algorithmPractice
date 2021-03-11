"""
https://www.algoexpert.io/questions/Run-Length%20Encoding
"""

import re
string = "A  **(())---         AA880001BB123"

def get_letters(string):
    return [letter  for letter in string if letter.isalpha()]

def count_letters(letters):
    letter_counts = {}
    for letter in letters:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts


def runLengthEncoding(letter_counts):
    encode_string = []

    for letter, count in letter_counts.items():
        while count >= 10:
            encode_string.extend([letter, str(9)])
            count -= 9
        encode_string.extend([letter, str(count)])
    return "".join(encode_string)

letters = get_letters(string)
counts = count_letters(letters)
print(runLengthEncoding(counts))
