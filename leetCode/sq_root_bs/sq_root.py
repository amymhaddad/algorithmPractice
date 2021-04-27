"""
https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
"""
#update var names

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
    if high * high == num:
        return high
    elif num >= low * low and num <= high * high:
        return low 
    
    


print(v2_sq_root(9))

"""
Key points:
-Set bounds w/2 pointers
-Set a condition that'll leave me w/2 values
-Set a question -- looking for the first Y value 
-Post-process

"""



