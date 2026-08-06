class NumArray:
    def __init__(self, nums):
        # Store the prefix sums - len = [0,0,0,0,0,0,0] = 7 zeros
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            # self.prefix_sums[0] = 0 represents the sum of 0 elements (i.e., an empty sum).
            # This provides a base case for calculations that involve the beginning of the array.
            # start to populate the prefix from the index[i], in this case start in range(1, 6 + 1)
            self.prefix_sums[i] = self.prefix_sums[i - 1] + nums[i - 1]
        # has you see you have one more index
        print(self.prefix_sums)

    # sumRange(0, right) = prefix_sums[right + 1] - prefix_sums[0]
    def sumRange(self, left, right):
        # Calculate the sum of the range using prefix sums
        return self.prefix_sums[right + 1] - self.prefix_sums[left]

# Example usage
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2))  # Output: 1
print(numArray.sumRange(2, 5))  # Output: -1
print(numArray.sumRange(0, 5))  # Output: -3

"""
Input - https://chatgpt.com/c/66f630cc-8524-8002-a952-60dd449ce626
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Time Complexity:

Initialization: O(n) (for creating the prefix sums).
Each sumRange query: O(1).
Overall complexity for multiple queries: O(n + q), where q is the number of queries.

Space Complexity:

The space used for the prefix sums array is O(n).

Visual Representation
Here's a table summarizing nums and prefix_sums:

Index (i)	nums[i-1]	prefix_sums[i]	Explanation
0	        N/A	        0	            Base case (sum of 0 elements)
1	        -2	        -2	            Sum of first 1 element: -2
2	        0	        -2	            Sum of first 2 elements: -2 + 0 = -2
3	        3	        1	            Sum of first 3 elements: -2 + 0 + 3 = 1
4	        -5	        -4	            Sum of first 4 elements: 1 + (-5) = -4
5	        2	        -2	            Sum of first 5 elements: -4 + 2 = -2
6	        -1	        -3	            Sum of first 6 elements: -2 + (-1) = -3

"""