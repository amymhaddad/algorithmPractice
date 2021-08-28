package main

//FirstNonRepeatingCharacter takes a string and returns the index of the first
//non-repeating character
//Solution 1
func FirstNonRepeatingCharacter(str string) int {
	var letterCounts = map[rune]int{}

	for _, char := range str {
		if _, found := letterCounts[char]; found {
			letterCounts[char]++
		} else {
			letterCounts[char] = 1
		}
	}

	for i, char := range str {
		if letterCounts[char] == 1 {
			return i
		}
	}
	return -1
}

//Solution 2
func FirstNonRepeatingCharacter(str string) int {
	for index1 := range str {
		foundDup := false
		for index2 := range str {
			if str[index1] == str[index2] && index1 != index2 {
				foundDup = true
			}
		}

		if !foundDup {
			return index1
		}

	}
	return -1

}
