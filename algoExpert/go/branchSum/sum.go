//https://www.algoexpert.io/questions/Branch%20Sums

package main

// This is the struct of the input root. Do not edit it.
type BinaryTree struct {
	Value int
	Left  *BinaryTree
	Right *BinaryTree
}

func BranchSums(root *BinaryTree) []int {
	var result []int
	helper(root, 0, result)
	return result
}

func helper(root *BinaryTree, count int, result []int) {
	if root == nil {
		return result
	}

	newCount := count + root.Value

	helper(root.Left, newCount, result)
	result = append(result, newCount)
	helper(root.Right, newCount, result)

}
