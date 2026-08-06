from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Helper function to perform binary search
        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        # Sort the potions array to perform binary search
        potions.sort()
        ans = []
        m = len(potions)

        # For each spell, find the number of successful pairs
        for spell in spells:
            # Find the minimum potion strength that can form a successful pair with the spell
            i = binary_search(potions, success / spell)
            ans.append(m - i)  # Add the count of successful pairs to the result

        return ans

# Example 1
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
#  Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.
print(Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))  # Expected output: [4, 0, 3]

# Example 2
# Input: spells = [3,1,2], potions = [8,5,8], success = 16
# Output: [2,0,2]
# Explanation:
# - 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
# - 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
# - 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
# Thus, [2,0,2] is returned.
print(Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16))  # Expected output: [2, 0, 2]

"""
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i]
represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their
strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with
the ith spell.

#-------------------------------------------------------------------------------------------#

Let's say we sort potions and have potions = [1, 2, 3, 4, 5], and success = 7.

We have a spell with a strength of 3. To form a successful pair, we need a potion with a strength of at 
least 7 / 3 = 2.3333.

If we do a binary search for this value on potions, we will find an insertion index of 2. Every potion on this index 
and to the right can form a successful pair. There are 3 indices in total (the potions with strength 3, 4, 5).

In general, if there are m potions, the final index is m - 1. If the insertion index is i, then the range [i, m - 1] 
has a size of (m - 1) - i + 1 = m - i.

We can iterate over the spells, and for each spell, perform a binary search on success / spell to find the insertion 
index i, then use the formula to find the number of potions that can form a successful pair.
"""