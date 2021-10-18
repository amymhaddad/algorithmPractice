"""
https://www.algoexpert.io/questions/Move%20Element%20To%20End
"""

#Solution 1
def moveElementToEnd(array, toMove):
    array.sort()

    for i, value in enumerate(array):
        if i == 0:
            continue
        if value != toMove:
            num = array.pop(i)
            array.insert(0, num)
            
    return array

#Solution 2
def v2_moveElementToEnd(array, toMove):
    p1, p2 = 0, len(array) -1

    while p2 > p1:
        if array[p1] == toMove and array[p2] != toMove:
            array[p1], array[p2] = array[p2], array[p1]
            p1 += 1
            continue
        elif array[p1] != toMove:
            p1 += 1
            
        elif array[p1] == toMove:
            p2 -= 1
    return array

#Solution 3
def v3_moveElementToEnd(array, toMove):
    p1, p2 = 0, len(array) -1

    while p1 < p2:
        while p1 < p2 and array[p2] == toMove:
            p2 -= 1

        if array[p1] == toMove:
            array[p1], array[p2] = array[p2], array[p1]
        p1 += 1
    return array
