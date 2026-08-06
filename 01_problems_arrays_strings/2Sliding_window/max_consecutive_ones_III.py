from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Initialize the left pointer of the sliding window
        curr = 0  # Count of zeros in the current window
        ans = 0  # Maximum length of the subarray found

        # Iterate over the array using the right pointer
        for right in range(len(nums)):
            # If the current element is zero, increase the zero count
            if nums[right] == 0:
                curr += 1

            # While the count of zeros exceeds k, move the left pointer
            while curr > k:
                if nums[left] == 0:
                    curr -= 1  # Decrease the zero count
                left += 1  # Move the left pointer to the right

            # Update the maximum length of the subarray found
            ans = max(ans, right - left + 1)

        return ans  # Return the maximum length of subarray with at most k zeros


# Example usage
solution = Solution()
print(solution.longestOnes([1, 1, 0, 0, 1, 1, 1, 0], 2))  # Output: 7
print(solution.longestOnes([0, 0, 1, 1, 0, 1, 1, 1], 1))  # Output: 6
print(solution.longestOnes([1, 1, 1, 1, 0], 0))  # Output: 4

"""
Time Complexity: O(n), where n is the length of the input list nums. Each element is processed once.
Space Complexity: O(1) since no additional space is used that scales with the input size.
"""