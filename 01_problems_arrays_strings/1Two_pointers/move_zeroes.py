class Solution:
    def moveZeroes(self, nums):
        # Pointer for the position of the next non-zero element
        pos = 0

        # Loop through the list
        for i in range(len(nums)):
            # If the current element is not zero, we want to move it
            if nums[i] != 0:
                # Swap the elements at pos and i
                nums[pos], nums[i] = nums[i], nums[pos]
                # Move the pos pointer to the right
                pos += 1

        return nums

# Example usage
sol = Solution()
print(sol.moveZeroes([0, 1, 0, 3, 12]))

"""
Time Complexity of moveZeroes:

Loop through the list:
The algorithm loops through the list exactly once using a for loop. If the length of the list is n, the time complexity
 of this loop is O(n), where n is the number of elements in the list nums.
 
Swapping elements:
During each iteration, the code checks if the current element is non-zero. If it is, a swap operation is performed 
between nums[i] and nums[pos]. Since each swap operation is a constant time operation (O(1)), this doesn’t add to 
the overall complexity.
The loop runs n times, and each iteration takes constant time. Thus, the overall time complexity is O(n).

Space Complexity of moveZeroes:

In-place modification:
The algorithm modifies the input list nums in place. No additional data structures (such as new lists or arrays) 
are created that depend on the input size.

Constant extra space:
The only extra variable used is pos, which takes constant space (O(1)).
Thus, the space complexity is O(1) because the space used does not scale with the input size.

What is O(1) in Big O Notation?
O(1) represents constant time complexity, meaning that the time it takes to run the algorithm or operation is 
independent of the size of the input. Whether the input is small or large, an O(1) operation always takes the same 
amount of time.

Key Characteristics of O(1):
Constant Time: The operation does not grow in complexity as the input size increases. It always takes a fixed, 
constant amount of time to execute.
Fast and Efficient: Since O(1) operations are constant time, they are considered very efficient, even for large inputs.
Simple Operations: Operations like accessing an element in an array by its index, assigning a value to a variable, 
or performing a basic arithmetic operation (addition, subtraction, etc.) are typically O(1).
"""