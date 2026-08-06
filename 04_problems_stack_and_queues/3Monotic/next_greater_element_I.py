from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary to hold the next greater elements
        next_greater = {}
        stack = []  # Stack to keep track of the elements for which we need to find the next greater

        # Iterate through nums2
        for num in nums2:
            # While stack is not empty and the current number is greater than the number at the stack's top
            while stack and num > stack[-1]:
                # Map the number at the top of the stack to the current number
                next_greater[stack.pop()] = num
            # Push the current number onto the stack
            stack.append(num)

        result = []  # Initialize the result list
        # Prepare the result based on nums1
        # return [next_greater.get(num, -1) for num in nums1]
        for num in nums1:
            next_greater_value = next_greater.get(num, -1)
            result.append(next_greater_value)
        return result

# Test case with the provided input
# Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
# Expected Output: [-1, 3, -1]
# Explanation:
# - For 4 in nums2: No greater element, output -1
# - For 1 in nums2: Next greater element is 3
# - For 2 in nums2: No greater element, output -1

solution = Solution()
print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))  # Output: [-1, 3, -1]

# Test case with the provided input
# Input: nums1 = [2, 4], nums2 = [1, 2, 3, 4]
# Expected Output: [3, -1]
# Explanation:
# - For 2 in nums2: Next greater element is 3
# - For 4 in nums2: No greater element, output -1

solution = Solution()
print(solution.nextGreaterElement([2, 4], [1, 2, 3, 4]))  # Output: [3, -1]

"""
The next greater element of some element x in an array is the first greater element that is to the right of x
in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater
element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]

Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
"""