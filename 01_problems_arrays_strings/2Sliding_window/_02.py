def find_length(s):
    # curr is the current number of zeros in the window
    left = curr = ans = 0  # Initialize left pointer, current zero count, and answer variable

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # Increment curr if the current character is '0'
        if s[right] == "0":
            curr += 1

        # While there are more than 1 zero in the window, shrink the window from the left
        while curr > 1:
            if s[left] == "0":
                curr -= 1  # Decrease the zero count if the left character is '0'
            left += 1  # Move the left pointer to the right

        # Update the answer with the maximum length of the valid window found
        ans = max(ans, right - left + 1)

    return ans  # Return the maximum length of the subarray found

# Example usage
print(find_length("110100110"))  # Output: 4 (subarray "1101")
print(find_length("000111"))     # Output: 4 (subarray "0111")
print(find_length("101"))        # Output: 3 (subarray "101")

"""
Time Complexity: O(n), where n is the length of the input string s. Each character is processed at most twice
(once by the right pointer and once by the left pointer).

Space Complexity: O(1) since no additional space is used that scales with the input size.
"""