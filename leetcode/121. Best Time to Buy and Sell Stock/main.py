# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description

def maxProfit(prices: list[int]) -> int:
    profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] - min_price > profit:
            profit = prices[i] - min_price
        elif prices[i] < min_price:
            min_price = prices[i]

    return profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))