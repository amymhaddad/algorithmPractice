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
    #start_val = max(red[0], blue[0])
    #totals.append(start_val)
   
    i = 0
    while len(totals) < len(red):
       # import pdb; pdb.set_trace()
        max_val = max(red[i], blue[i])
        min_val = min(red[i], blue[i])
        totals.append(max_val)
        if len(totals) <= len(red):
            totals.append(min_val)
        else:
            break
        i += 1


    return totals


print(v2_tandem(red, blue, fastest))
