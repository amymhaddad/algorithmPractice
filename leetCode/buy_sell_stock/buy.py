"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


def buy_stock(prices):
    if len(prices) <= 1:
        return 0

    purchase_price = prices[0]
    max_profit = 0

    for _, curr_price in enumerate(prices[1:]):
        curr_profit = curr_price - purchase_price
        if curr_profit > max_profit:
            max_profit = curr_profit
            continue
        if curr_price < purchase_price:
            purchase_price = curr_price
    return max_profit
