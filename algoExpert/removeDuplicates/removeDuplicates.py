class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Sol 1
def removeDuplicatesFromLinkedList(linkedList):
    current_node = linkedList
    while current_node.next is not None:
        curr_value = current_node.value
        next_node_value = current_node.next.value
        if curr_value == next_node_value:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return linkedList


# Sol 2
def removeDuplicatesFromLinkedList(linkedList):
    current_node = linkedList

    while current_node is not None:
        next_unique = current_node.next

        while next_unique is not None and next_unique.value == current_node.value:
            next_unique = next_unique.next

        current_node.next = next_unique
        current_node = next_unique
    return linkedList
