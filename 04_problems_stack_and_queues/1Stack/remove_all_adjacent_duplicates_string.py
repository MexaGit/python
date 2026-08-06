class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Initialize an empty stack to store characters
        stack = []

        # Loop through each character in the string
        for c in s:
            # If the stack is not empty and the top of the stack is the same as the current character
            # is the same as the current character (c), this means there's a duplicate
            if stack and stack[-1] == c:
                # Remove (pop) the last character from the stack (since it's a duplicate)
                stack.pop()
            else:
                # If no duplicate, add the current character to the stack
                stack.append(c)

        # After processing the string, join the stack into a final string and return it
        return "".join(stack)

# Create an instance of the Solution class
sol = Solution()

# Test case 1: Basic case with consecutive duplicates
print(sol.removeDuplicates("abbaca"))  # Expected output: "ca"
# Test case 2: No duplicates
print(sol.removeDuplicates("abcdef"))  # Expected output: "abcdef"
# Test case 3: Entire string is duplicates
print(sol.removeDuplicates("aaaa"))  # Expected output: "" (empty string because all characters are removed)
"""
You are given a string s consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"

Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal,
and this is the only possible move.  The result of this move is that the string is "aaca",
of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"
"""