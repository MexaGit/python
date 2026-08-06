from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            # Base case: If we reach the end of either string, no more characters to compare
            if i == len(text1) or j == len(text2):
                return 0

            # If the characters match, move to the next characters in both strings
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)

            # If the characters don't match, explore both possibilities:
            # 1. Move to the next character in text1
            # 2. Move to the next character in text2
            return max(dp(i + 1, j), dp(i, j + 1))

        # Start the dynamic programming recursion from the start of both strings
        return dp(0, 0)

"""
https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
"""