from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = -prices[0], 0

        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)

        return free

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

#----------------------------------------------------------------------------------------------------#

Overview
As shown in the picture below, if we do the following operations:

Buy the stock on day 0.
Sell the stock on day 3.
Buy the stock on day 4.
Sell the stock on day 5.
Considering the two transaction fees, we can make a total profit of 8.

However, we have to be aware of some restrictions:
We can hold at most 1 stock at a time, we can't buy this stock twice.
We can't sell the stock before we hold it.

Approach 2: Space-Optimized Dynamic Programming
Intuition
In the previous solution, we created two arrays of length n to record the maximum profits up to each day.

However, if we look at the state transition equation:

hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)
We can see that the maximum profit up to day i (hold[i] or free[i]) only depends on the maximum profit up to day i - 1
(hold[i - 1] and free[i - 1]), and we don't need to keep track of the profits from earlier days.

Therefore, we can use only two variables hold and free to represent the maximum profits in the two states on the
current day. When we move to the next day (day i), we can simply update these two variables.

hold = max(hold, free - prices[i])
free = max(free, hold + prices[i] - fee)
To avoid modifying hold before updating free, we can do the following:

tmp = hold
hold = max(hold, free - prices[i])
free = max(free, tmp + prices[i] - fee)

Algorithm
1. Set free = 0 and hold = -prices[0] as the maximum profit for two status on day 0.
2. Iterate from day 1 to day n - 1, on each day i:
    Set tmp = hold so that we record the maximum profit for holding a stock on day i - 1.
    Update hold to the larger of hold and free - prices[i].
    Update free to the larger of free and tmp + prices[i] - fee.
3. Return free once the iteration ends.
"""