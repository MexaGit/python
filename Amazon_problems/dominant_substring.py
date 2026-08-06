from collections import defaultdict

def is_dominant_exact_half(substring):
    # Create a frequency dictionary
    freq = defaultdict(int)

    # Count the frequency of each character
    for char in substring:
        freq[char] += 1

    # Get the length of the substring
    length = len(substring)

    # Check if any character appears exactly length/2 times
    half_length = length // 2
    for char, count in freq.items():
        if count == half_length:
            return True

    return False

def extract_longest_dominant_even_substring(s):
    n = len(s)
    max_len = 0  # Variable to store the maximum length

    # Iterate over every possible starting point
    for start in range(n):
        # Check each possible substring from `start` with even length
        for end in range(start + 2, n + 1, 2):  # Step by 2 to ensure even length
            substring = s[start:end]
            if is_dominant_exact_half(substring):
                max_len = max(max_len, len(substring))

    return max_len


# Test case
s = "addiffft"
result = extract_longest_dominant_even_substring(s)

print(result)  # Expected output: 6
