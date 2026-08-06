def check_for_target(nums, target):
    left = 0  # Initialize the left pointer at the start of the list
    right = len(nums) - 1  # Initialize the right pointer at the end of the list

    # Continue until the two pointers meet
    while left < right:
        # curr is the current sum of the elements at the left and right pointers
        curr = nums[left] + nums[right]

        # Check if the current sum equals the target
        if curr == target:
            return True  # Return True if the target sum is found

        # If the current sum is greater than the target, move the right pointer left
        if curr > target:
            right -= 1
        else:
            # If the current sum is less than the target, move the left pointer right
            left += 1

    return False  # Return False if no pair sums to the target


# Example usage
print(check_for_target([1, 2, 3, 4, 6], 6))  # Output: True (2 + 4)
print(check_for_target([1, 2, 5], 10))  # Output: False

"""
Time Complexity: O(n), where n is the length of the input list, since we traverse the list with two pointers.
Space Complexity: O(1), as no additional space proportional to the input size is used.
"""