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


func main() {
	x := int(math.Inf(0))
	y := 9
	fmt.Println(x > y)
	fmt.Println(x)
}
