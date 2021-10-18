"""
https://www.algoexpert.io/questions/Move%20Element%20To%20End
"""

def moveElementToEnd(array, toMove):
    array.sort()

    for i, value in enumerate(array):
        if i == 0:
            continue
        if value != toMove:
            num = array.pop(i)
            array.insert(0, num)
            
    return array




def v2_moveElementToEnd(array, toMove):
    p1, p2 = 0, len(array) -1

    while p2 >= p1:
        if array[p1] == toMove and array[p2] != toMove:
            array[p1], array[p2] = array[p2], array[p1]
            p1 += 1
            continue
        p2 -= 1
        if array[p1] != toMove:
            p1 += 1
    return array


array =  [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(v2_moveElementToEnd(array, toMove))
