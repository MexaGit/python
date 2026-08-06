from collections import deque
from tkinter import Listbox
from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # Initialize a queue to perform BFS starting from 'start', with step count 0
        queue = deque([(start, 0)])
        # Keep track of visited nodes to avoid reprocessing
        seen = {start}

        while queue:
            # Get the current node (mutation string) and the number of steps
            node, steps = queue.popleft()

            # If the current node matches the end, return the number of steps
            if node == end:
                return steps

            # Generate all possible mutations by changing each character to A, C, G, or T
            for c in "ACGT":
                for i in range(len(node)):
                    # Generate a neighbor mutation by changing one character
                    neighbor = node[:i] + c + node[i + 1:]

                    # If the neighbor mutation is valid and not seen, process it
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)  # Mark as seen to avoid loops

        # If no mutation path was found, return -1
        return -1

# Test case 1
start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
print(Solution().minMutation(start, end, bank))  # Output: 1

# Test case 2
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(Solution().minMutation(start, end, bank))  # Output: 2

"""
https://leetcode.com/problems/minimum-genetic-mutation/description/
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is
defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid
gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed
to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

#-------------------------------------------------------------------------------------------------#

Approach: BFS (Breadth-First Search)
Intuition

We can imagine the problem as a graph. Each gene string is a node, and mutations are the edges. Two nodes have an edge 
(are neighbors) if they differ by one character. The added constraints are that the characters must be one of "ACGT", 
and each node must be in bank.
Then, the problem is simplified: what is the shortest path between start and end? When a graph problem involves finding 
a shortest path, BFS should be used over DFS. This is because with BFS, all nodes at distance x from start will be 
visited before any node at distance x + 1 will be visited. Once we find the target (end), we know that we found it in 
the shortest number of steps possible.

Algorithm
Perform a BFS starting from node start. Keep track of the number of steps taken so far and return that number of steps 
when we find end. Only traverse to nodes that are in bank. Neighbors can be found by iterating over each node and 
replacing one of the characters with a character from "ACGT".

To check if a node is in bank, we would normally first convert bank to a set to have O(1) checking. However, the 
problem's constraints state that 0 <= bank.length <= 10. With such a small constraint, it may actually be slower 
to use a set due to the overhead associated with hashing. Therefore, we will keep bank as an array.

Initialize a queue queue and a set seen. The queue will be used for BFS and the set will be used to prevent visiting 
a node more than once. Initially, the queue and set should hold start.

Perform a BFS. At each node, if node == end, return the number of steps so far. Otherwise, iterate over all the 
neighbors. For each neighbor, if neighbor is not in seen and neighbor is in bank, add it to queue and seen.

If we finish the BFS and did not find end, then the task is impossible. Return -1.
"""