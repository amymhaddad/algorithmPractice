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

	for _, ch := range str {
		if !unicode.IsLetter(ch) {
			continue

		}

		currLetter = strings.ToUpper(string(ch))

		//If I've found the same letter but the length of letters is >= 9, then I need to create a new slice
		if len(letters) >= 9 && currLetter == letters[len(letters)-1] {
			encode = append(encode, strconv.Itoa(count)+letters[len(letters)-1])
			letters = []string{currLetter}
			count = 1
			continue
		}

		//IF I'm at the start of the string OR I have a repeating letter and the length of the string is less than or == to 9
		if (len(letters) == 0) || len(letters) <= 9 && currLetter == letters[len(letters)-1] {
			letters = append(letters, currLetter)
			count++
			continue
		}

		//I've found a NEW letter
		if currLetter != letters[len(letters)-1] {
			encode = append(encode, strconv.Itoa(count)+letters[len(letters)-1])
			if count > 0 {
				count = 0
				letters = []string{currLetter}
			}
			letters = append(letters, currLetter)
			count++
			continue
		}

	}
	encode = append(encode, strconv.Itoa(count)+letters[len(letters)-1])
	return strings.Join(encode, "")

}

func main() {
	x := RunLengthEncoding("AAAAAAAAAAAAABBCCCCDD")
	fmt.Println(x)
	//10A3A2B4C2D
}
