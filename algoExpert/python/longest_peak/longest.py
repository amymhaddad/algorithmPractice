"""
https://www.algoexpert.io/questions/Longest%20Peak
"""
def longestPeak(array):
    longest_peak_len = 0
    i = 1

    while i < len(array) -1:
        is_peak = array[i] > array[i-1] and array[i] > array[i+1]

        if not is_peak:
            i += 1
            continue

        left_index = i - 2
        while left_index >= 0 and array[left_index] < array[left_index+1]:
            left_index -= 1

        right_index = i + 2
        while right_index < len(array) and array[right_index] < array[right_index-1]:
            right_index += 1

        curr_peak_len = right_index - left_index - 1
        longest_peak_len = max(longest_peak_len, curr_peak_len)
        i = right_index
    return longest_peak_len
