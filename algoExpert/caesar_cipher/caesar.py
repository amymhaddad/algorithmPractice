"""
https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
"""

from string import ascii_lowercase as lower

def caesar_rotation(string, key):
    alphabet_length = 26
    index_letter = {i: letter for i, letter in enumerate(lower, 1)}
   
    new_string = [] 
    for letter in string:
        for index, char in index_letter.items():
            if letter == char:
                new_value = index + key
                if new_value > alphabet_length:
                    new_value = new_value % alphabet_length
                new_string.append(index_letter[new_value])
    return "".join(new_string)


