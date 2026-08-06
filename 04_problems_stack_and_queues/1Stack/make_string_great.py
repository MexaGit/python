class Solution:
    def makeGood(self, s: str) -> str:
        # Use stack to store the visited characters.
        stack = []

        # Iterate over 's'.
        # Difference:
        # for x in s: directly iterates over the string.
        # for x in list(s): converts the string into a list
        # (which is an unnecessary step in most cases).
        for curr_char in list(s):
            # If the current character make a pair with the last character in the stack,
            # remove both of them. Otherwise, we add the current character to stack.
            # ord() is a Python function that returns the Unicode (ASCII) value of a character.
            # abs() function return the absolute value
            """
            Why 32? In the ASCII table, the difference between a lowercase letter and its
            corresponding uppercase letter is exactly 32. For example:
                ord('a') - ord('A') = 97 - 65 = 32
                ord('b') - ord('B') = 98 - 66 = 32
            """
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr_char)

        # Returns the string concatenated by all characters left in the stack.
        return "".join(stack)

# Input string: "leEeetcode"
# Expected output: "leetcode"

solution = Solution()
s = "leEeetcode"
print(solution.makeGood(s))  # Output: "leetcode"
e = "abBAcC"
print(solution.makeGood(e))  # Output: ""

"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them.
You can keep doing this until the string becomes good.
Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"

Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode"
to be reduced to "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""

Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
"""