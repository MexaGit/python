def fn(arr, target):
    left = 0  # Start at the beginning of the array
    right = len(arr)  # End one past the last element (exclusive range)

    # Continue searching while left is less than right
    while left < right:
        mid = (left + right) // 2  # Find the middle element

        # If the mid element is >= target, move the right boundary
        if arr[mid] >= target:
            right = mid  # Narrow the search to the left half
        else:
            left = mid + 1  # Narrow the search to the right half

    # When the loop ends, 'left' is the first position where target can be inserted
    return left

# Example usage
print(fn([1, 3, 5, 7, 9], 3))


# What Does This Code Do?
# This version of binary search finds the first position in the sorted array where the target could be inserted to
# maintain sorted order. If the target exists in the array, it returns the index of the first occurrence.
# If it doesn’t exist, it returns the index where the target could be inserted.

"""
What Can This Code Be Used For?
Finding the First Occurrence:  
    If the target is in the array, the function returns the first index where the target appears (like a lower bound).
    
Finding the Insertion Point:
    If the target isn’t in the array, the function returns the index where it should be inserted to keep the array 
    sorted.
Use Case in Real Life:
    Binary search insertion is useful in sorted lists where you need to maintain order when adding new elements, such as in:
        Leaderboards (placing scores in order)
        Autocomplete suggestions (inserting words in order)
    Stock prices (keeping prices sorted by value)
"""