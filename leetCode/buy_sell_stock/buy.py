"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
#prices = [7,1,5,3,6,4]
prices = [7, 5, 4, 2, 1]

def buy_stock(prices):

    buy = prices[0]
    max_profit = 0

    for i, price in enumerate(prices[1:], 1):
       # import pdb; pdb.set_trace()
        curr_profit = prices[i] - buy
        if curr_profit > max_profit:
            max_profit = curr_profit
            continue
        if prices[i] < buy and prices[i] != prices[-1]:
            buy = prices[i]
    return max_profit

print(buy_stock(prices))
