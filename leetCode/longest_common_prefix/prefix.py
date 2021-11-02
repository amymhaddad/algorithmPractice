#https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    strs.sort(key=len)
    shortest_word = strs[0]
    remaining_words = strs[1:]

    index_ptr = 0 
    longest_prefix_seen_so_far = ""
    while index_ptr < len(remaining_words):
        
        curr_word = remaining_words[index_ptr]
        for i, letter in enumerate(curr_word):
            if curr_word == shortest_word:
                longest_prefix_seen_so_far = curr_word
                break 
            #import pdb; pdb.set_trace()
            if i >= len(shortest_word) or letter != shortest_word[i]:
                longest_prefix_seen_so_far = curr_word[:i]
                break

        index_ptr += 1
    return longest_prefix_seen_so_far


#print(longestCommonPrefix(["b",""]))
#print(longestCommonPrefix(["flower","flower","flower","flower"]))
#print(set(["",""]))

def prefix(strs):
    if not strs:
        return ""

    if len(strs) == 1:
        return strs[0]

    shortest_word = min(strs, key=len)
    i = 0

    while i < len(shortest_word):
        import pdb; pdb.set_trace()

        curr_char = strs[0][i]

        for word in strs:
            if word[i] != curr_char:
                return shortest_word[:i]
        i += 1
    return shortest_word[:i]

print(prefix(["flower","flower","flower","flower"]))

"""
Test cases
["flower","flow","flight"]
[""]
["ab", "a"]
["",""] -- 2 empty strings

["flower","flow","flight"]
["dog","racecar","car"]
[""]
["ab", "a"]
["",""]

When working w/n2 problems ask if sorting helps -- esp when deling w/shortest and longest problem statements
FInd the shortest word and comp to other words
"""
