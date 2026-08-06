class Solution:
    def partitionString(self, s: str) -> int:
        lastSeen = [-1]*26
        count = 1
        substringStarting = 0

        for i in range(len(s)):
            if lastSeen[ord(s[i]) - ord('a')] >= substringStarting:
                count += 1
                substringStarting = i
            lastSeen[ord(s[i]) - ord('a')] = i

        return count

"""
https://leetcode.com/problems/optimal-partition-of-string/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
"""