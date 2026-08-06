class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)  # Length of the strings
        max_len = 0  # Maximum length of the valid substring found
        start = 0  # Starting index of the current window (substring)
        curr_cost = 0  # Current total cost of converting substring s[start:i] into t[start:i]

        # Iterate through the characters of s and t
        for i in range(N):
            # Calculate the cost to convert s[i] to t[i]
            # ord() is a built-in Python function that returns the Unicode (ASCII) code of a character.
            # Each character in a string has a corresponding integer value based on its Unicode code point.
            # abs() stands for absolute value, which removes the negative sign from a number, ensuring the result is
            # always positive.
            curr_cost += abs(ord(s[i]) - ord(t[i]))

            # If the current cost exceeds maxCost, shrink the window from the left
            while curr_cost > maxCost:
                # Subtract the cost of converting s[start] to t[start] as we slide the window
                # before while (5 = s[i] - t[i]) -= (5 = after while s[start] - t[start])
                # curr_cost = 0
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1  # Move the start of the window to the right

            # Update the maximum length of the valid substring found so far
            max_len = max(max_len, i - start + 1)

        return max_len  # Return the maximum length of the valid substring

# Example usage
solution = Solution()
"""
Strings:
s = "a" "b" "c" "d"
t = "f" "b" "c" "d"

Costs:
a to f: |97 - 102| = 5
b to b: |98 - 98| = 0
c to c: |99 - 99| = 0
d to d: |100 - 100| = 0

Window	Characters	Total Cost	Max Cost	Valid?	Max Length
[0,0]	"a"	        5	        3	        No	    0
[1,1]	"b"	        0	        3	        Yes	    1
[1,2]	"bc"	    0	        3	        Yes	    2
[1,3]	"bcd"	    0	        3	        Yes	    3
"""

print(solution.equalSubstring("abcd", "fbcd", 3))  # Output: 3

"""
maxCost = 3.
Iteration (i)	Current Characters	Cost Calculation	    Current Cost	Status	        Start Index	Max Length
0	            'a' to 'c'		                            97 - 99	        = 2	            2	        Valid (2 ≤ 3)
1	            'b' to 'd'		                            98 - 100	    = 2	            4	        Exceeds (4 > 3)
                                    Remove cost for 'a'	    4 - 2 = 2	    Valid (2 ≤ 3)	1	        1
2	            'c' to 'e'		                            99 - 101	    = 2	            4	        Exceeds (4 > 3)
                                    Remove cost for 'b'	    4 - 2 = 2	    Valid (2 ≤ 3)	2	        1
3	            'd' to 'f'		                            100 - 102	    = 2	            4	        Exceeds (4 > 3)
                                    Remove cost for 'c'	    4 - 2 = 2	    Valid (2 ≤ 3)	3	        1
"""
print(solution.equalSubstring("abcd", "cdef", 3))  # Output: 1
print(solution.equalSubstring("abcd", "acde", 0))  # Output: 1

"""
Time Complexity of equalSubstring:

Loop through the characters in s and t:
The function iterates through each character in the strings s and t using a for loop. If the length of the strings 
is N, this loop runs exactly N times, giving a time complexity of O(N).

Calculating the cost:
For each character, the algorithm calculates the absolute difference between the corresponding characters in s and t 
using abs(ord(s[i]) - ord(t[i])). This is a constant time operation, O(1).

Sliding window adjustment:
The while loop adjusts the window (substring) if the current cost exceeds maxCost. In the worst case, the window may 
shrink to a single character. However, both the for and while loops together process each character at most once, 
making this part of the algorithm also O(N).
Since each character is processed at most twice (once when expanding the window and once when shrinking it), 
the overall time complexity is O(N).

Space Complexity of equalSubstring:

Constant space for variables:
The function uses a fixed number of variables (N, max_len, start, curr_cost), which all take constant space O(1).

Input strings:
The input strings s and t are provided as input and are not modified or duplicated. Thus, the space required by the 
input is O(N), but this doesn't contribute to the additional space used by the algorithm.
Therefore, the overall space complexity is O(1), as the algorithm only uses a constant amount of extra space beyond 
the input.
"""