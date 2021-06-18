"""
https://www.algoexpert.io/questions/Valid%20Starting%20City
"""







def rotate_index(indices, step, curr_index):
    indices_length = len(indices)
    new_indices = indices_length * [None]

    for i, value in enumerate(indices):
        index = (i + step ) % indices_length
        import pdb; pdb.set_trace()
        new_indices[i] = index
    return new_indices

distances = [5, 25, 15, 10, 15]
step = 1
#print(rotate_index(distances, step, curr_index))
