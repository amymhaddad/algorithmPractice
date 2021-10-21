// https://www.algoexpert.io/questions/Node%20Depths

package main

type BinaryTree struct {
	Value       int
	Left, Right *BinaryTree
}

func NodeDepths(root *BinaryTree) int {
	var totalDepth int

	currLevel := []*BinaryTree{root}

	var levelDepth int

	for len(currLevel) > 0 {
		levelDepth++
		nextLevel := []*BinaryTree{}

		for _, node := range currLevel {
			if node.Left != nil {
				nextLevel = append(nextLevel, node.Left)
			}
			if node.Right != nil {
				nextLevel = append(nextLevel, node.Right)
			}
		}
		totalDepth += levelDepth * len(nextLevel)
		currLevel = nextLevel
	}
	return totalDepth
}
