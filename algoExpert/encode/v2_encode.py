"""
https://www.algoexpert.io/questions/Run-Length%20Encoding
"""

def encode(string):

    encoded_chars = []
    run_length = 1

    for i in range(1, len(string), 1):
        curr_char = string[i]
        prev_char = string[i-1]
        if run_length == 9 or curr_char != prev_char:
            encoded_chars.append(str(run_length)+prev_char)
            run_length = 0
        run_length += 1

    encoded_chars.append(str(run_length)+string[len(string)-1])
    return "".join(encoded_chars)

