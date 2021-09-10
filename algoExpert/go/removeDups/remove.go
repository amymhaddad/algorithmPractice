package main

//LinkedList struct
type LinkedList struct {
	Value int
	Next  *LinkedList
}

//Solution 1
func RemoveDuplicatesFromLinkedList(linkedList *LinkedList) *LinkedList {
	curr := linkedList

	for curr != nil && curr.Next != nil {
		nextVal := curr.Next.Value
		currVal := curr.Value

		if currVal == nextVal {
			curr.Next = curr.Next.Next

		} else {
			curr = curr.Next
		}
	}

	return linkedList

}

//Solution 2
func RemoveDuplicatesFromLinkedList(linkedList *LinkedList) *LinkedList {
	curr := linkedList

	for curr != nil && curr.Next != nil {
		nextVal := curr.Next
		for nextVal != nil && nextVal.Value == curr.Value {
			nextVal = nextVal.Next
		}
		curr.Next = nextVal
		curr = curr.Next
	}
	return linkedList
}
