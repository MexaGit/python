class Solution:
    def makePalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        cnt = 0
        while l < r:
            if s[l] != s[r]:
                cnt += 1
                if cnt > 2:
                    return False
            l += 1
            r -= 1
        return True
"""
https://leetcode.com/problems/valid-palindrome-iv/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Example 1:

Input: s = "abcdba"
Output: true
Explanation: One way to make s a palindrome using 1 operation is:
- Change s[2] to 'd'. Now, s = "abddba".
One operation could be performed to make s a palindrome so return true.
"""