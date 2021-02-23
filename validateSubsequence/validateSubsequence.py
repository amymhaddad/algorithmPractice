array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
# # 
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [5, 1, 25, 22, 6, -1, 8, 10]

#array = [1, 1, 1, 1, 1]
#sequence = [1, 1, 1]


def validateSubsequenceuence(array, sequence):


    for num in array:
        if num not in sequence:
            array.pop(num)
    return array

print(validateSubsequenceuence(array, sequence))


# def validate(array, sequence):

#     seq_nums_indexes = {}
#     seq_index = 0

#     for num in array:
#         if seq_index >= len(sequence):
#             break
#         if num in sequence:
#             seq_nums_indexes[seq_index] = num
#             seq_index += 1
    
#     matched_seq = {i: num   for i, num in enumerate(sequence)}
#     return seq_nums_indexes == matched_seq

# print(validate(array, sequence))

