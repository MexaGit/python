from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        # Since 'l' and 'o' appear twice in "balloon", divide their counts by 2
        counts['l'] = counts.get('l', 0) // 2
        counts['o'] = counts.get('o', 0) // 2
        # List of required characters
        required_chars = ['b', 'a', 'l', 'o', 'n']
        # Find the minimum count among the required characters
        return min(counts.get(char, 0) for char in required_chars)

# Example usage:
solution = Solution()
input_text = "loonbalxballpoon"
print(solution.maxNumberOfBalloons(input_text))  # Output: 2

"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon"
as possible. You can use each character in text at most once. Return the maximum number of instances that
can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2
"""