from typing import List

class Solution:
    # Approach 3 (Dynamic programming - Bottom up) [Accepted]
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array with infinity for all amounts
        dp = [float('inf')] * (amount + 1)
        # Base case: to make the amount 0, we need 0 coins
        dp[0] = 0

        # Loop through each coin
        for coin in coins:
            # Update the dp array for all amounts that can be made with this coin
            for x in range(coin, amount + 1):
                # Update dp[x] to be the minimum of its current value or
                # using this coin (1 + dp[x - coin])
                dp[x] = min(dp[x], dp[x - coin] + 1)

        # Return the result: if dp[amount] is still infinity, it means we can't form that amount
        return dp[amount] if dp[amount] != float('inf') else -1


# Test cases
solution = Solution()

# Test case 1: Coin denominations [1, 2, 5] and amount 11
coins1 = [1, 2, 5]
amount1 = 11
# The minimum number of coins needed is 3 (5 + 5 + 1)
print(solution.coinChange(coins1, amount1))  # Output: 3

# Test case 2: Coin denominations [2] and amount 3
coins2 = [2]
amount2 = 3
# It's not possible to make amount 3 with coin denomination 2, so output should be -1
print(solution.coinChange(coins2, amount2))  # Output: -1


"""
Approach 3 (Dynamic programming - Bottom up) [Accepted]
Algorithm
For the iterative solution, we think in bottom-up manner. Before calculating F(i), we have to compute all minimum
counts for amounts up to i. On each iteration i of the algorithm F(i) is computed as minj=0…n−1F(i−cj)+1

Bottom-up approach using a table to build up the solution to F6.

In the example above you can see that:

F(3)=min{F(3−c),F(3−c2),F(3−c)}+1
    =min{F(3−1),F(3−2),F(3−3)}+1
    =min{F(2),F(1),F(0)}+1
    =min{1,1,0}+1
    =1
"""