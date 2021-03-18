"""
Write a function is_prime that takes a single argument n and returns True if n is a prime number and False otherwise. Assume n > 1.
"""


def is_prime(num):
    def helper(possible_factor):
        if num == possible_factor:
            return True
        elif num % possible_factor == 0:
            return False
        return helper(possible_factor + 1)

    return helper(2)


print(is_prime(521))
