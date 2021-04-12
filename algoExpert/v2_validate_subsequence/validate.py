"""
https://www.algoexpert.io/questions/Validate%20Subsequence
"""

# Solution 1
def isValidSubsequence(array, subsequence):
    i = 0
    count = 0
    for value in array:
        if i == len(subsequence):
            break
        if subsequence[i] == value:
            count += 1
            i += 1
    return count == len(subsequence)


# Solution 2
def isValidSubsequence(array, sequence):
    arr_index = 0
    seq_index = 0

    while arr_index < len(array) and seq_index < len(sequence):
        if array[arr_index] == sequence[seq_index]:
            seq_index += 1
        arr_index += 1
    return seq_index == len(sequence)
