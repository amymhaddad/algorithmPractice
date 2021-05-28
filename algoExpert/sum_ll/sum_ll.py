"""
https://www.algoexpert.io/questions/Sum%20of%20Linked%20Lists
"""

class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



def sumOfLinkedLists(linkedListOne, linkedListTwo):
    linked1_ints = get_digits(linkedListOne)
    linked2_ints = get_digits(linkedListTwo)
    sum_of_lists = linked1_ints + linked2_ints

    num = reverse_digits([d for d in str(sum_of_lists)])
    return store_digits(num)

def store_digits(num):

    new_list = LinkedList(num % 10)
    num //= 10

    while num > 0:

        last_digit = num % 10 
        new_list.value, new_list.next = last_digit, LinkedList(new_list.value, new_list.next)
        num //= 10
    return new_list


def get_digits(linked_list):

    total_numbers = []

    while linked_list is not None:
        number = linked_list.value
        total_numbers.append(str(number))
        linked_list = linked_list.next
    return reverse_digits(total_numbers)

def reverse_digits(digits):
    i = 0
    j = len(digits) -1

    while i < j:
        digits[i], digits[j] = digits[j], digits[i]
        i += 1
        j -= 1
    return int("".join(digits))


