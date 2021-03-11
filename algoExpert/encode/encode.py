"""
https://www.algoexpert.io/questions/Run-Length%20Encoding
"""


def parse_given_string(string):
    parsed_string = []

    p1, p2 = 0, 1

    while p2 < len(string):
        start_char = string[p1]
        next_char = string[p2]
        length_of_nine = p2 - p1 == 9

        if length_of_nine:
            parsed_string.extend(["9", start_char])
            p1, p2 = p2, p2 + 1

        elif start_char == next_char:
            p2 += 1

        else:
            char_count = p2 - p1
            parsed_string.extend([str(char_count), start_char])
            p1, p2 = p2, p2 + 1
    if p1 < p2:
        parsed_string.extend([str(p2 - p1), string[p1]])
    return "".join(parsed_string)
