from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0  # Initialize the count of valid splits
        left_section = 0  # Sum of the left section
        total = sum(nums)  # Total sum of the array

        # Iterate through the array, except the last element
        for i in range(len(nums) - 1):
            left_section += nums[i]  # Add the current element to the left section
            right_section = total - left_section  # Calculate the right section sum
            # Check if the left section is greater than or equal to the right section
            if left_section >= right_section:
                ans += 1  # Increment the count of valid splits

        return ans  # Return the total count of valid splits

# Example usage
solution = Solution()
print(solution.waysToSplitArray([10, 4, -8, 7]))  # Output: 2
print(solution.waysToSplitArray([1, 2, 3, 4, 5, 6]))  # Output: 3

"""
Time Complexity: O(n), where n is the length of nums (for calculating the total and iterating through the elements).
Space Complexity: O(1), as no additional space is used that grows with the input size.
"""