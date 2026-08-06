
def fn(arr, target):
    left = 0  # Start at the beginning of the array
    right = len(arr) - 1  # End at the last element

    # Keep searching while the search range is valid
    while left <= right:
        mid = (left + right) // 2  # Find the middle element

        # If we found the target, do something (e.g., return index)
        if arr[mid] == target:
            # do something
            return mid  # Typically, we return the index

        # If the middle element is greater than the target, search left half
        if arr[mid] > target:
            right = mid - 1  # Narrow the search to the left half
        else:
            left = mid + 1  # Narrow the search to the right half

    # If we exit the loop, the target wasn’t found.
    # 'left' is the correct insertion point to maintain sorted order
    return left  # Return the insertion point


# What Does This Code Do?
# This function performs a binary search on a sorted array to look for a given target. If the target is found,
# it returns immediately (though you’d typically return the index where it was found). If the target isn’t found,
# it returns the position where the target could be inserted to maintain the sorted order.

"""
Summary
This binary search function can be used to:
    Search for a target element in a sorted array.
    Find the insertion point for the target if it doesn’t exist in the array.
This function ensures that the array remains sorted even if the target needs to be inserted.
"""