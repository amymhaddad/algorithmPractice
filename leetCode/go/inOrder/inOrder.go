package main

//TreeNode is a binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

//Recursive solution
func inorderTraversal(root *TreeNode) []int {
	var nodes []int
	return getNodes(root, &nodes)
}

func getNodes(root *TreeNode, nodes *[]int) []int {

	if root != nil {
		getNodes(root.Left, nodes)
		*nodes = append(*nodes, root.Val)
		getNodes(root.Right, nodes)
	}
	return *nodes
}

//Iterative solution
func inorderTraversal(root *TreeNode) []int {
	var s []*TreeNode
	var results []int

	for {
		if root != nil {
			s = append(s, root)
			root = root.Left
		} else {
			if len(s) == 0 {
				break
			}

			root, s = s[len(s)-1], s[:len(s)-1]
			results = append(results, root.Val)
			root = root.Right

		}
	}
	return results

}
