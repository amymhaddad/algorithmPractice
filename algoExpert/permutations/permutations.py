# https://www.algoexpert.io/questions/Permutations

# def getPerm(arr):
#     permutations = []
#     helper(arr, [], permutations)
#     return permutations
#
# def helper(arr, curr_perm, total_perms):
#     if not len(arr) and len(curr_perm):
#         total_perms.append(curr_perm)
#
#     else:
#         for i in range(len(arr)):
#             new_arr = arr[:i] + arr[i+1:]
#             new_perm = curr_perm + [arr[i]]
#             helper(new_arr, new_perm, total_perms)
#
#print(getPerm([1, 2, 3]))

def v2_getPerm(arr):
    perms = []
    helper(0, arr, perms)
    return perms

def helper(i, arr, perms):
    if i == len(arr) - 1:
        perms.append(arr[:])

    else:
        for next_index in range(i, len(arr)):
            import pdb; pdb.set_trace()
            swap(arr, i, next_index)
            helper(i+1, arr, perms)
            swap(arr, i, next_index)

def swap(arr, i, next_index):
    arr[i], arr[next_index] = arr[next_index], arr[i]

print(v2_getPerm([1, 2, 3]))
