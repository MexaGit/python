from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Helper function to generate all possible combinations by changing one digit at a time.
        def neighbors(node):
            ans = []
            for i in range(4):
                num = int(node[i])  # Current digit at position i.
                for change in [-1, 1]:  # Increment or decrement the digit by 1.
                    x = (num + change) % 10  # Ensure the digit wraps around using modulo 10.
                    ans.append(node[:i] + str(x) + node[i + 1:])  # Generate the new combination.
            return ans

        # If the starting point "0000" is a deadend, return -1 immediately.
        if "0000" in deadends:
            return -1

        # Initialize a queue with the starting point "0000" and a set of deadends.
        queue = deque([("0000", 0)])  # Store the lock state and number of moves.
        seen = set(deadends)  # Store visited nodes.
        seen.add("0000")  # Mark the initial state as visited.

        # BFS to find the shortest path to unlock the lock.
        while queue:
            node, steps = queue.popleft()

            # If the current node is the target combination, return the number of moves.
            if node == target:
                return steps

            # Generate all neighboring combinations.
            for neighbor in neighbors(node):
                if neighbor not in seen:  # If the neighbor hasn't been visited yet.
                    seen.add(neighbor)  # Mark it as visited.
                    queue.append((neighbor, steps + 1))  # Add it to the queue with incremented steps.

        # If we exhaust the queue without finding the target, return -1.
        return -1


# Test Cases
solution = Solution()

# Test Case 1: Normal case, the lock can be opened.
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
deadends1 = ["0201", "0101", "0102", "1212", "2002"]
target1 = "0202"
print(solution.openLock(deadends1, target1))  # Output: 6

# Test Case 2: The starting point is a deadend.
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
deadends2 = ["0000"]
target2 = "8888"
print(solution.openLock(deadends2, target2))  # Output: -1

"""
https://leetcode.com/problems/open-the-lock/description/
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock
will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of
turns required to open the lock, or -1 if it is impossible.

#-----------------------------------------------------------------------------------------------------#

Whenever a problem is asking for the minimum number of steps/operations/moves to do something, you should immediately 
think if BFS could be used.

We can think about each number in the range [0, 9999] as a node. For a given node, the neighbors are all numbers that 
differ in only one position by a value of one (while considering the wrap-around case of 0 and 9).

Let's use a helper function neighbors that takes a node and generates all strings that differ in one position by a 
value of one.

Once we have this function, the implementation comes down to a very simple BFS that we have done many times already. 
Associate the number of steps taken so far with each node in the queue. For each (node, steps) pair, if node = target, 
then return steps. Otherwise, iterate over neighbors(node) and for each neighbor, check if it has been visited already 
(using a set seen). If it hasn't, push (neighbor, steps + 1) onto the queue. We start the BFS from "0000".

One last thing: we have an added restriction where we can't visit any nodes in deadends. We can initialize seen with 
all these nodes since seen already provides us with the function of not visiting nodes.
"""