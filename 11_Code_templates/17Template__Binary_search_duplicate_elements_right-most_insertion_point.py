def fn(arr, target):
    left = 0  # Start at the beginning of the array
    right = len(arr)  # Search ends just past the last index

    while left < right:  # Loop until the search space is exhausted
        mid = (left + right) // 2  # Find the middle index

        # If the middle element is greater than the target
        if arr[mid] > target:
            right = mid  # Narrow the search to the left half
        else:  # If mid is <= target, move left to mid + 1
            left = mid + 1

    # Return the insertion point (left will be at the correct index)
    return left


# What Does This Code Do?
# This function performs a binary search to find the smallest index where the target can be inserted such that:
# If the target is present, it returns the first position after the last occurrence of the target (the upper bound).
# If the target is not present, it returns the insertion point where the target could be placed to maintain the sorted
# order.

"""
Summary:
This version of binary search helps find the upper bound of a target in a sorted array. If the target exists, 
it returns the first position after the target’s last occurrence. If the target does not exist, it returns the 
insertion point to maintain the sorted order.

Use Cases:
    Finding the upper bound of a target in a sorted array.
    Determining the insertion point for a new element in a sorted array.
    Useful in problems like searching for intervals or scheduling tasks where you need to insert values while keeping 
    everything in order.
Key Differences from Standard Binary Search:
    Always returns the first position after the target if it exists.
    Returns the insertion point if the target does not exist.
    Narrow search based on > vs. <= condition to find the upper bound.
"""