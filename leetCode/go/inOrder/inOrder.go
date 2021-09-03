package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// //Recursive solution
// func inorderTraversal(root *TreeNode) []int {
// 	var nodes []int
// 	return getNodes(root, &nodes)
// }

// func getNodes(root *TreeNode, nodes *[]int) []int {

// 	if root != nil {
// 		getNodes(root.Left, nodes)
// 		*nodes = append(*nodes, root.Val)
// 		getNodes(root.Right, nodes)
// 	}
// 	return *nodes
// }

//Iterative Solution
func inorderTraversal(root *TreeNode) []int {
	//s needs to be slice of pointers to TreeNodes --> *TreeNode
	//Appending to a slcie of pointers to TreeNodes
	var s []int
	var results []int

	for len(s) != 0 {
		if root.Left != nil {
			root = root.Left
			s = append(s, root)
		}

		results = append(results, root.Val)

		if root.Right != nil {
			root = root.Right
			s = append(s, root)
		}

	}
	return results

}
