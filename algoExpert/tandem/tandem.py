"""
https://www.algoexpert.io/questions/Tandem%20Bicycle
"""

def v1_tandem(red, blue, fastest):
    total = []

    for i in range(len(red)):
        for j in range(len(blue)):
            max_per_pair = (red[i], blue[i])
            total.append(max_per_pair)
    return total


red = [5, 5, 3, 9, 2]
blue = [3, 6, 7, 2, 1]
fastest = True

def tandem(red, blue, fastest):
    if fastest:
        return find_max_speeds(red, blue)
    return find_min_speeds(red, blue)

def find_max_speeds(red, blue):
    total = 0 
    red.sort(reverse=True)
    blue.sort()

    for i in range(len(red)):
        max_speed = max(red[i], blue[i])
        total += max_speed
    return total

print(find_max_speeds(red, blue))
