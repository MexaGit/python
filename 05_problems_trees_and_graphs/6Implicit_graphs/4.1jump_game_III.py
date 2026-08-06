from typing import List

class Solution:
    # Breadth-First Search
    def canReach(self, arr: List[int], start: int) -> bool:
        # Get the length of the array
        n = len(arr)

        # Initialize the queue with the starting index
        q = [start]

        # Perform BFS using the queue
        while q:
            node = q.pop(0)  # Get the current index from the queue

            # Check if we have reached a value of 0
            if arr[node] == 0:
                return True

            # If the value is negative, it means we have already visited this node
            if arr[node] < 0:
                continue

            # Check the next possible moves (left or right) based on the current value
            for i in [node + arr[node], node - arr[node]]:
                if 0 <= i < n:  # Ensure the next move is within bounds
                    q.append(i)

            # Mark the current node as visited by making its value negative
            arr[node] = -arr[node]

        # If no path to reach zero is found, return False
        return False

    # Depth-First Search
    def canReach1(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            arr[start] = -arr[start]
            return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])

        return False

# Test case 1: A reachable zero
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3
arr1 = [4, 2, 3, 0, 3, 1, 2]
start1 = 5
# Expected output: True (can reach 0 at index 3)
print(Solution().canReach(arr1, start1))

# Test case 2: Zero is not reachable
# Explanation: There is no way to reach at index 1 with value 0.
arr2 = [3, 0, 2, 1, 2]
start2 = 2
# Expected output: False (cannot reach 0 from any position)
print(Solution().canReach(arr2, start2))

"""
https://leetcode.com/problems/jump-game-iii/description/
Given an array of non-negative integers arr, you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

#----------------------------------------------------------------------------------------------#

You probably can guess from the problem title, this is the third problem in the series of Jump Game problems. 
https://leetcode.com/problems/jump-game/description/
Those problems are similar, but have considerable differences, making their solutions quite different.

Here, two approaches are introduced: Breadth-First Search approach and Depth-First Search approach.
Most solutions start from a brute force approach and are optimized by removing unnecessary calculations. Same as this 
one.

A naive brute force approach is to iterate all the possible routes and check if there is one reaches zero. However, 
if we already checked one index, we do not need to check it again. We can mark the index as visited by make it negative.
"""