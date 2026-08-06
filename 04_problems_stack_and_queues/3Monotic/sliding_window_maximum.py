from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # List to store the maximum values for each window
        ans = []
        # Deque to store indices of the elements in the current window
        queue = deque()
        for i in range(len(nums)):
            # maintain monotonic decreasing.
            # all elements in the deque smaller than the current one
            # have no chance of being the maximum, so get rid of them
            # Remove indices from the back while the current element is greater
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # queue[0] is the index of the maximum element.
            # if queue[0] + k == i, then it is outside the window
            # If the leftmost index is out of the current window, remove it
            if queue[0] + k == i:
                queue.popleft()

            # only add to the answer once our window has reached size k
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans

# Test case with an increasing sequence
# Input: nums = [1, 3, 5, 7, 9], k = 3
# Expected Output: [5, 7, 9]
# Explanation:
# Window 1: [1, 3, 5] → max = 5
# Window 2: [3, 5, 7] → max = 7
# Window 3: [5, 7, 9] → max = 9

solution = Solution()
print(solution.maxSlidingWindow([1, 3, 5, 7, 9], 3))  # Output: [5, 7, 9]

# Test case with mixed values and duplicates
# Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Expected Output: [3, 3, 5, 5, 6, 7]
# Explanation:
# Window 1: [1, 3, -1] → max = 3
# Window 2: [3, -1, -3] → max = 3
# Window 3: [-1, -3, 5] → max = 5
# Window 4: [-3, 5, 3] → max = 5
# Window 5: [5, 3, 6] → max = 6
# Window 6: [3, 6, 7] → max = 7

solution = Solution()
print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3, 3, 5, 5, 6, 7]

