class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L = len(prices)
        # padding the array with additional zero to simply the logic
        MP = [0] * (L + 2)

        for i in range(L-1, -1, -1):
            C1 = 0
            # Case 1). buy and sell the stock
            for sell in range(i + 1, L):
                profit = (prices[sell] - prices[i]) + MP[sell + 2]
                C1 = max(profit, C1)

            # Case 2). do no transaction with the stock p[i]
            C2 = MP[i + 1]

            # sum up two cases
            MP[i] = max(C1, C2)

        return MP[0]

prices1 = [1, 2, 3, 0, 2]
# Transactions = [buy, sell, cooldown, buy, sell].
# Max profit = (2 - 1) + (2 - 0) = 1 + 2 = 3
print(Solution().maxProfit(prices1))  # Expected Output: 3

prices2 = [1]
# Only one price, so no transaction possible.
print(Solution().maxProfit(prices2))  # Expected Output: 0