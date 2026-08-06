from functools import cache
from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(i, remain):
            # Base case: if we've processed all piles or have no coins left to take
            if i == len(piles) or remain == 0:
                return 0

            # Option 1: Skip the current pile and move to the next
            ans = dp(i + 1, remain)
            curr = 0

            # Option 2: Take coins from the current pile
            # We can take at most `remain` coins or the number of coins in the current pile
            for j in range(min(remain, len(piles[i]))):
                curr += piles[i][j]  # Add the j-th coin from the current pile
                # Calculate the maximum value by taking `j + 1` coins from the current pile
                ans = max(ans, curr + dp(i + 1, remain - j - 1))

            return ans

        return dp(0, k)

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

"""
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/description/
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom,
and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k
coins optimally.

#-------------------------------------------------------------------------------------------------#

Solution
Note. For this problem, we assume that you already know the fundamentals of dynamic programming and are figuring out
how to apply it to a wide range of problems, such as this one. If you are not yet at this stage, we recommend checking
out our relevant Explore Card content on dynamic programming before coming back to this article.

Approach 1: Bottom-up Dynamic Programming
Intuition
Let dp[i][coins] be the maximum total value of coins you can have in your wallet if you choose at most coins coins from
the leftmost i piles optimally.

For example, dp[4][7] is the maximum total value when one takes at most seven coins from the leftmost four piles. Since
all coins have positive denomination, if the leftmost four piles contain at least seven coins in total, it is optimal
to take exactly seven coins. In other words, it is never optimal to take less coins than we are allowed.

The base case of this DP is i = 0 – no piles are considered, so one didn't take any coins from any piles. Since the
total value of 0 coins is zero, dp[0][coins] = 0.

Now consider i > 0 when one takes at most coins coins from the leftmost i piles (numbered from 0 to i - 1). We want to
know the optimal answer for this DP state.

Since we use dynamic programming, we will reduce the problem with i piles to the smaller subproblem. As it is common in
DP, we solve the problem of size i using the result for the problem of size i - 1.

One may not take any coins from the (i - 1)-th pile and take at most coins coins from the leftmost i - 1 piles.
One may take one coin from the (i - 1)-th pile, and at most coins - 1 coins from the leftmost i - 1 piles.
One may take two coins from the (i - 1)-th pile, and at most coins - 2 coins from the leftmost i - 1 piles.
...
One may take currentCoins coins from the (i - 1)-th pile, and at most coins - currentCoins coins from the leftmost
i - 1 piles.
...
When we choose currentCoins coins from the (i - 1)-th pile, we must optimally choose at most coins - currentCoins coins
from the leftmost i - 1 piles (numbered from 0 to i - 2). It may be easier to think about it in reverse: when we are at
pile i - 1 with coins remaining space in our wallet, every coin we take reduces our space by 1. We need to determine
the optimal number of coins to take before moving to the next pile.

Let currentSum be the sum of the taken coins from the (i - 1)-th pile (their quantity is currentCoins).

When the value of currentCoins is optimal, dp[i][coins] = dp[i - 1][coins - currentCoins] + currentSum, because
dp[i - 1][coins - currentCoins] gives the optimal answer to the smaller subproblem of size i - 1.

There are two constraints for currentCoins: first, one cannot take more coins from the (i - 1)-th pile than the amount
of coins the pile has (piles[i - 1].length); and second, we cannot take more coins than we are allowed, so currentCoins
must not exceed coins.

Combining these two constraints, one concludes that all values of currentCoins between 0 and
min(piles[i - 1].length, coins) inclusively are feasible. We try all these values to find the optimal one.

Finally, we can formulate the DP transitions: dp[i][coins] is the maximum dp[i - 1][coins - currentCoins] + currentSum
over currentCoins between 0 and min(piles[i - 1].length, coins) inclusively.

Since it is never optimal to take less than k coins if it is allowed to take k, the answer to the problem
is dp[n][k] – one takes at most k coins (in the optimal solution we will take exactly k) from n piles.

Algorithm
1. Declare the DP table and initialize it with zeros.
2. Iterate i from 1 to n.
    Iterate coins from 0 to k.
        Initialize currentSum = 0.
        Iterate currentCoins from 0 to min(piles[i - 1].length, coins).
            If currentCoins > 0, increase currentSum by piles[i - 1][currentCoins - 1].
            Update the value of dp[i][coins] with dp[i - 1][coins - currentCoins] + currentSum.
Return dp[n][k].
"""