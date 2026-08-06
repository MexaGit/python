from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)  # Length of the input array

        # Step 1: Create the prefix sum array
        prefix = [nums[0]]  # Initialize with the first element
        for i in range(1, n):
            # Append the cumulative sum to the prefix array
            prefix.append(prefix[-1] + nums[i])

        ans = 0  # Initialize the count of valid splits
        # Step 2: Iterate through the array to find valid splits
        for i in range(n - 1):
            left_section = prefix[i]  # Sum of the left section
            right_section = prefix[-1] - prefix[i]  # Sum of the right section
            # Check if the left section is greater than or equal to the right section
            if left_section >= right_section:
                ans += 1  # Increment the count of valid splits

        return ans  # Return the total count of valid splits

# Example usage
solution = Solution()
print(solution.waysToSplitArray([10, 4, -8, 7]))  # Output: 2
print(solution.waysToSplitArray([1, 2, 3, 4, 5, 6]))  # Output: 3

"""
Time Complexity: O(n), where n is the length of nums (for creating the prefix sum and processing the splits).
Space Complexity: O(n) for the prefix sum array.
"""