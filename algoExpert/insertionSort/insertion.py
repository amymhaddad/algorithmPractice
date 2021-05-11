"""
https://www.algoexpert.io/questions/Insertion%20Sort
"""

def insertionSort(array):
    prev_num = 0
    next_num = 1

    while next_num < len(array):
        if array[next_num] >= array[prev_num]:
            next_num += 1
            prev_num += 1
            continue

        elif array[next_num] < array[prev_num]:
            if prev_num == 0:
                swap(prev_num, next_num, array)
            else:
                current = next_num 
                while prev_num >= 0:
                    if array[next_num] < array[prev_num]:
                       # import pdb; pdb.set_trace()
                        swap(prev_num, next_num, array)
                    prev_num -= 1
                    next_num -= 1
            prev_num = current
            next_num = current +1 
    return array
        
def swap(prev_num, next_num, array):
    array[prev_num], array[next_num] = array[next_num], array[prev_num]
    return array

print(insertionSort([5, 8, 2]))


