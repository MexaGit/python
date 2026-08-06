class Solution:
    # Bottom-up
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

# Test cases
solution = Solution()

# Test case 1: text1 = "abcde", text2 = "ace"
text1_1 = "abcde"
text2_1 = "ace"
# The longest common subsequence is "ace", so output should be 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
print(solution.longestCommonSubsequence(text1_1, text2_1))  # Output: 3

# Test case 2: text1 = "abc", text2 = "def"
text1_2 = "abc"
text2_2 = "def"
# There are no common subsequences, so output should be 0
print(solution.longestCommonSubsequence(text1_2, text2_2))  # Output: 0
# Explanation: There is no such common subsequence, so the result is 0.