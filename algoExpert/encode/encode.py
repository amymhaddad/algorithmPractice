"""
https://www.algoexpert.io/questions/Run-Length%20Encoding
"""


#string = "1  222 333    444  555"
#string = "AAAAAAAAAAAAABBCCCCDD"
string = "ABB"

 
def parse_given_string(string):
    parsed_string = []

    p1, p2 = 0, 1

    while p2 < len(string):
        start_char = string[p1]
        next_char = string[p2]

        if start_char == next_char:
            p2 += 1

        else:
            char_count =  p2 - p1 
            parsed_string.extend([char_count, start_char])
            p1 = p2
            p2 = p1 + 1
    if p1 < p2:
        #import pdb; pdb.set_trace()
        parsed_string.extend([(p2-p1), string[p1]])
    return parsed_string 
print(parse_given_string(string))

