"""
https://www.algoexpert.io/questions/Minimum%20Waiting%20Time
"""

array = [3, 2, 1, 2, 6]

def min_waiting_time(array):
    #Account for edge cases -- array of < 2
    #update sorting in place
    array.sort()
    
    prev = 0
    curr = array[0]
    total = []

    for num in array[1:]: 
        total.append(prev + curr)
        prev += curr
        curr = num 
    return sum(total)
print(min_waiting_time(array))

