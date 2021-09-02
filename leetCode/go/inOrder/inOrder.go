package main

func inorderTraversal(root *TreeNode) []int {
	var nodes []int
	if root != nil {
		inorderTraversal(root.Left)
		nodes = append(nodes, root.val)
		inorderTraversal(root.Right)
	}
	return nodes
}
