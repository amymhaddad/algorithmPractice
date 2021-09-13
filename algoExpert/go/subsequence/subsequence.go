package main

import "fmt"

func isValidSubsequence(array []int, sequence []int) bool {

	numsWithIndexes := make(map[int]int)

	for i := 0; i <= array; i++ {
		numsWithIndexes[array[i]] = i
	}

	var validNums int

	for i := 0; i <= sequence; i++ {
		if index, found := numsWithIndexes[sequence[i]]; found && i <= index {
			validNums++
		}
	}
	return validNums == len(sequence)
}

func main() {
	fmt.Println("vim-go")
}
