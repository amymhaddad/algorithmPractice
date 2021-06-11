"""
https://www.algoexpert.io/questions/Three%20Number%20Sum
"""

def threeNumberSum(array, targetSum):
    array.sort()
    result = []

    i = 0
    second = 0
    third = len(array) -1 
    while i < len(array):
        while second < third:
            three_num_sum = array[i] + array[second] + array[third]
            if len({array[i], array[second], array[third]}) < 3:
                second += 1
                continue

            if three_num_sum == targetSum:
                new_value = sorted([array[i], array[second], array[third]])
                if new_value not in result:
                    result.append(new_value)
                second = 0
                third = len(array) -1
                break
            elif three_num_sum < targetSum:
                second += 1
            elif three_num_sum > targetSum:
                third -= 1
        i += 1
    result.sort()    
    return result 
            

array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

#print(threeNumberSum(array, targetSum))

def v2_three_num_sum(array, targetSum):
    
    results = []
    
    for i in range(len(array) -1):
        first = array[i]
        for k in range(i+1, len(array)):
            second = array[k]
            for l in range(k+1, len(array)):
                third = array[l]
                if first + second + third == targetSum:
                    results.append(sorted([first, second, third]))
    results.sort()
    return results

print(v2_three_num_sum(array, targetSum))


