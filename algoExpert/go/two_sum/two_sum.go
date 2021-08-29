package main

//TwoNumberSum takes a slice of numbers and checks of any two numbers in the
//slice sum to the given target
//Solution 1
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

//Solution 2
func TwoNumberSum(array []int, target int) []int {

	differences := make(map[int]bool)
	for i := range array {
		currValue := array[i]
		diff := target - currValue

		if _, found := differences[diff]; found {
			return []int{currValue, diff}
		}

		differences[currValue] = true
	}

	return []int{}
}
