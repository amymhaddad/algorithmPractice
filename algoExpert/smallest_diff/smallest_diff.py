"""
https://www.algoexpert.io/questions/Smallest%20Difference
"""

def smallest_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()

    left = len(arr1) -1
    right = 0
    
    min_diff_so_far = abs(arr1[left]) - abs(arr2[right])

    results = {}
    results[min_diff_so_far] = [arr1[left], arr2[right]]

    for i in range(len(arr2)):
        abs_diff = abs(arr1[left] - (arr2[i])) - 0
        if abs_diff > min_diff_so_far:
            break 
        if abs_diff < min_diff_so_far:
            min_diff_so_far = abs_diff
            results[min_diff_so_far] = [arr1[left], arr2[i]]

    smallest_diff = min([value for value in results.keys()])
    return results[smallest_diff]

arr1 = [10, 0, 20, 25]
arr2 = [1005, 1006, 1014, 1032, 1031]

# arr1 = [-1, 5, 10, 20, 28, 3]
# arr2 = [26, 134, 135, 15, 17]
print(smallest_difference(arr1, arr2))
            

