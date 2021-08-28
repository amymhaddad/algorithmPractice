package main

import "fmt"

//TwoNumberSum takes a slice of numbers and checks of any two numbers in the
//slice sum to the given target
func TwoNumberSum(array []int, target int) []int {
	for i := range array {
		for j := range array {
			currVal := array[i] + array[j]
			if currVal == target && i != j {
				return []int{array[i], array[j]}
			}
		}
	}
	return []int{}
}

func main() {
	x := []int{3, 5, -4, 8, 11, 1, -1, 6}
	y := 10
	z := TwoNumberSum(x, y)
	fmt.Println(z)

}
