def change(coins):
    coins.sort()
    change = 0

    for i, val in enumerate(coins):
        if val > change + 1:
            return change + 1

        change += val
    return change + 1
