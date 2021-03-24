"""
https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
"""

from string import ascii_lowercase as lower

def caeasr(string, key):
    d = {i: letter for i, letter in enumerate(lower, 1)}
    print(d)

print(caeasr("xyz", 2))
