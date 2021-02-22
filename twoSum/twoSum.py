"""
Write a function that takes an array of integers and an integer representing a target sum.
If any two numbers in the input array sum to the target sum, then the function returns the numbers in an array. 
If no two numbers sum to the target sum, then return an empty array. You can't add a single integer to itself.
"""
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

#Solution 1
def twoNumSum2(array, targetSum):
    for i, num1 in enumerate(array):
        for k, num2 in enumerate(array[i+1:]):
            if num1 + num2 == targetSum:
                return [array[array.index(num1)], array[array.index(num2)]]
    return []

#Solution 2
def twoNumSum3(array, targetSum):

    index_nums = { num: i for i, num in enumerate(array)}

    for i, num in enumerate(array):
        diff = targetSum - num 
        if diff in index_nums and diff + num == targetSum and num != diff:
            return [diff, num]

    return []


