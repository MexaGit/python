from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort both arrays first
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        result = []

        # Two-pointer technique
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1  # Move pointer i if nums1[i] is smaller
            elif nums1[i] > nums2[j]:
                j += 1  # Move pointer j if nums2[j] is smaller
            else:
                # Both elements are equal, add to result and move both pointers
                result.append(nums1[i])
                i += 1
                j += 1

        return result


# Example usage
solution = Solution()
print(solution.intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9]

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return 
the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Explanation: [9,4] is also accepted.
"""
