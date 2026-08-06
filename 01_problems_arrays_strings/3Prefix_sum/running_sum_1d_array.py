from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        left = 0  # Initialize the cumulative sum
        ans = []   # List to store the running sum results

        # Iterate through each number in the input list
        for num in nums:
            left += num  # Add the current number to the cumulative sum
            ans.append(left)  # Append the current cumulative sum to the results list

        return ans  # Return the list of running sums

# Example usage
solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]
print(solution.runningSum([1, 1, 1, 1]))  # Output: [1, 2, 3, 4]
print(solution.runningSum([3, 1, 2, 10]))  # Output: [3, 4, 6, 16]

"""
Time Complexity: O(n), where n is the length of nums (due to the single loop iterating through the list).
Space Complexity: O(n) for storing the results in ans.
"""