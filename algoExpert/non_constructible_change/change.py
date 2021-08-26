
def change(coins):
    coins.sort()

    change_options = []

    for i, num in enumerate(coins):
        if num not in change_options:
            change_options.append(num)

        if len(coins) -1 == i:
            break
        next_sum = coins[i]+coins[i+1]

        if next_sum not in change_options:
            change_options.append(next_sum)

    change_options.sort()
    return change_options

coins = [1, 2, 4, 9]
print(change(coins))
