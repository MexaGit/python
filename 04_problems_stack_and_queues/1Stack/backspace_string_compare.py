class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Define a helper function to process each string with backspaces
        def build(s):
            # Initialize an empty stack to process the characters of the string
            stack = []

            # Loop through each character in the string
            for c in s:
                if c != "#":
                    # If the character is not a backspace ("#"), add it to the stack
                    stack.append(c)
                elif stack:
                    # If the character is a backspace and the stack is not empty, remove the last character
                    stack.pop()

            # After processing the string, return the final result as a string (by joining the stack)
            return "".join(stack)

        # Compare the final processed versions of both strings
        print(build(s), build(t))
        return build(s) == build(t)

# Create an instance of the Solution class
sol = Solution()
# Test case 1: Simple case with no backspaces
print(sol.backspaceCompare("abc", "abc"))  # Expected output: True
# Test case 2: Case with backspaces resulting in the same string
print(sol.backspaceCompare("ab#c", "ad#c"))  # Expected output: True
# Test case 3: Case with backspaces removing characters completely
print(sol.backspaceCompare("ab##", "c#d#"))  # Expected output: True



"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.
For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings
are both equal to "ac".

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true

Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true

Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false

Explanation: s becomes "c" while t becomes "b".
"""