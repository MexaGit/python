def reverseOnlyLetters(S: str) -> str:
    # Convert the input string to a list for easier manipulation
    S = list(S)
    left, right = 0, len(S) - 1  # Initialize two pointers

    # Loop until the left pointer meets the right pointer
    while left < right:
        # Move the left pointer to the right until it finds a letter
        while left < right and not S[left].isalpha():
            left += 1

        # Move the right pointer to the left until it finds a letter
        while left < right and not S[right].isalpha():
            right -= 1

        # Swap the letters at the left and right pointers
        if left < right:  # Ensure pointers haven't crossed
            S[left], S[right] = S[right], S[left]
            left += 1  # Move left pointer to the right
            right -= 1  # Move right pointer to the left

    # Convert the list back to a string and return it
    return ''.join(S)


# Example usage
print(reverseOnlyLetters("Qedo1ct-eeLg=ntse-T!"))  # Output: "Te-s1Lg-cdeon-Q!"

"""
Time Complexity of reverseOnlyLetters:

Two-pointer traversal:
The algorithm uses two pointers (left and right) to traverse the string from both ends, moving towards the center. 
In the worst case, each pointer traverses the entire string. This results in a time complexity of O(n), where n 
is the length of the string S.

Character checks:
Each iteration of the while loop includes checking if a character is a letter using the isalpha() function, which is 
a constant time operation O(1). Even though there are inner while loops, the total number of operations remains 
proportional to n because each pointer moves through the string only once.

Swapping letters:
Swapping two characters (letters) is a constant time operation, taking O(1). Since the number of swaps is bounded 
by n/2 (at most), this doesn’t affect the overall time complexity beyond O(n).
Converting the list back to a string:

After processing the list, it is converted back to a string using ''.join(S), which also takes O(n) time because 
it concatenates all n characters.
Thus, the overall time complexity is O(n).

Space Complexity of reverseOnlyLetters:

Space for the list:
The input string S is converted to a list, which requires O(n) space because each character from the original string 
is stored in a list.

Additional variables:
The algorithm uses two pointers (left and right), which take constant space O(1).
Therefore, the space complexity is O(n) due to the creation of the list representation of the string.
"""