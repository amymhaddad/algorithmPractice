"""
https://www.algoexpert.io/questions/Generate%20Document
"""

from collections import Counter


def generate_document(characters, document):
    if len(characters) < len(document):
        return False

    char_counter = Counter(characters)
    doc_counter = Counter(document)

    for letter, count in doc_counter.items():
        if letter in char_counter and char_counter[letter] >= count:
            continue
        else:
            return False

    return True


def generateDocument_v2(characters, document):
    if len(characters) < len(document):
        return False

    char_counter = {}

    for char in characters:
        char_counter[char] = char_counter.get(char, 0) + 1
    for char in document:
        if char not in char_counter:
            return False
        else:
            char_counter[char] -= 1
            if char_counter[char] < 0:
                return False
    return True


def generateDocument_v3(characters, document):

    already_counted = set()
    for char in document:
        if char in already_counted:
            continue
        character_count = characters.count(char)
        document_count = document.count(char)
        if document_count > character_count:
            return False
        already_counted.add(char)
    return True
