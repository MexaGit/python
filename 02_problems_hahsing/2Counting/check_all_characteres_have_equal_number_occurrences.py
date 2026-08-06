from collections import defaultdict
from collections import  Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        print(counts.keys(), counts.values(), counts.items())

        frequencies = counts.values()
        # A set automatically removes duplicate values,
        # Since there's only one unique frequency (2) - ('a', 2), ('b', 2), ('c', 2)
        print(len(frequencies), len(set(frequencies)), set(frequencies), frequencies)
        return len(set(frequencies)) == 1

    def areOccurrencesEqual1(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1

solution = Solution()
print(solution.areOccurrencesEqual("abacbc"))

"""
Given a string s, determine if all characters have the same frequency.
For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb", return false. "a"
appears 3 times, "b" appears 2 times. 3 != 2.

Example 1:
Input: s = "abacbc"
Output: true

Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
"""