"""
Write a function is_prime that takes a single argument n and returns True if n is a prime number and False otherwise. Assume n > 1.
"""

def is_prime(num):
    if num <= 2:
        return True

    def helper(num, factor):
        factors = []
        while factor < num:
            if num % factor == 0:
                factors.append(factor)
            factor += 1
        return len(factors) == 0
    return helper(num, 2)

#print(is_prime(521))

def v2_is_prime(num):
    if num <= 2:
        return True

    def helper(factor):
        if num % factor == 0:
            return False
        elif factor >= num:
            return False
        else:
            return helper(num, factor + 1)
    helper(2)
print(is_prime(2))
