package main

import (
	"math"
)

//BST is a tree
type BST struct {
	Value int
	Left  *BST
	Right *BST
}

//ValidateBst determines if a given tree is a valid BST
func (tree *BST) ValidateBst() bool {
	max := int(math.MaxInt64)
	min := int(math.MinInt64)
	return validate(tree, min, max)
}

func validate(tree *BST, min, max int) bool {

	if tree == nil {
		return true
	}

	if tree.Value < min || tree.Value >= max {
		return false
	}
	return Validate(tree.Left, min, tree.Value) && Validate(tree.Right, tree.Value, max)
}
