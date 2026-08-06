from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * (k + 1) for _ in range(2)] for __ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for remain in range(1, k + 1):
                for holding in range(2):
                    ans = dp[i + 1][holding][remain]
                    if holding:
                        ans = max(ans, prices[i] + dp[i + 1][0][remain - 1])
                    else:
                        ans = max(ans, -prices[i] + dp[i + 1][1][remain])

                    dp[i][holding][remain] = ans

        return dp[0][0][k]

# Test cases
solution = Solution()

# Test case 1: k = 2, prices = [2, 4, 1]
k1 = 2
prices1 = [2, 4, 1]
# The best option is to buy at price 2 and sell at price 4, so the output should be 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
print(solution.maxProfit(k1, prices1))  # Output: 2

# Test case 2: k = 2, prices = [3, 2, 6, 5, 0, 3]
k2 = 2
prices2 = [3, 2, 6, 5, 0, 3]
# The best option is to buy at price 2 and sell at price 6, then buy at price 0 and sell at price 3, total profit is 7
print(solution.maxProfit(k2, prices2))  # Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0)
# and sell on day 6 (price = 3), profit = 3-0 = 3.