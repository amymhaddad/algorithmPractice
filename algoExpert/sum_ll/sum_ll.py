"""
https://www.algoexpert.io/questions/Sum%20of%20Linked%20Lists
"""

class LinkedList:   
    def __init__(self, value):
        self.value = value
        self.next = None

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    linked1_ints = get_digits(linkedListOne)
    linked2_ints = get_digits(linkedListTwo)
    sum_of_lists = linked1_ints + linked2_ints

    new_list = LinkedList(sum_of_lists % 10)
    sum_of_lists = sum_of_lists // 10

    while sum_of_lists is not None:
        last_digit = sum_of_lists % 10 
        new_list.value, new_list.next = last_digit, new_list(new_list.first, ())
        sum_of_lists = sum_of_lists // 10

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


nums = 123

while nums > 0:
    print("here")

    nums = nums // 10
