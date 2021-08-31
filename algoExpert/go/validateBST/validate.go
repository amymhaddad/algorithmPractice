package main

import (
	"fmt"
	"math"
)

// func Inf(sign int) float64

type BST struct {
	Value int
	Left  *BST
	Right *BST
}

func (tree *BST) ValidateBst() bool {
	max := int(math.MaxInt64)
	min := int(math.MinInt64)

	return Validate(tree, max, min)
}

func Validate(tree *BST, max int, min int) bool {
	if tree == nil {
		return true
	}
	//Valid bst val: val >= min min and val < max val
	//SO to break these conditions, use the syntax below
	if tree.Value < min || tree.Value >= max {
		return false
	}
	return Validate(tree.Left, min, tree.Value) && Validate(tree.Right, tree.Value, max)
}

func main() {
	x := int(math.Inf(0))
	y := 9
	fmt.Println(x > y)
	fmt.Println(x)
}
