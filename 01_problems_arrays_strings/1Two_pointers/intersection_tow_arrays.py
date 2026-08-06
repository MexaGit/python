from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Sort both arrays
        nums1.sort()
        nums2.sort()

        p1 = p2 = 0

        # Create set that stores integers appearing in both arrays
        intersection = set()

        while p1 < len(nums1) and p2 < len(nums2):
            # Add a value to the set if values at both pointers equal
            if nums1[p1] == nums2[p2]:
                intersection.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        # Convert intersection to an array
        result = []
        for x in intersection:
            result.append(x)

        # Return the result
        return result


solution = Solution()
print(solution.intersection([4,9,5], [9,4,9,8,4]))

"""
Given two integer arrays nums1 and nums2, return an array of their intersection:
(Array IntersectionThe intersection of two arrays is defined as the set of elements that are present in both arrays)
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Explanation: [4,9] is also accepted.
"""