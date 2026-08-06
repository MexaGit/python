class Solution:
    def numberOfWays(self, s):
        n = len(s)

        # Arrays to store count of '0's and '1's up to the current index
        count_0_before = [0] * n
        count_1_before = [0] * n

        count_0 = 0
        count_1 = 0

        # Traverse the string to fill the count arrays
        for i in range(n):
            if s[i] == '0':
                count_0 += 1
            else:
                count_1 += 1
            count_0_before[i] = count_0
            count_1_before[i] = count_1

        total_valid_selections = 0

        # Now traverse the string again and for each building, check how many valid patterns it can form
        for i in range(1, n - 1):
            if s[i] == '1':  # We're looking for '010' pattern
                total_valid_selections += count_0_before[i - 1] * (count_0_before[n - 1] - count_0_before[i])
            else:  # We're looking for '101' pattern
                total_valid_selections += count_1_before[i - 1] * (count_1_before[n - 1] - count_1_before[i])

        return total_valid_selections

"""
https://leetcode.com/problems/number-of-ways-to-select-buildings/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Example 1:

Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
"""