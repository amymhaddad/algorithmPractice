package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

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
