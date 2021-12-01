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
		if (len(letters) == 0) || (len(letters) <= 9 && currLetter == letters[len(letters)-1]) {
			letters = append(letters, currLetter)
			count++
			continue
		}

		if currLetter != letters[len(letters)-1] {
			//countAsString := string(count)
			encode = append(encode, strconv.Itoa(count)+letters[len(letters)-1])
			if count > 0 {
				count = 0
				letters = []string{currLetter}
			}
			letters = append(letters, currLetter)
			count++
			fmt.Println("c", encode)
			continue
		}

		// 	fmt.Println(count, letters)
		// } else if (len(letters) == 0) || (len(letters) < 10 && currLetter == letters[len(letters)-1]) {
		// 	letters = append(letters, currLetter)
		// 	count++
		// }

		// if len(letters) >= 9 && currLetter == letters[len(letters)-1] {
		// 	encode = append(encode, string(count)+letters[len(letters)-1])
		// 	letters = []string{currLetter}
		// 	count = 1
		//}
		// if len(letters) > 1 && currLetter != letters[len(letters)-1] {
		// 	encode = append(encode, string(count)+letters[len(letters)-1])
		// 	letters = []string{currLetter}
		// 	count++

		// 	fmt.Println(count, letters)
		// } else if (len(letters) == 0) || (len(letters) < 10 && currLetter == letters[len(letters)-1]) {
		// 	letters = append(letters, currLetter)
		// 	count++
		// }

	}
	encode = append(encode, string(count)+letters[len(letters)-1])
	return strings.Join(encode, "")

}

func main() {
	x := RunLengthEncoding("1AAB")
	fmt.Println(x)
}
