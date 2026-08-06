from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack to hold the indices of the temperature array
        stack = []
        # Initialize the answer list with zeros, same length as temperatures
        answer = [0] * len(temperatures)

        # Iterate over the temperatures
        for i in range(len(temperatures)):
            # While there are indices in the stack and the current temperature is higher
            # than the temperature at the index stored at the top of the stack
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # Pop the index from the stack
                j = stack.pop()
                # Calculate the number of days until a warmer temperature and store it
                answer[j] = i - j
            # Push the current index onto the stack
            stack.append(i)

        return answer

# Test case where temperatures are consistently increasing
# Input: temperatures = [70, 71, 72, 73, 74]
# Expected Output: [1, 1, 1, 1, 0]
# Explanation:
# Day 0 (70) → warmer on day 1 (71) → 1 day until warmer
# Day 1 (71) → warmer on day 2 (72) → 1 day until warmer
# Day 2 (72) → warmer on day 3 (73) → 1 day until warmer
# Day 3 (73) → warmer on day 4 (74) → 1 day until warmer
# Day 4 (74) → no warmer days ahead → 0 days

solution = Solution()
print(solution.dailyTemperatures([70, 71, 72, 73, 74]))  # Output: [1, 1, 1, 1, 0]

# Test case with mixed temperatures
# Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Expected Output: [1, 1, 4, 2, 1, 1, 0, 0]
# Explanation:
# Day 0 (73) → warmer on day 1 (74) → 1 day
# Day 1 (74) → warmer on day 2 (75) → 1 day
# Day 2 (75) → warmer on day 6 (76) → 4 days
# Day 3 (71) → warmer on day 5 (72) → 2 days
# Day 4 (69) → warmer on day 6 (72) → 1 day
# Day 5 (72) → warmer on day 6 (76) → 1 day
# Day 6 (76) → no warmer days ahead → 0 days
# Day 7 (73) → no warmer days ahead → 0 days

solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]

"""
Given an array of integers temperatures represents the daily temperatures, return an array answer
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]}

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""