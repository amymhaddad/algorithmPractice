package main

//LinkedList struct
type LinkedList struct {
	Value int
	Next  *LinkedList
}

func removeDuplicatesFromLinkedList(linkedList *LinkedList) *LinkedList {

	curr := linkedList

	for curr != nil {
		nextVal := curr.Next.Value
		currVal := curr.Value

		if nextVal == currVal {
			curr = curr.Next.Next
		} else {
			curr = curr.Next
		}
	}

	return linkedList

}
