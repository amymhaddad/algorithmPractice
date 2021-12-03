//https://www.algoexpert.io/questions/Run-Length%20Encoding

package main

import (
	"strconv"
	"strings"
)

//Sol 1
func RunLengthEncoding(str string) string {
	currRunLength := 1
	var encodedLetters []byte

	for i := 1; i < len(str); i++ {
		currChar := str[i]
		prevChar := str[i-1]

		if currRunLength == 9 || currChar != prevChar {
			encodedLetters = append(encodedLetters, strconv.Itoa(currRunLength)[0])
			encodedLetters = append(encodedLetters, prevChar)
			currRunLength = 0
		}

		currRunLength++
	}
	encodedLetters = append(encodedLetters, strconv.Itoa(currRunLength)[0])
	encodedLetters = append(encodedLetters, str[len(str)-1])
	return string(encodedLetters)
}

//Sol 2
func RunLengthEncoding(str string) string {
	var count int
	var letters []string
	var encode []string
	var currLetter string
	var prevLetter string
	for _, ch := range str {

		currLetter = string(ch)

		if len(letters) == 9 || currLetter != prevLetter && len(letters) > 0 {
			encode = append(encode, strconv.Itoa(count)+prevLetter)
			letters = []string{currLetter}
			prevLetter = currLetter
			count = 1
			continue
		}

		if (len(letters) == 0) || len(letters) < 9 && currLetter == prevLetter {
			letters = append(letters, currLetter)
			prevLetter = currLetter
			count++
			continue
		}

	}

	encode = append(encode, strconv.Itoa(count)+currLetter)
	return strings.Join(encode, "")
}

//Sol 3
func RunLengthEncoding(str string) string {
	var count int
	var letters []string
	var encode []string
	var currLetter string
	var prevLetter string
	for _, ch := range str {

		currLetter = string(ch)

		if len(letters) == 9 && currLetter == prevLetter || currLetter != prevLetter && len(letters) > 0 {
			encode = append(encode, strconv.Itoa(count)+prevLetter)
			letters = []string{currLetter}
			prevLetter = currLetter
			count = 1
		} else {
			letters = append(letters, currLetter)
			prevLetter = currLetter
			count++
		}

	}

	encode = append(encode, strconv.Itoa(count)+currLetter)
	return strings.Join(encode, "")

}
