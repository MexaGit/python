from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # When k is 0, the average of each element is the element itself
        if k == 0:
            return nums

        window_size = 2 * k + 1  # Size of the window for averaging
        n = len(nums)  # Length of the input list
        averages = [-1] * n  # Initialize the result list with -1

        # If the window size is larger than the list, return the averages initialized to -1
        if window_size > n:
            return averages

        # Generate 'prefix' array for 'nums'
        # 'prefix[i + 1]' will be the sum of all elements from index '0' to 'i'
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Calculate averages for valid indices
        for i in range(k, n - k):
            leftBound = i - k  # Start index for the subarray
            rightBound = i + k  # End index for the subarray
            subArraySum = prefix[rightBound + 1] - prefix[leftBound]  # Calculate the sum of the subarray
            average = subArraySum // window_size  # Calculate the average
            averages[i] = average  # Store the average at index i

        return averages  # Return the list of averages

# Example usage
solution = Solution()
print(solution.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))  # Output: [-1, -1, 5, 4, 4, -1, -1, -1]
print(solution.getAverages([1, 2, 3, 4, 5], 1))  # Output: [2, 3, 4, 3, 2]
print(solution.getAverages([1, 2, 3], 0))  # Output: [1, 2, 3]
