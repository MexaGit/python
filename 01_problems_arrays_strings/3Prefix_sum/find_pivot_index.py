class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)  # Total sum of the array
        left_sum = 0  # Initialize the left sum

        # Iterate through the array to find the pivot index
        for idx, ele in enumerate(nums):
            # right_sum is calculated by subtracting left_sum and the current element (ele) from total_sum
            right_sum = total_sum - left_sum - ele
            # Example of right_sum calculation:
            # If nums = [1, 7, 3, 6, 5, 6]:
            # - When idx = 0 (ele = 1):
            #   right_sum = total_sum - left_sum - ele
            #   = 28 - 0 - 1 = 27
            #
            # - When idx = 1 (ele = 7):
            #   right_sum = 28 - 1 - 7 = 20
            #
            # - When idx = 2 (ele = 3):
            #   right_sum = 28 - 8 - 3 = 17
            #
            # - When idx = 3 (ele = 6):
            #   right_sum = 28 - 11 - 6 = 11
            #
            # - When idx = 4 (ele = 5):
            #   right_sum = 28 - 17 - 5 = 6
            #
            # - When idx = 5 (ele = 6):
            #   right_sum = 28 - 22 - 6 = 0

            # Check if left sum equals right sum
            if left_sum == right_sum:
                return idx  # Return the pivot index

            left_sum += ele  # Update left sum for the next index

        return -1  # Return -1 if no pivot index is found


# Example usage
solution = Solution()

# Example 1:
# For the array [1, 7, 3, 6, 5, 6]:
# Total sum of the array = 1 + 7 + 3 + 6 + 5 + 6 = 28
# Now, the goal is to find an index where the sum of elements to the left equals the sum of elements to the right
# At index 3 (element 6):
#   Left sum = 1 + 7 + 3 = 11
#   Right sum = 5 + 6 = 11
# Since left_sum == right_sum at index 3, the output is 3
print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3

# Example 2:
# For the array [1, 2, 3]:
# Total sum of the array = 1 + 2 + 3 = 6
# There's no index where the left sum equals the right sum
# The output is -1
print(solution.pivotIndex([1, 2, 3]))  # Output: -1

"""
In your specific code (pivotIndex function):
The pivot index is a position in the array where the sum of all elements to the left of that index equals 
the sum of all elements to the right.
    For example, in the array [1, 7, 3, 6, 5, 6], the pivot index is 3. This is because:
    The sum of the elements on the left side of index 3 ([1, 7, 3]) is 11.
    The sum of the elements on the right side of index 3 ([5, 6]) is also 11.
    Thus, the sum of the left and right sides of index 3 is equal, making index 3 the pivot.
    
General meaning of a pivot:
    A pivot in general terms can refer to something that serves as the central point around which other things 
    are balanced or rotate. In algorithms, it often refers to a point that divides a set into two balanced parts.
    
Time Complexity:
The function calculates the total sum of the array using sum(nums), which takes O(n) time, where n is the length 
of the array.
The subsequent loop iterates through the array once, checking for the pivot index, which also takes O(n) time.
Therefore, the overall time complexity is O(n).

Space Complexity:
The algorithm uses a constant amount of extra space for variables (total_sum and left_sum), regardless of the size 
of the input array.
No additional data structures are used that scale with the input size.
Thus, the overall space complexity is O(1).
"""