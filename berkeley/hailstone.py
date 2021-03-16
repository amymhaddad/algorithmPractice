"""
Recall the hailstone function from Homework 1. First, pick a positive integer n as the start. If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1. Write a recursive version of hailstone that prints out the values of the sequence and returns the number of steps.
"""

def hailstone(num):
    print(num)
    if num == 1:
        return 1

    else:
        if num % 2 == 0:
            return 1 + hailstone(num // 2)
        else:
            return 1 + hailstone(num * 3 + 1)

print(hailstone(10))
