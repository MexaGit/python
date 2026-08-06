class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Step 1: Initialize pointers
        left = 0
        # Step 2: Find the index of the character ch
        while left < len(word) and word[left] != ch:
            left += 1

        # Step 3: If ch is found, reverse the prefix up to and including ch
        if left < len(word):  # ch was found
            # Reverse the prefix using slicing and concatenate the rest of the string
            # left is 3 but d is on index 4 so left + 1, take all from [start:left +1] and
            # reverse all from there [::-1] will be dcba + [left + 1] = dcba + efd
            return word[:left + 1][::-1] + word[left + 1:]

        # If ch is not found, return the original word
        return word

# Example usage
solution = Solution()
print(solution.reversePrefix("abcdefd", "d"))  # Output: "dcbaefd"
print(solution.reversePrefix("abcdefd", "x"))  # Output: "abcdefd"

"""
Time Complexity:

Finding the index of ch:
The while loop traverses the word string to find the index of the character ch. In the worst case, it may need to scan 
the entire string. If the length of the string is n, this operation takes O(n) time.

Reversing the prefix:
If the character ch is found, the prefix (substring up to and including the character ch) is reversed using slicing 
(word[:left + 1][::-1]). Slicing and reversing take O(k) time, where k is the length of the prefix. In the worst case, 
k can be n, so this operation also takes O(n).

Concatenating the remaining string:
Concatenating the reversed prefix with the remaining part of the string takes O(n - k) time, where n - k is the length 
of the remaining part. In the worst case, this can be O(n).
Thus, the overall time complexity is dominated by the O(n) operations. Hence, the total time complexity is O(n).

Space Complexity:

Space for storing the prefix:
When slicing and reversing the prefix, a new string is created. The size of this new string can be at most n in the 
worst case (if ch is at the end of the string).

Concatenation:
The concatenation of two substrings also creates a new string of size n.
No additional data structures are used beyond these temporary strings.
Thus, the space complexity is O(n) due to the creation of new strings during slicing and concatenation.

What is O(n) in Big O Notation?
O(n) represents the time complexity of an algorithm, where n is the size of the input (e.g., the length of a list or 
string). When an algorithm is said to have O(n) complexity, it means that the time it takes to run the algorithm grows 
linearly with the size of the input.

Key Characteristics of O(n):
Linear Growth: If the input size increases, the execution time increases proportionally.
Scalability: O(n) algorithms handle small and large inputs well, though large input sizes may still cause slowdowns 
because the time increases linearly.
Common in Practice: Many efficient algorithms are designed to run in O(n) time, such as linear search, single loop 
traversals, or algorithms that process each element of a list once.
"""