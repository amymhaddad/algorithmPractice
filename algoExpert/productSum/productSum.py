array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


def productSum(array, depth=1):
    total = 0
    for ele in array:
        if type(ele) is list:
            total += productSum(ele, depth + 1)
        else:
            total += ele
    return total * depth


print(productSum(array))
