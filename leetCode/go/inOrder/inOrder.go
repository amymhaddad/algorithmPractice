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
	var s []*TreeNode
	var results []int
	var val int 

	for {
		if root != nil {
			s = append(s, root)
			root = root.Left
		} else {
			if len(s) == 0 {
				break
			}
		//	fmt.Println(s)
			val, s = s[len(s)-1], s[:len(s)-1]
			results = append(results, val)
			root = root.Right
		}

	}

	return results

}
