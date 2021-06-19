"""
https://www.algoexpert.io/questions/Valid%20Starting%20City
"""



def validStartingCity(distances, fuel, mpg):

    indices = [i for i in range(len(distances))]
    #if want variable data to persist outside of loop, then keep var outside 
    while True:
        #If I need somethign local, then keep in the loop
        gas = 0
        
        curr_indices = rotate_index(indices, 1, indices[0])

        for i in range(len(curr_indices)):
            gas += fuel[i]         
            if  (gas * mpg) < distances[i]:
                import pdb; pdb.set_trace()
                gas = 0
                indices = curr_indices
                #indices = rotate_index(indices, 1, indices[0])
                break
            else:
              gas -= (distances[i] / mpg)
    return indices[0]

def rotate_index(indices, step, curr_index):
    indices_length = len(indices)
    new_indices = indices_length * [None]

    for i, value in enumerate(indices):
        index = (i + step ) % indices_length
        new_indices[i] = index
    return new_indices


distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

# distances = [10, 20, 10, 15, 5, 15, 25]
# fuel = [0, 2, 1, 0, 0, 1, 1]
# mpg = 20
print(validStartingCity(distances, fuel, mpg))
