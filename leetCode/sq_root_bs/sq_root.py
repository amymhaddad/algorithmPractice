"""
https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
"""
#update var names
def sq_root(num):
    low = 1
    high = num 

    while low < high:
        curr = (low + high) // 2
        #import pdb; pdb.set_trace()
        if curr * curr == num or in_range(curr, num):
            return curr
        elif curr * curr > num: 
            high = curr - 1
        else:
            low = curr + 1
    return -1

def in_range(num, given):
    res = []
    
    #import pdb; pdb.set_trace()
    lower = num * num 
    upper = (num + 1) * (num + 1)
    for i in range(lower, upper):
        res.append(i)
    return given in res

#print(lower, upper)

print(sq_root(8))



