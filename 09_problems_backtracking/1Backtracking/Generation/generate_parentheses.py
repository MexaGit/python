from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []  # This will store all valid combinations of parentheses.

        def backtracking(cur_string, left_count, right_count):
            # If the current string's length is equal to 2*n,
            # it means we have a valid combination of parentheses.
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))  # Add the valid combination to the answer list.
                return

            # If we can still add a left parenthesis '('
            if left_count < n:
                cur_string.append("(")  # Add a left parenthesis
                # Recur with updated counts: one more left parenthesis added
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()  # Backtrack: remove the last added '('

            # We can add a right parenthesis ')' only if there are left parentheses to match it.
            if right_count < left_count:
                cur_string.append(")")  # Add a right parenthesis
                # Recur with updated counts: one more right parenthesis added
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()  # Backtrack: remove the last added ')'

        # Start the backtracking process with an empty string and counts set to 0.
        backtracking([], 0, 0)
        return answer  # Return the list of all valid combinations


# Example Test Cases
# Test Case 1: Generate 3 pairs of parentheses
print(Solution().generateParenthesis(3))
# Expected Output: ["((()))","(()())","(())()","()(())","()()()"]

# Test Case 2: Generate 1 pair of parentheses
print(Solution().generateParenthesis(1))
# Expected Output: ["()"]

# Test Case 3: Generate 2 pairs of parentheses
print(Solution().generateParenthesis(2))
# Expected Output: ["(())","()()"]


"""
https://leetcode.com/problems/generate-parentheses/description/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#-------------------------------------------------------------------------------------------#

Approach 2: Backtracking, Keep Candidate Valid
Intuition
If you are not familiar with backtracking, you can refer to our Backtracking Explore Card for more information.

The previous approach of generating all possible strings of length 2n and checking each one is simple but inefficient, 
as it generates many invalid strings that must be checked.

A better approach is to use backtracking to generate only valid strings. This involves recursively building strings of 
length 2n and checking their validity as we go. In case the current string is invalid, we will not continue the 
recursive process on it. Instead, we will backtrack to the previous valid string on the recursive path. This approach 
allows us to focus only on generating valid strings, thus saving us time and resources. We continue the recursion only 
on the valid strings until we reach the ones of length 2n.

As shown in the picture below: ) is an invalid string, so every string prefixed with it is also invalid, and we can 
just drop it.

img

To ensure that the current string is always valid during the backtracking process, we need two variables left_count 
and right_count that record the number of left and right parentheses in it, respectively.

Therefore, we can define our backtracking function as backtracking(cur_string, left_count, right_count) that takes 
the current string, the number of left parentheses, and the number of right parentheses as arguments. This function 
will build valid combinations of parentheses of length 2n recursively.

The function adds more parentheses to cur_string only when certain conditions are met:
    If left_count < n, it suggests that a left parenthesis can still be added, so we add one left parenthesis to }
    cur_string, creating a new string new_string = cur_string + (, and then call backtracking(new_string, 
    left_count + 1, right_count).
    If left_count > right_count, it suggests that a right parenthesis can be added to match a previous unmatched left 
    parenthesis, so we add one right parenthesis to cur_string, creating a new string new_string = cur_string + ), and 
    then call backtracking(new_string, left_count, right_count + 1).

This function ensures that the generated string of length 2n is valid, and adds it directly to the answer. By only 
generating valid strings, we can avoid wasting time checking invalid strings.

Algorithm
1. Initialize an empty list answer to store the valid strings.
2. Define backtracking(cur_string, left_count, right_count) to generate valid strings recursively.
    If len(cur_string) = 2n, add it to answer and return.   If left_count < n, add ( to cur_string and move on to 
    backtracking(new_string, left_count + 1, right_count).
    If left_count > right_count, add ) to cur_string and move on to backtracking(new_string, 
    left_count, right_count + 1).
3. Call backtracking on empty string (backtracking("", 0, 0)) and return answer once the backtracking process is 
complete.
"""