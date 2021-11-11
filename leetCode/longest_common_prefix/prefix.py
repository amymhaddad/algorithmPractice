#https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    shortest_word = min(strs, key=len)

    for i, letter in enumerate(shortest_word):
        for word in strs:
            if word[i] != letter:
                return shortest_word[:i]
    return shortest_word
