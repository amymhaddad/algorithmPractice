"""
https://www.algoexpert.io/questions/Three%20Number%20Sum
"""

# Solution 1:
def threeNumberSum(array, target):
    array.sort()
    results = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target:
                results.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1

    return results

    # The reason you stop at len(array)-2 is bc I need to account for the left and right pointers


# Solution 2:
def threeNumberSum(array, targetSum):
    results = []
    array.sort()

    for i in range(len(array) - 1):
        first = array[i]
        for k in range(i + 1, len(array)):
            second = array[k]
            for l in range(k + 1, len(array)):
                third = array[l]
                if first + second + third == targetSum:
                    results.append([first, second, third])
    return results
