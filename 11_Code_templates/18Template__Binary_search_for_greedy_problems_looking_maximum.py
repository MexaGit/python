def fn(arr):
    def check(x):
        # Implement this depending on the problem
        return BOOLEAN  # Returns True or False based on the condition

    left = MINIMUM_POSSIBLE_ANSWER  # The smallest possible value to consider
    right = MAXIMUM_POSSIBLE_ANSWER  # The largest possible value to consider

    # Binary search loop to find the largest possible value that meets the condition
    while left <= right:
        mid = (left + right) // 2  # Check the middle value

        if check(mid):  # If the condition is satisfied for mid
            left = mid + 1  # Try a larger value
        else:
            right = mid - 1  # Try a smaller value

    # When the loop exits, 'right' will be the largest value that satisfies the condition
    return right

# What Does This Code Do?
# This code performs binary search on the answer to find the largest possible value that satisfies a certain condition.
# The key part is the check() function, which is a custom function that returns True or False depending on whether a
# given value (in this case, mid) meets the problem’s condition.

"""
When Do We Use This Pattern?
This pattern is used when:
    You need to maximize or minimize some value.
    You don’t search an array directly but instead search a range of possible answers 
    (like finding the largest feasible value that meets a condition).
Problems like:
    Allocating resources (e.g., distributing items to people, minimizing the maximum load).
    Scheduling problems (e.g., minimum time required to finish all tasks).
    Finding the longest or shortest possible value that satisfies a constraint (like the longest side of a square).
"""