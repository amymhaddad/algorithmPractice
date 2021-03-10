"""
https://www.algoexpert.io/questions/Run-Length%20Encoding
"""

import re
string = "A  **(())---         AA880001BB123"
matched_letters = re.findall(r'[A-Z]*', string)
#print(matched_letters)


all_letters = []
for letter in string:
    if letter.isalpha():
        all_letters.append(letter)


all_counts = {}
for letter in all_letters:
    all_counts[letter] = all_counts.get(letter, 0) + 1
print(all_counts)
