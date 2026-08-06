from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Number of projects
        n = len(profits)
        # Combine capital and profits and sort projects by capital required
        projects = sorted(zip(capital, profits))
        # Max heap to store profits of projects we can afford
        heap = []
        # Index for traversing the sorted projects
        i = 0

        # Perform at most k projects
        for _ in range(k):
            # Add all projects that we can afford to the max heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])  # Use negative to simulate max heap
                i += 1
            if len(heap) == 0:
                # If no projects can be done, return current capital
                return w
            # Take the project with the maximum profit
            w -= heapq.heappop(heap)  # Subtracting negative gives us the profit
        return w

# Test cases

# Example 1:
solution = Solution()

# Input: k = 2, w = 0, profits = [1, 2, 3], capital = [0, 1, 1]
# Output: 3
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project indexed 2.
# Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
k2 = 2
w2 = 0
profits2 = [1, 2, 3]

capital2 = [0, 1, 1]
print(solution.findMaximizedCapital(k2, w2, profits2, capital2))  # Output: 4

"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode
would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can
only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital
after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is
needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added
to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final
maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

#--------------------------------------------------------------------------------------#

A Greedy Approach
Intuition
When you don't know how to solve the problem completely, think of its simpler subproblems.

Consider a particular case k=1. What project is the best to choose when we can finish only one? We want the one that 
yields the maximum profit. However, the choice is constrained – the project is available only if it requires capital 
that is not larger than our initial capital. Thus the optimal project is the most profitable among those for which we 
have enough money to start. If no project is available, we don't have the option to begin any, and the answer is 0.

It can be generalized for arbitrary k. First, we greedily choose the most profitable available project. Then our capital
increases by the profit of this project, and some new projects that were unavailable before might become available now. 
If we choose a project other than the most profitable one, our capital increases by a value less than the maximum 
possible, and fewer new options become available. It means we should greedily choose the maximum profit every time. 
We can repeat this process of choosing the most profitable project and then updating the projects we can afford until 
we finish k projects or cannot afford any new ones.

Now the problem breaks into two parts: finding new available projects after finishing the previous one and finding the 
most profitable available project.

To handle the first part, we make the following observation: when our capital grows, we have more options to 
choose from, and the smaller capital a project requires, the sooner it becomes available. Thus we can sort the projects
by increasing capital and keep a pointer to the first unavailable project. As we gain more money, we can increment 
this pointer to unlock more projects.

For the second part of the problem, we need a data structure for maintaining available projects that can perform the 
following operations:
    insert an element (for adding a new available project),
    get the maximum element (for choosing the best project),
    delete the maximum element (for finishing the best project).
    
The data structure with the above properties is a priority queue. The priority of a project is its profit.

It leads us to the following algorithm.

Algorithm
1. Sort the projects by increasing capital. Keep a pointer ptr to the first unavailable project in the sorted array.
2. Maintain a priority queue for the profits of available projects. Initially, the priority queue is empty.
3. Do the following k times:
    Add to the priority queue the profits of the newly available projects. We move the pointer through the sorted 
    array when new projects become available.
    If the priority queue is empty, terminate the algorithm.
    The maximum value in the priority queue is the profit of the project we will start now. Increase our capital 
    by this value. Delete it so since we can not use it anymore.
"""