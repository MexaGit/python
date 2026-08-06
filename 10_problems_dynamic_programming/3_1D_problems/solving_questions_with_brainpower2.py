from typing import List

class Solution:
    # bottom-up implementation
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # n + 1 to avoid out of bounds

        for i in range(n - 1, -1, -1):
            j = i + questions[i][1] + 1
            # need to make sure we don't go out of bounds
            dp[i] = max(questions[i][0] + dp[min(j, n)], dp[i + 1])

        return dp[0]

# Test cases
solution = Solution()

# Test case 1:
questions1 = [[3, 2], [4, 3], [4, 4], [2, 5]]
# Explanation: Choose the first question (3 points), skip the next 2, choose the last question (2 points)
# Total points = 3 + 2 = 5
# Explanation: The maximum points can be earned by solving questions 0 and 3.
# - Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
# - Unable to solve questions 1 and 2
# - Solve question 3: Earn 2 points
# Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
print(solution.mostPoints(questions1))  # Output: 5

# Test case 2:
questions2 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
# Explanation: The maximum points can be earned by solving questions 1 and 4.
# - Skip question 0
# - Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
# - Unable to solve questions 2 and 3
# - Solve question 4: Earn 5 points
# Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
# Total points = 1 + 2 + 3 + 4 = 10
print(solution.mostPoints(questions2))  # Output: 10