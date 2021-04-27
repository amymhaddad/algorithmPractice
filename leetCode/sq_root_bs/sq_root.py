"""
https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
"""
#update var names
def sq_root(num):
    if num <= 2:
        return num
    low = 1
    high = num 

    while low < high:
        curr = (low + high) // 2
        import pdb; pdb.set_trace()
        if curr * curr == num or in_range(curr, num):
            return curr
        elif curr * curr > num: 
            high = curr - 1
        else:
            low = curr + 1
    return 1

def in_range(num, given):
    res = []
    lower = num * num 
    upper = (num + 1) * (num + 1)
    for i in range(lower, upper):
        res.append(i)
    return given in res


#print(sq_root(5))

def v2_sq_root(num):
    if num <= 2:
        return num 
    low = 1 
    high = num 

    while high - low > 1:
        mid = (low + high) // 2

        if mid * mid >= num:
            high = mid
        else:
            low = mid
    #import pdb; pdb.set_trace()
    if mid * mid == num:
        return mid
    elif num >= low * low and num <= high * high:
        return low 
    
    


print(v2_sq_root(5))



