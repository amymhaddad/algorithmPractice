"""
https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/
"""

# linear O(n) solution
def peak(arr):
    max_so_far = arr[0]

    for i, num in enumerate(arr[1:]):
        if num > max_so_far:
            max_so_far = num

    return arr.index(max_so_far)


# O(log n) solution
def v2_peak(arr):

    if len(arr) == 1:
        return 0

    low = 0
    high = len(arr) - 1

    while low < high - 1:
        mid = (low + high) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        elif arr[mid] < arr[mid + 1]:
            low = mid + 1

        else:
            high = mid - 1
    if arr[low] >= arr[high]:
        return low
    return high
