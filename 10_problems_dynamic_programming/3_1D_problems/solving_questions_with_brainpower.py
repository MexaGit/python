from functools import cache
from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Memoization using @cache to store the results of subproblems and avoid recomputation
        @cache
        def dp(i):
            # Base case: if the index exceeds the last question, no more points can be collected
            if i >= len(questions):
                return 0

            # j represents the next question that can be answered after skipping `questions[i][1]` questions.
            # i + questions[i][1] + 1 ensures that we follow the constraint of the cooldown.
            j = i + questions[i][1] + 1

            # The maximum points can be obtained by either:
            # 1. Solving the current question (questions[i][0]) and moving to the next valid question dp(j).
            # 2. Skipping the current question and moving to the next question dp(i + 1).
            return max(questions[i][0] + dp(j), dp(i + 1))

        return dp(0)


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

"""
https://leetcode.com/problems/solving-questions-with-brainpower/description/
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order
(i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will
earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i,
you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
    If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
    If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve
    questions 2 and 3.
Return the maximum points you can earn for the exam.

#-------------------------------------------------------------------------------------------#

Overview
First, we provide an example in the picture below. Note that questions[0] = [points_0, brainpower_0] = [3, 2], d
so if we solve the first question, we can earn 3 points and have to skip at least 2 following questions.
"""