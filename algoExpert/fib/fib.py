"""
https://www.algoexpert.io/questions/Nth%20Fibonacci
"""

# v1 of fib
def getNthFib_v1(n):
    cache = {}
    cache[1] = 0
    cache[2] = 1
    if n in cache:
        return cache[n]
    else:
        fib_num = getNthFib_v1(n - 1) + getNthFib_v1(n - 2)
        cache[n] = fib_num
        return fib_num


# v2 of fib
def getNthFib_v2(n):
    last_two = [0, 1]
    counter = 3

    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0], last_two[1] = last_two[1], next_fib
        counter += 1
    if n > 1:
        return last_two[1]
    else:
        return last_two[0]


# v3 of fib
def getNthFib_v3(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]

    else:
        memoize[n] = getNthFib_v3(n - 1, memoize) + getNthFib_v3(n - 2, memoize)
        return memoize[n]


# v4 of fib
def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)
