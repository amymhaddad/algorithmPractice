"""
https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
"""

from string import ascii_lowercase as lower

#Sol 1
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

#Sol 2

def caesar(string, key):
    new_string = []
    
    for letter in string:
        upated_letter = rotate_letter(letter, key)
        new_string.append(upated_letter)
    return "".join(new_string)

def rotate_letter(letter, key):
    min_ord_value = 96
    max_ord_value = 122
    alpha_length = 26

    new_ord_value = ord(letter) + key

    if new_ord_value <= max_ord_value:
        return chr(new_ord_value)

    difference = new_ord_value - max_ord_value
    new_ord_value = min_ord_value + difference % 26
  
    return chr(new_ord_value)

"""
-What you % is the max_length -- the max contraint (ie, the number of spaces you need to rotate)

"""