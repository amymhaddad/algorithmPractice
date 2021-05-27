"""
https://www.algoexpert.io/questions/Sum%20of%20Linked%20Lists
"""

class Link:
    def __init__(self, value):
        self.value = value
        self.next = None
#x = Link(1, Link(5))
#y = Link(1, Link(4))

def sumOfLinkedLists(linkedListOne, linkedListTwo):

    linked1_ints = get_digits(linkedListOne)

    print(linked1_ints)


def get_digits(linked_list):

    digits = []

    while linked_list is not None:
        linked_list = linked_list.value
        digits.append(linked_list.value)
        linked_list = linked_list.next
    return digits

print(sumOfLinkedLists(x, y))
