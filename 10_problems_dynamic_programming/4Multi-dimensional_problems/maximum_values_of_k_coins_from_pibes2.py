from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for remain in range(1, k + 1):
                dp[i][remain] = dp[i + 1][remain] # skip this pile
                curr = 0
                for j in range(min(remain, len(piles[i]))):
                    curr += piles[i][j]
                    dp[i][remain] = max(dp[i][remain], curr + dp[i + 1][remain - j - 1])

        return dp[0][k]

# Test cases
solution = Solution()

# Test case 1: piles = [[1, 100, 3], [7, 8, 9]], k = 2
piles1 = [[1, 100, 3], [7, 8, 9]]
k1 = 2
# The best option is to take 1 from the first pile and 100 from the first pile, resulting in 1 + 100 = 101
# Explanation:
# The above diagram shows the different ways we can choose k coins.
# The maximum total we can obtain is 101.
print(solution.maxValueOfCoins(piles1, k1))  # Output: 101

# Test case 2: piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], k = 7
piles2 = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]]
k2 = 7
# The best option is to take all coins from the last pile, resulting in 700 + 1 + 1 + 1 + 1 + 1 + 1 = 706
# Explanation:
# The maximum total can be obtained if we choose all coins from the last pile
print(solution.maxValueOfCoins(piles2, k2))  # Output: 706
