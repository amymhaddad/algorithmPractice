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

def v2_tandem(red, blue, fastest):
    red.sort(reverse=True)
    blue.sort(reverse=True)

    totals = []
   
    i = 0
    #Why if I extract out the logic into a var name, the program breaks on the 
    #second check for min speeds? BUT if I hard code the logic, it works?
    #speeds_needed = len(totals) < len(red)
    
    while len(totals) < len(red):
        max_val = max(red[i], blue[i])
        if len(totals) < len(red):
            totals.append(max_val)

        min_val = min(red[i], blue[i])
        if len(totals) < len(red):
            totals.append(min_val)
        i += 1     


    return sum(totals)


print(v2_tandem(red, blue, fastest))
