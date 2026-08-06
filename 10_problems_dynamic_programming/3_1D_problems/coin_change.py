from functools import lru_cache
from typing import List

class Solution:
    # (Dynamic programming - Top down) [Accepted]
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Define a depth-first search (DFS) function with memoization
        @lru_cache(None)
        def dfs(rem):
            # If the remaining amount is negative, it's an invalid path
            if rem < 0:
                return -1

            # If no remaining amount, we found a valid combination
            if rem == 0:
                return 0

            # Initialize the minimum cost to infinity
            min_cost = float('inf')
            # Try each coin in the list
            for coin in coins:
                # Recursively call dfs with the remaining amount after using the current coin
                res = dfs(rem - coin)
                # If the result is valid (not -1), update the minimum cost
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            # Return the minimum cost found, or -1 if no combination was found
            return min_cost if min_cost != float('inf') else -1

        # Start the DFS with the initial amount
        return dfs(amount)


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
You are given an integer array coins representing coins of different denominations and an integer amount representing a
total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Approach 2 (Dynamic programming - Top down) [Accepted]
Intuition
Could we improve the exponential solution above? Definitely! The problem could be solved with polynomial time using
Dynamic programming technique. First, let's define:

F(S) - minimum number of coins needed to make change for amount S using coin denominations [c0…cn−1]

We note that this problem has an optimal substructure property, which is the key piece in solving any Dynamic
Programming problems. In other words, the optimal solution can be constructed from optimal solutions of its subproblems.
How to split the problem into subproblems? Let's assume that we know F(S) where some change val1,val2,… for S which
is optimal and the last coin's denomination is C.

Then the following equation should be true because of optimal substructure of the problem:

F(S)=F(S−C)+1

But we don't know which is the denomination of the last coin C. We compute F(S−ci) for each possible denomination
c0,c1,c2…cn−1 and choose the minimum among them. The following recurrence relation holds:

F(S)=mini=0...n−1F(S−ci)+1
subject to  S−ci≥0

F(S)=0 ,when S=0
F(S)=−1 ,when n=0

In the recursion tree above, we could see that a lot of subproblems were calculated multiple times. For example the
problem F(1) was calculated 13 times. Therefore we should cache the solutions to the subproblems in a table and access
them in constant time when necessary

Algorithm
The idea of the algorithm is to build the solution of the problem from top to bottom. It applies the idea described
above. It use backtracking and cut the partial solutions in the recursive tree, which doesn't lead to a viable solution.
Тhis happens when we try to make a change of a coin with a value greater than the amount S. To improve time complexity
we should store the solutions of the already calculated subproblems in a table.
"""