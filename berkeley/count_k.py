"""
Consider a special version of the count_stair_ways problem, where instead of taking 1 or 2 steps, we are able to take up to and including k steps at a time. Write a function count_k that figures out the number of paths for this scenario. Assume n and k are positive.
"""


def count_k(stairs, steps):
    if stairs == 0:
        return 1

    elif stairs < 0:
        return 0

    else:
        i = 1
        total = 0
        while i <= steps:
            total += count_k(stairs - i, steps)
            i += 1
        return total


print(count_k(3, 3))
