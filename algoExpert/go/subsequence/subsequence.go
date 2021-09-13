package main

//Solution 1
func IsValidSubsequence(array []int, sequence []int) bool {
	arrIndex := 0
	seqIndex := 0

	var validNums int
	for seqIndex <= len(sequence)-1 && arrIndex <= len(array)-1 {
		if sequence[seqIndex] == array[arrIndex] {
			validNums++
			arrIndex++
			seqIndex++
		} else if seqIndex <= arrIndex {
			arrIndex++
		} else {
			break
		}

	}
	return validNums == len(sequence)
}

//Solution 2
func IsValidSubsequence(array []int, sequence []int) bool {
	var seqIndex int
	var validNums int
	for i := 0; i <= len(array)-1; i++ {
		if array[i] == sequence[seqIndex] {
			validNums++
			seqIndex++
			if seqIndex >= len(sequence) {
				break
			}
		}
	}

	return validNums == len(sequence)
}
