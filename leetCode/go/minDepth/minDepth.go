package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
//Solution 1
func minDepth(root *TreeNode) int {

	depth := 0

	if root == nil {
		return depth
	}

	level := []*TreeNode{root}

	for len(level) != 0 {

		nextLevel := []*TreeNode{}
		depth++

		for _, node := range level {

			if node.Left == nil && node.Right == nil {
				return depth
			}

			if node.Left != nil {
				nextLevel = append(nextLevel, node.Left)
			}

			if node.Right != nil {
				nextLevel = append(nextLevel, node.Right)
			}

		}

		level = nextLevel
	}

	return depth

}

//Solution 2
func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return bfs([]*TreeNode{root})
}

func bfs(nodes []*TreeNode) int {

	nextLevel := []*TreeNode{}

	for _, node := range nodes {

		if node == nil {
			continue
		}

		if node.Left == nil && node.Right == nil {
			return 1
		}

		nextLevel = append(nextLevel, node.Left)
		nextLevel = append(nextLevel, node.Right)
	}

	return 1 + bfs(nextLevel)

}
