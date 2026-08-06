from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    start_idx = 0  # To store the starting index of the longest substring

    for right in range(len(s)):
        counts[s[right]] += 1
        print(counts)

        # Shrink the window if we have more than k distinct characters
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        # If we found a longer valid substring, update the answer and track its start
        if right - left + 1 > ans:
            ans = right - left + 1
            start_idx = left

    # Return both the length and the substring
    return ans, s[start_idx:start_idx + ans]


# Example usage
result_length, result_substring = find_longest_substring("eceaabddddde", 2)
print(f"Length: {result_length}, Substring: '{result_substring}'")

"""
Example 1: You are given a string s and an integer k. Find the length of the longest substring 
that contains at most k distinct characters.
For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters 
is "ece".
"""
