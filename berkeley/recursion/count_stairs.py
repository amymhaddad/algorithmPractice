"""
Imagine that you want to go up a flight of stairs that has n steps, where n is a positive integer. You can either take 1 or 2 steps each time. In this question, you'll write a function count_stair_ways that solves this problem.
"""


def count_stairs(stairs):
    if stairs == 1:
        return 1
    elif stairs == 2:
        return 2

    else:
        return count_stairs(stairs - 1) + count_stairs(stairs - 2)


# print(count_stairs(4))


def count_stairs_cache(stairs, cache={1: 1, 2: 2}):

    if stairs in cache:
        return cache[stairs]

    else:
        cache[stairs] = count_stairs_cache(stairs - 1) + count_stairs_cache(stairs - 2)
        return cache[stairs]


print(count_stairs_cache(4))
