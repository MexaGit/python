from typing import List

class Solution:
    # Dynamic Programming
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = [0] * n, [0] * n

        # In order to hold a stock on day 0, we have no other choice but to buy it for prices[0].
        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)

        return free[-1]

# Test Case 1
prices1 = [1, 3, 2, 8, 4, 9]
fee1 = 2
# Buying on day 0 (price = 1), selling on day 3 (price = 8), transaction fee = 2
# Then, buying on day 4 (price = 4), selling on day 5 (price = 9), transaction fee = 2
# Max Profit = (8 - 1 - 2) + (9 - 4 - 2) = 5 + 3 = 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
print(Solution().maxProfit(prices1, fee1))  # Output: 8

# Test Case 2
prices2 = [1, 3, 7, 5, 10, 3]
fee2 = 3
# Buying on day 0 (price = 1), selling on day 2 (price = 7), transaction fee = 3
# Then, buying on day 3 (price = 5), selling on day 4 (price = 10), transaction fee = 3
# Max Profit = (7 - 1 - 3) + (10 - 5 - 3) = 3 + 2 = 5
print(Solution().maxProfit(prices2, fee2))  # Output: 5

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee
representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the
transaction fee for each transaction.

Note:
You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
"""