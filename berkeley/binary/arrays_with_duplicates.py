"""
Given an array w/dups, find the index of the first occurance of the given
target
"""
arr = [1, 2, 3, 4, 4, 4]
target = 9

def get_first_index(arr, target):
    low = 0 
    high = len(arr)

    while high - low > 1:
        mid = (high + low) // 2
        
        if arr[mid] >= target:
            high = mid
        else:
            low = mid 
    print(low, high, mid)
    if low == mid:
        return high
    if mid > low:
        return low
    return -1

print(get_first_index(arr, target))


"""
Given an array w/dups, find the index of the last occurance of the given
target
"""
#arr = [1, 3, 8, 8, 8, 9]

#arr = [8, 8, 8, 9, 10]
#arr = [1, 2, 3, 4]
#target = 8
def get_last_index(arr, target):
    low = 0 
    high = len(arr)

    while high - low > 1:
        mid = (high + low) // 2

        if arr[mid] <= target:
            low = mid
        else:
            high = mid

    if arr[low] == target:
        return low
    return -1

##print(get_last_index(arr, target))


