"""
https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
"""

from string import ascii_lowercase as lower

def caesar_rotation_v2(string, key):
    index_letter = {i: letter for i, letter in enumerate(lower, 1)}
   
    new_string = [] 
    while len(new_string) < len(string):
        #import pdb; pdb.set_trace()
        for index, letter in index_letter.items():
            if letter in string:
                new_index = index + key
                if new_index > 26:
                    new_index = new_index % 26
                new_string.append(index_letter[new_index])
    return "".join(new_string)

#print(caesar_rotation("iwufqnkqkqoolxzzlzihqfm", 25))

def caesar_rotation(string, key):
    index_letter = {i: letter for i, letter in enumerate(lower, 1)}
   
    new_string = [] 
    for letter in string:
        for index, char in index_letter.items():
            if letter == char:
                new_value = index + key
                if new_value > 26:
                    new_value = new_value % 26
                new_string.append(index_letter[new_value])
    return "".join(new_string)


#print(caesar_rotation("iwufqnkqkqoolxzzlzihqfm", 25))
