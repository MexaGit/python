class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0  # Initialize two pointers for strings s and t

        # Iterate through both strings until we reach the end of either
        while i < len(s) and j < len(t):
            # If characters match, move the pointer in s
            if s[i] == t[j]:
                i += 1  # Move the pointer for s forward
            j += 1  # Always move the pointer for t forward

        # Check if we have traversed all characters in s
        return i == len(s)  # Return True if all characters in s were found in t

# Example usage
solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))  # Output: True
print(solution.isSubsequence("axc", "ahbgdreccx"))  # Output: False

"""
Time Complexity: O(n), where n is the length of string t. In the worst case, we may need to iterate 
through all characters of t.
Space Complexity: O(1) since no additional space is used that scales with the input size.
"""