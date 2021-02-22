
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

# array = [5, 1, 22, 25, 6, -1, 8, 10]
 #sequence = [5, 1, 25, 22, 6, -1, 8, 10]

# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [5, 1, 22, 22, 25, 6, -1, 8, 10]

def validateSubsequenceuence(array, sequence):

    array_vals = {num: True for num in array }

    for num in sequence:
        if num not in array_vals:
            return False
        else:
            del array_vals[num]
    return True

#print(validateSubsequenceuence(array, sequence))

def validate(array, sequence):

    valid_arr = []
    for num in array:
        if num in sequence:
            valid_arr.append(num)
    return set(valid_arr) == set(sequence) 

print(validate(array, sequence))





