from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            # Another way to solve this problem is to use a tuple of length 26 representing the count
            # of each character as the key instead of the sorted string.
            # ans[tuple(sorted(s))].append(s)
            key = "".join(sorted(s))
            groups[key].append(s)

        return groups.values()

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
"""