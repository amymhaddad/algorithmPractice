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
        #import pdb; pdb.set_trace()
        
        while second < third:
            three_num_sum = array[i] + array[second] + array[third]
            print("total", three_num_sum)
            if three_num_sum == targetSum:
                result.append([array[i], array[second], array[third]])
                i += 1
                break
            elif three_num_sum < targetSum:
                second += 1
            elif three_num_sum > targetSum:
                third -= 1
        i += 1
        
    return result 
            

array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array, targetSum))
