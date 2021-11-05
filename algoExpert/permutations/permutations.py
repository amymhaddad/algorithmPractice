# https://www.algoexpert.io/questions/Permutations

def getPermutations(arr):
    total_perms = []
    helper(arr, [], total_perms)
    return total_perms

def helper(arr, perm, total_perms):
    if arr == [] and len(perm) > 0:
        total_perms.append(perm)

    else:
        for i, _ in enumerate(arr):
            new_arr = arr[:i] + arr[i+1:]
            curr_perm = perm + [arr[i]]
            helper(new_arr, curr_perm, total_perms)

print(getPermutations([1, 2, 3]))
