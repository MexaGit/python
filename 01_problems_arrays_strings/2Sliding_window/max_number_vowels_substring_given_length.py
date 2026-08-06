class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Why a set?
        Quick lookup: A set provides O(1) time complexity for membership tests. This makes it much faster to check
        if a character is a vowel compared to using a list or a string, which would have O(n) lookup time.
        No duplicates: Sets inherently store only unique elements, so even if a vowel were repeated, it would
        only appear once in the set.
        """
        vowels = set('aeiou')  # Set of vowels for quick lookup
        current_vowel_count = 0  # Count of vowels in the current window

        # Step 1: Initialize the first window
        for i in range(k):
            if s[i] in vowels:
                current_vowel_count += 1

        max_vowel_count = current_vowel_count  # Set the max to the first window count

        # Step 2: Slide the window over the string
        for i in range(k, len(s)):
            # Add the next character in the window
            if s[i] in vowels:
                current_vowel_count += 1

            # Remove the character that's sliding out of the window
            if s[i - k] in vowels:
                current_vowel_count -= 1

            # Update the maximum vowel count found
            max_vowel_count = max(max_vowel_count, current_vowel_count)

        return max_vowel_count

# Example usage
solution = Solution()
print(solution.maxVowels("abciiidef", 3))  # Output: 3
print(solution.maxVowels("aeiou", 2))  # Output: 2
print(solution.maxVowels("leetcode", 3))  # Output: 2

"""
Time Complexity of maxVowels:

Initializing the first window:
The first for loop initializes the vowel count for the first k characters of the string s. This loop runs k times, 
giving it a time complexity of O(k).

Sliding the window:
The second for loop slides the window across the rest of the string, which processes the remaining n - k characters 
(where n is the length of s). This loop runs O(n - k), which simplifies to O(n) since it essentially covers the entire 
string after the initial window.

Total complexity:
The overall time complexity is dominated by the second loop, resulting in a total time complexity of O(n).

Space Complexity of maxVowels:

Space for the set of vowels:
The algorithm uses a set of vowels, which takes up constant space since it contains a fixed number of characters 
(5 vowels: 'a', 'e', 'i', 'o', 'u'). This space is O(1).

Other variables:
The function uses a few additional integer variables (max_vowel_count, current_vowel_count), which also take constant 
space O(1).
Therefore, the overall space complexity is O(1), as the algorithm does not use any additional data structures that 
scale with the input size.
"""