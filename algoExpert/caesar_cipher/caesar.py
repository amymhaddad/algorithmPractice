"""
https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
"""

from string import ascii_lowercase as lower

def caeasr(string, key):
    d = {i: letter for i, letter in enumerate(lower, 1)}
   
    new_string = [] 
    for index, letter in d.items():
        if letter in string:

            new_index = index + key
            if new_index > 26:
                new_index = new_index % 26
            new_string.append(d[new_index])
    return new_string

print(caeasr("xyz", 2))
