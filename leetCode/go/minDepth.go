package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
import "sort"

func minDepth(root *TreeNode) int {
	depth := 1
	var totalDepths []int

	for root {
		if root.Left != nil {
			root = root.Left
			depth++
		} else {
			totalDepths = append(totalDepths, depth)
			depth = 1
			root = root.Right
		}
	}

	return sort.IntsAreSorted(totalDepths)
}
