"""
https://www.algoexpert.io/questions/Move%20Element%20To%20End
"""

def moveElementToEnd(array, toMove):
    array.sort()

    for i, value in enumerate(array[1:], start=1):
        if value != toMove:
            import pdb; pdb.set_trace()
            num = array.pop(value)
            array.insert(0, num)
            
    return array


array =  [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd(array, toMove))
