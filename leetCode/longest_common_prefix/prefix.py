#https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    strs.sort(key=len)
    shortest_word = strs[0]
    longest_prefix_seen_so_far = strs[0]
    
    for i, word in enumerate(strs[1:]):
        for k, letter in enumerate(shortest_word):
            if letter != word[k]:
                if i== 0 and k == 0:
                    return ""
                else:
                    longest_prefix_seen_so_far = shortest_word[:k]
                    break

    return longest_prefix_seen_so_far


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

def longest_common_prefix(strs):
    if not strs:
        return ''

    if len(strs) == 1:
        return strs[0]

    shortest_word = min(strs, key=len)

    i = 0
    while i < len(shortest_word):
        import pdb; pdb.set_trace()
        current_char = strs[0][i]

        for word in strs:
            if word[i] != current_char:
                return shortest_word[:i]

        i += 1

    return shortest_word[:i]

print(longest_common_prefix(["flower","flow","flight"]))
