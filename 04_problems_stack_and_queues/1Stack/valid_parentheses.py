class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of unmatched opening brackets
        stack = []
        matching = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            # If it's an opening bracket (one of the keys in the dictionary)
            if c in matching:
                # Push (add) the opening bracket to the stack
                stack.append(c)
            else:
                # If it's a closing bracket but the stack is empty, it means there's no matching opening bracket
                if not stack:
                    return False  # The string is invalid

                # Pop (remove) the most recent opening bracket from the stack
                previous_opening = stack.pop()

                # Check if the closing bracket matches the most recent opening bracket
                # If it doesn't match, the string is invalid
                if matching[previous_opening] != c:
                    return False

        # In the end, if the stack is empty, all opening brackets had matching closing brackets
        # If the stack still has items, it means there are unmatched opening brackets, so it's invalid
        return not stack


# Create an instance of the Solution class
sol = Solution()

print(sol.isValid("()[]{}"))  # Expected output: True
print(sol.isValid("(]"))  # Expected output: False
print(sol.isValid("{[]}"))  # Expected output: True
print(sol.isValid(""))  # Expected output: True

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The string is valid if all open brackets are closed by the same type of closing bracket in the correct order,
and each closing bracket closes exactly one open bracket.
For example, s = "({})" and s = "(){}[]" are valid, but s = "(]" and s = "({)}" are not valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""