def check_if_palindrome(s: str) -> bool:
    left = 0  # Initialize the left pointer at the start of the string
    right = len(s) - 1  # Initialize the right pointer at the end of the string

    # Continue comparing characters until the two pointers meet
    while left < right:
        # If characters at left and right pointers do not match, it's not a palindrome
        if s[left] != s[right]:
            return False  # Return False immediately if mismatch is found
        left += 1  # Move the left pointer to the right
        right -= 1  # Move the right pointer to the left

    return True  # If all characters matched, return True

# Example usage
print(check_if_palindrome("racecar"))  # Output: True
print(check_if_palindrome("hello"))    # Output: False

"""
Time Complexity:

The time complexity is O(n), where n is the length of the string. The function makes a single pass through half
of the string.

Space Complexity:

The space complexity is O(1) since the function uses a constant amount of space for the pointers and does not create 
any additional data structures that scale with input size.
"""