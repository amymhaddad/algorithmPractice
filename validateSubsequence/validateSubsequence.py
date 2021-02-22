
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 25, 22, 6, -1, 8, 10]

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

    array_vals = {num: i for i, num in enumerate(array)}
    next_index = 1

    for i in range(len(sequence)):
        #import pdb; pdb.set_trace()
        if next_index + i >= len(sequence):
            break

        next_val = sequence[next_index + i]
        current_val = sequence[i]

        if current_val not in array_vals:
            return False
        
        if current_val in array_vals and next_val in array_vals:
            if array_vals[next_val] < array_vals[current_val]:
                return False

        else:
            del array_vals[current_val]
    return True

print(validate(array, sequence))





