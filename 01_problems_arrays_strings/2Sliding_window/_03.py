def find_best_subarray(nums, k):
    curr = 0  # Initialize the current sum of the first k elements

    # Step 1: Calculate the sum of the first k elements
    for i in range(k):
        curr += nums[i]

    ans = curr  # Initialize the answer with the current sum

    # Step 2: Slide the window across the array
    for i in range(k, len(nums)):
        # Update the current sum by adding the next element and removing the element that's sliding out
        # curr += nums[i] - nums[i - k]  # Adding the new element and removing the old one
        # curr += nums[3] - nums[0]
        # curr += 6 + 4 - 1 = 9
        # curr += nums[i] - nums[i - k]
        # curr += nums[4] - nums[1]
        # curr += 9 + 5 - 2 = 12  # Now curr holds the sum of the subarray [3, 4, 5]
        curr += nums[i] - nums[i - k]
        # Update the answer with the maximum sum found
        ans = max(ans, curr)

    return ans  # Return the maximum sum of any subarray of length k

# Example usage
print(find_best_subarray([1, 2, 3, 4, 5], 3))  # Output: 12 (subarray [3, 4, 5])
print(find_best_subarray([2, 1, 5, 2, 3], 2))  # Output: 7 (subarray [5, 2])
print(find_best_subarray([1, 2, 3], 1))  # Output: 3 (subarray [3])

"""
Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

Time Complexity: O(n), where n is the length of the input list nums. Each element is processed a constant number 
of times (once during the initial sum and once during the sliding window).

Space Complexity: O(1) since no additional space is used that scales with the input size.

This part is key to understanding the sliding window concept:
Sliding the window: We start sliding the window across the array by updating curr on each iteration. For each new 
element that comes into the window (nums[i]), we add its value to the current sum. Simultaneously, we subtract the 
value of the element that is sliding out of the window (nums[i - k]).

Explanation of the update:
Add the new element: nums[i] is the element at the current index i, and it enters the window.
Subtract the element that is leaving: nums[i - k] is the element k steps behind i, which is now outside the window 
and should be removed from the sum.
For example:

If nums = [1, 2, 3, 4, 5] and k = 3, after calculating the initial sum of the first subarray [1, 2, 3], we move to 
the next subarray [2, 3, 4]. To do this, we:
Subtract 1 (the element at index i - k = 0) because it’s sliding out of the window.
Add 4 (the element at index i = 3) because it’s entering the window.
So the updated sum for the subarray [2, 3, 4] is:
curr=6+4−1=9

We then update ans with the maximum of ans and curr.
Update the maximum sum:

After updating curr with the sum of the new window, we check if it's greater than the previous maximum sum (ans). 
If it is, we update ans.

Example Walkthrough:
Let's consider an example with nums = [1, 2, 3, 4, 5] and k = 3:
Initial sum of first k elements ([1, 2, 3]):
curr = 1 + 2 + 3 = 6
ans = 6
First window slide: Move the window to the subarray [2, 3, 4]:
Update curr: curr = curr + nums[3] - nums[0] = 6 + 4 - 1 = 9
Update ans: ans = max(6, 9) = 9
Next window slide: Move the window to the subarray [3, 4, 5]:
Update curr: curr = curr + nums[4] - nums[1] = 9 + 5 - 2 = 12
Update ans: ans = max(9, 12) = 12
The function will return 12, which is the sum of the subarray [3, 4, 5].
"""