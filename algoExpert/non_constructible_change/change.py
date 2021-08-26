
def change(coins):
    coins.sort()

    change_options = []
    total_so_far = 0
    for i in range(len(coins)):
        if coins[i] not in change_options:
            change_options.append(coins[i])

        if i == len(coins) + 1:
            break 
        
        next_val = total_so_far + coins[i]
        if next_val not in change_options:
            change_options.append(next_val)
        total_so_far += coins[i]
    
    change_options.sort()
    for i in range(len(change_options)):
        if i == len(change_options) - 1:
            return change_options[-1] + 1
       
        elif change_options[i+1] - change_options[i] > 1:
            max_change_num = change_options[i+1]
            break 

        else:
            continue
    print(change_options)
    #NOW iterate through change_options and get the difference
    #IF the diff is > 1, check if the diff is alrady in change_options
    #If not, return the diff at that point

coins = [5, 7, 1, 1, 2, 3, 22]
print(change(coins))
