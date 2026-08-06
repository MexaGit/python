from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()  # Initialize a Counter to keep track of character frequencies in the current window

        left = right = 0  # Two pointers for the sliding window
        res = 0  # Result variable to store the maximum length of the substring found

        # Loop until the right pointer reaches the end of the string
        while right < len(s):
            r = s[right]  # Current character at the right pointer
            chars[r] += 1  # Increment the count of the current character

            # While there are duplicate characters in the current window
            #  In Counter, the order of the elements is based on the order of their first appearance in the input
            #  sequence, but their counts accumulate as they are encountered again.
            while chars[r] > 1:
                l = s[left]  # Character at the left pointer
                chars[l] -= 1  # Decrement the count of the left character
                left += 1  # Move the left pointer to the right to reduce the window size

            # Update the result with the maximum length found
            res = max(res, right - left + 1)
            print(chars)
            """
            Key reason for placing right += 1 after the while loop:
            By delaying the increment of right, we ensure that every position of the right pointer is fully processed
            (including handling any duplicates) before moving on to the next character. If we moved right too early 
            (inside the loop), we would miss handling the current character correctly. Thus, placing right += 1 
            after the while loop guarantees that the current window is valid and fully processed before moving 
            to the next character.
            """
            right += 1  # Move the right pointer to expand the window
        return res  # Return the maximum length of the substring without repeating characters


    # Sliding Window Optimized
    def lengthOfLongestSubstring1(self, s: str) -> int:
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index is not None and left <= index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res

solution = Solution()
print(solution.lengthOfLongestSubstring("abcdeafbdgcbb")) # eafbdgc [4,10]
# Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1})

"""
Counter is a part of Python's collections module. It helps to count the frequency of elements in a collection 
(like a list or string). In this case, it will count how many times each character appears in the current window 
of the substring.

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcdeafbdgcbb"
Output: 7

Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1

Explanation: The answer is "b", with the length of 1.
"""