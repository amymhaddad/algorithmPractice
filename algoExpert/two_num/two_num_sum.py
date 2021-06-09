"""
https://www.algoexpert.io/questions/Two%20Number%20Sum
"""

# Solution 1
def twoNumberSum(array, targetSum):
    for i in range(len(array)):
        for k in range(i + 1):
            if array[i] + array[k] == targetSum and i != k:
                return [array[i], array[k]]
    return []


# Soltuion 2
def v2_twoNumberSum(array, target):
    index_values = {i: num for i, num in enumerate(array)}

    for i in range(len(array)):
        for key, value in index_values.items():
            if i == key:
                continue
            elif array[i] + value == target:
                return [array[i], value]
    return []
