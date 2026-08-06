from typing import List

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # If N is 1, return all single-digit numbers (0-9)
        if N == 1:
            return [i for i in range(10)]

        # Initialize the queue with candidates for the first level (1 to 9)
        # We start from 1 to avoid leading zeros
        queue = [digit for digit in range(1, 10)]

        # Iterate N-1 times because we are building a number with N digits
        for level in range(N-1):
            next_queue = []  # Prepare to hold the next level of numbers
            for num in queue:
                tail_digit = num % 10  # Get the last digit of the current number
                # Use a set to avoid duplicates when K == 0 (e.g., if K=0, both next digits will be the same)
                next_digits = set([tail_digit + K, tail_digit - K])

                # Generate the next numbers by appending the valid next digits
                for next_digit in next_digits:
                    # Check if the next digit is valid (0-9)
                    if 0 <= next_digit < 10:
                        # Form the new number by appending next_digit to num
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)  # Add the new number to the next level queue
            # Move to the next level of numbers
            queue = next_queue

        # Return the final list of numbers with N digits
        return queue

# Example Test Cases
# Test Case 1: N = 3, K = 7
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
print(Solution().numsSameConsecDiff(3, 7))
# Expected Output: [181, 292, 707, 818, 929]

# Test Case 2: N = 2, K = 1
print(Solution().numsSameConsecDiff(2, 1))
# Expected Output: [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]

# Test Case 3: N = 1, K = 0
print(Solution().numsSameConsecDiff(1, 0))
# Expected Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


"""
https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
Given two integers n and k, return an array of all the integers of length n where the difference between every two
consecutive digits is k. You may return the answer in any order.

Note that the integers should not have leading zeros. Integers as 02 and 043 are not allowed.

#-------------------------------------------------------------------------------------------------#

Overview
The problem asks us to come up a list of digit combinations that follow the defined pattern.
Before jumping to the implementation, it is always helpful to manually deduce some examples.

Suppose that we have N=3 and K=2, i.e. we should come up a series of 3-digits numbers, where for each number the
difference between each adjacent digits is 2.

Let us try to build the number digit by digit. Starting from the highest digit (in the image), we can pick the digit 1.
Then for the next digit, we need to pick 3 (i.e. 1+2).
Finally, for the last digit, we could have two choices: 5 and 1 (i.e. 3+2,3−2).
We illustrate the process in the following graph, where each node represents a digit that we pick, and the level of the
node corresponds to the position that the digit situates in the final number.

tree illustration

As one might notice that, we just converted the problem into a tree traversal problem, where each path from the root to
a leaf forms a solution for the problem.

As we know, the common algorithms for the tree traversal problem would be DFS (Depth-First Search) and BFS
(Breadth-First Search), which are exactly what we will present in the following sections.

Approach 2: BFS (Breadth-First Search)
Intuition

It might be more intuitive to come up a DFS solution as we presented before.
However, it is also viable to solve this problem with BFS (Breadth-First Search) traversal strategy.

Rather than building the solution one by one, we could do it batch by batch, i.e. level by level.

Each level contains the numbers that are of the same amount of digits.
Also, each level corresponds to the solutions with a specific number of digits.

BFS

For example, given N=3 and K=7, at the first level, we would have potentially 9 candidates
(i.e. [1, 2, 3, 4, 5, 7, 8, 9]).
When we move on to the second level, the candidates are reduced down to [18, 29, 70, 81, 92].
Finally, at the last level, we would have the solutions as [181, 292, 707, 818, 929].

Algorithm

Here are a few steps to implement the BFS algorithm for this problem.
    We could implement the algorithm with nested two-levels loops, where the outer loop iterates through levels and the
    inner loop handles the elements within each level.
    We could use a list data structure to keep the numbers for a single level, i.e. here we name the variable as queue.
    For each number in the queue, we could apply the same logics as in the DFS approach, except the last step, rather
    than making a recursive call for the next number we simply append the number to the queue for the next level.
"""