from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        averages = [-1] * len(nums)  # Initialize averages list with -1
        # If k is 0, return nums since each average will be the number itself
        if k == 0:
            return nums

        # all elements in nums between the indices i - k and i + k (inclusive).
        window_size = 2 * k + 1  # Total size of the window k + 1 + k = 2 * k + 1
        n = len(nums)  # Length of the input list

        # If the window size is greater than the list, return averages initialized to -1
        if window_size > n:
            return averages

        # Calculate the sum of the first window
        window_sum = sum(nums[:window_size])
        averages[k] = window_sum // window_size  # Store average for the middle of the window

        # Slide the window across the array
        for i in range(window_size, n):
            # Update the window sum by removing the element that is sliding out:
            # element at position i - window_size is no longer part of the window
            # and adding the new element that is coming into the window:
            # element at position i is the new number that’s coming into the window nums[i]
            window_sum = window_sum - nums[i - window_size] + nums[i]
            averages[i - k] = window_sum // window_size  # Store the average

        return averages  # Return the list of averages

# Example usage
solution = Solution()
print(solution.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))  # Output: [-1, -1, -1, 5, 4, 4, -1, -1, -1]
print(solution.getAverages([1, 2, 3, 4, 5], 1))  # Output: [-1, 2, 3, 4, -1]
print(solution.getAverages([1, 2, 3], 0))  # Output: [1, 2, 3]

"""
Time Complexity: O(n), where n is the length of nums. This includes the initial sum calculation and the sliding 
window updates.

Space Complexity: O(n), for storing the averages.
"""