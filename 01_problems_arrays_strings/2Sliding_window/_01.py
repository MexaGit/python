def find_length(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0  # Initialize left pointer, current sum, and answer variable

    # Iterate through the array with the right pointer
    for right in range(len(nums)):
        curr += nums[right]  # Add the current number to the current sum

        # While the current sum exceeds k, move the left pointer to reduce the sum
        # less than or equal to k
        while curr > k:
            curr -= nums[left]  # Subtract the number at the left pointer from the sum
            left += 1  # Move the left pointer to the right

        # Update the answer with the maximum length of the valid window found
        ans = max(ans, right - left + 1)

    return ans  # Return the maximum length of the subarray found

# Example usage
print(find_length([1, 2, 3, 4, 5], 11))  # Output: 4 (subarray [1, 2, 3, 4]) = 10
# In this case, all the valid subarrays ([2, 1], [1, 5], [5, 2], [2, 3]) have a length of 2.
# The first such subarrays found by the sliding window are [2, 1] or [1, 5].
print(find_length([2, 1, 5, 2, 3], 7))   # Output: 2 (subarray [2, 1] or [1, 5])
print(find_length([1, 2, 3, 1, 1, 1], 9))  # Output: 6 (subarray [1, 2, 3, 1, 1, 1])

"""
To summarize what each variable does in the code:
left: the leftmost index of our current window
right: the rightmost index of our current window
curr: the sum of our current window
ans: the length of the longest valid window we have seen so far

Iterate right over the input to add elements to the window. Update curr by adding nums[right] to it. 
When the window becomes invalid (curr > k), remove elements from the window by subtracting nums[left] from curr. 
Then increment left. We need to do this until the window becomes valid again, so we use a while loop.

The size of a window is right - left + 1. Update our answer only when the window becomes valid.
Time Complexity: O(n), where n is the length of the input list nums. Each element is processed at most twice 
(once by the right pointer and once by the left pointer).

Space Complexity: O(1) since no additional space is used that scales with the input size.
"""