class Solution(object):
    # Dynamic Programming with State Machine
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sold, held, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            # Temporary variable to store the previous sold state
            pre_sold = sold

            # Update the sold state: If we sell the stock today, we add today's price to held.
            sold = held + price

            # Update the held state: Either keep holding the stock or buy today.
            held = max(held, reset - price)

            # Update the reset state: Either continue in reset or come from the sold state.
            reset = max(reset, pre_sold)

        # The maximum profit will be either in the sold or reset state.
        return max(sold, reset)

prices1 = [1, 2, 3, 0, 2]
# Transactions = [buy, sell, cooldown, buy, sell].
# Max profit = (2 - 1) + (2 - 0) = 1 + 2 = 3
print(Solution().maxProfit(prices1))  # Expected Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

prices2 = [1]
# Only one price, so no transaction possible.
print(Solution().maxProfit(prices2))  # Expected Output: 0

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one
share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

3--------------------------------------------------------------------------------------------------#

Overview
First of all, we would like to mention that this is yet another problem from the series of
Best-Time-to-Buy-and-Sell-Stock problems, which we list as follows:

Best Time to Buy and Sell Stock
Best Time to Buy and Sell Stock II
Best Time to Buy and Sell Stock III
Best Time to Buy and Sell Stock IV
One could try to resolve them one by one, which certainly could help with this problem.

There have been quite some excellent posts in the Discussion forum. We would like to mention that the user
fun4LeetCode even developed a mathematical representation that is able to be generalized to each of the problems.

That being said, here we contribute some approaches, which hopefully could provide you different perspectives for the
problem.

As one might have seen the hint from the problem description, which says "dynamic programming" (i.e. DP), we could
tackle this problem mainly with the technique called dynamic programming.

Often the case, in order to come up with a dynamic programming solution, it would be beneficial to draw down some
mathematical formulas to model the problem.

As a reminder, the nature of dynamic programming is to break the original problem into several subproblems, and then
reuse the results of subproblems for the original problem.

Therefore, due to the nature of DP, the mathematical formulas that we should come up with would almost certainly
assume the form of recursion.

Before embarking on the next sections of this article, we kindly ask the audiences to keep an open mind, fasten your
seat belts and enjoy the ride with a heavy (yet healthy) dose of mathematical formulas.
"""