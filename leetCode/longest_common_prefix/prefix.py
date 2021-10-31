#https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):

    strs.sort()
    print(strs)


#print(longestCommonPrefix(["b",""]))
print(longestCommonPrefix(["flower","flow","flight"]))
#print(set(["",""]))


"""
Test cases
["flower","flow","flight"]
[""]
["ab", "a"]
["",""] -- 2 empty strings

When working w/n2 problems ask if sorting helps -- esp when deling w/shortest and longest problem statements
FInd the shortest word and comp to other words
"""
