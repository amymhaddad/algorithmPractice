"""
Given two non-empy arrays of integers, write a funciton taht dtermiens whether the second array is a subsequence of the first.
"""


def validate(array, sequence):
    seq_nums_indexes = {}
    seq_index = 0

    for num in array:
        if seq_index >= len(sequence):
            break
        if num in sequence:
            seq_nums_indexes[seq_index] = num
            seq_index += 1

    matched_seq = {i: num for i, num in enumerate(sequence)}
    return seq_nums_indexes == matched_seq
