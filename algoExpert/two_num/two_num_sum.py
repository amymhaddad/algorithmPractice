"""
https://www.algoexpert.io/questions/Two%20Number%20Sum
"""

def twoNumberSum(array, targetSum):
    total = []

    for i in range(len(array)):
        for k in range(i+1):
            if array[i] + array[k] == targetSum and i != k:
                total.append(array[i])
                total.append(array[k])
                break
    return total



array = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

print(twoNumberSum(array, target))

#Solution 1 - hash map
def two_num(array, target):
    index_values = {i: num for i, num in enumerate(array)}
    total_values = []

    for i in range(len(array)):
        for key, value in index_values.items():
            if i == key:
                continue
            elif array[i] + value == target:
                if array[i] not in total_values:
                    total_values.append(array[i])
                    total_values.append(value)
                    break   
    return total_values
#print(two_num(array, target))
