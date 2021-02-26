"""
Determine if a string is a palindrome
"""

#Sol 1: recursion 
#O(n)
string = "abba"
def isPalindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and isPalindrome(string[1:-1])

# def test_string_is_palindrome_odd_number_of_letters():
#     string = "abcdcba"
#     assert isPalindrome(string) == True


# def test_string_is_palindrome_even_number_of_letters():
#     string = "abba"
#     assert isPalindrome(string) == True


#Sol 2: pointers
#O(n) | O(1)
def isPalindrome_v2(string):
    p1 = 0
    p2 = len(string) -1 

    while p1 < p2:
        if string[p1] == string[p2]:
            p1 += 1
            p2 -=1 

        else:
            return False
    return True


def main():
    return isPalindrome(string)

if __name__ == "__main__":
    main()


#Questions:
#Running tests w/in file
#Runnign __name__
#INstalling pytest and running tests from external file