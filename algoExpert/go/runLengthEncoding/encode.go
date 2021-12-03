//https://www.algoexpert.io/questions/Run-Length%20Encoding

package main

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

func RunLengthEncoding(str string) string {
	var count int
	var letters []string
	var encode []string
	var currLetter string
	var prevLetter string
	for _, ch := range str {
		if !unicode.IsLetter(ch) {
			continue

		}

		currLetter = string(ch)

		if len(letters) == 9 && currLetter == prevLetter || currLetter != prevLetter && len(letters) > 0 {
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

		// //IF length of letters is 9 and current letter equals prev letter, start a new list and count
		// if len(letters) == 9 && currLetter == prevLetter || currLetter != prevLetter {
		// 	encode = append(encode, strconv.Itoa(count)+currLetter)
		// 	letters = []string{currLetter}
		// 	prevLetter = currLetter
		// 	count = 1
		// 	continue
		// }

	}

	encode = append(encode, strconv.Itoa(count)+currLetter)
	return strings.Join(encode, "")

}

func main() {
	x := RunLengthEncoding("AAB")
	fmt.Println(x)
	//10A3A2B4C2D
}
