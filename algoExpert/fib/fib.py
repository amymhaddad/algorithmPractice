"""
https://www.algoexpert.io/questions/Nth%20Fibonacci
"""

def getNthFib(n):
	cache = {} 
	cache[1] = 0
	cache[2] = 1
	if n in cache:
		return cache[n]
	else:
		fib_num = getNthFib(n -1) + getNthFib(n - 2)
		cache[n] = fib_num
		return fib_num