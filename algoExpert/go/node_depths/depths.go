// https://www.algoexpert.io/questions/Node%20Depths

package main

type BinaryTree struct {
	Value       int
	Left, Right *BinaryTree
}

//Sol: 1
func NodeDepths_1(root *BinaryTree) int {
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

//Sol: 2
func NodeDepths_2(root *BinaryTree) int {
	return calcDepth([]*BinaryTree{root}, 0)
}

func calcDepth(nodes *BinaryTree, levelDepth int) int {
	if nodes == nil {
		return 0
	}
	return levelDepth + calcDepth(nodes.Left, levelDepth+1) + calcDepth(nodes.Right, levelDepth+1)
}
