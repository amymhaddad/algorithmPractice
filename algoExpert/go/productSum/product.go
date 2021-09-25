package main

type SpecialArray []interface{}

func ProductSum(array SpecialArray) int {
	return helper(array, 1)
}

func helper(array SpecialArray, depth int) int {
	sum := 0

	for _, el := range array {
		if value, ok := el.(SpecialArray); ok {
			sum += helper(value, depth+1)
		} else if value, ok := el.(int); ok {
			sum += value
		}
	}

	return sum * depth
}
