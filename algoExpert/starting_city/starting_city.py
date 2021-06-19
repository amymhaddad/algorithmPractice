"""
https://www.algoexpert.io/questions/Valid%20Starting%20City
"""



def validStartingCity(distances, fuel, mpg):
    
    while True:
        gas = 0
        indices = [i for i in range(len(distances))]
        available_miles = 0

        for i, index in enumerate(indices):
            gas += fuel[i]
            available_miles += (gas * mpg)
            if available_miles < distances[i]:
                indices = rotate_index(indices, 1, indices[0])
                gas = 0
                break
        return i

def rotate_index(indices, step, curr_index):
    indices_length = len(indices)
    new_indices = indices_length * [None]

    for i, value in enumerate(indices):
        index = (i + step ) % indices_length
        new_indices[i] = index
    return new_indices

distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
step = 1
#print(rotate_index(distances, step, curr_index))

print(validStartingCity(distances, fuel, 10))
