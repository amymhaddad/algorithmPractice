package main

import "fmt"

//FirstNonRepeatingCharacter takes a string and returns the index of the first
//non-repeating character
func FirstNonRepeatingCharacter(str string) int {
	var letterCounts = map[rune]int{}

	for _, char := range str {
		if _, found := letterCounts[char]; found {
			letterCounts[char]++
		} else {
			letterCounts[char] = 1
		}
	}
	return -1
}

func main() {
	x := FirstNonRepeatingCharacter("abcdcaf")
	fmt.Println(x)
}
