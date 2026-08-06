from collections import deque  # Importing a "queue" to explore nodes level by level
from typing import List  # Helps define lists nicely in Python


# Step 1: Define the 'TreeNode' class to represent each person (node) in the family tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Each node (person) has a value (their name or number)
        self.left = left  # Points to the left child (left family branch)
        self.right = right  # Points to the right child (right family branch)
        self.parent = None  # We'll fill this later with the parent node


# Step 2: Define the Solution class with the function to find nodes k-distance away
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        # A. DFS Step: Mark every node with its parent
        def dfs(node, parent):
            if not node:  # If there’s no node here, stop.
                return

            node.parent = parent  # Set the parent of this node

            # Go left and right, assigning parents to those nodes too
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)  # Start DFS from the root (top person in the family tree)

        # B. BFS Step: Use a queue to explore nodes level by level
        queue = deque([target])  # Start the search from the target node
        seen = {target}  # Use a set to remember who we've visited to avoid loops
        distance = 0  # Track how far we’ve moved from the target node

        # Start BFS search until we reach the desired distance (k)
        while queue and distance < k:
            current_length = len(queue)  # How many people are at the current level

            for _ in range(current_length):
                node = queue.popleft()  # Get the next node from the queue

                # Explore all neighbors: left child, right child, and parent
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in seen:  # If it's valid and not visited yet
                        seen.add(neighbor)  # Mark as visited
                        # print([item.val for item in seen])
                        queue.append(neighbor)  # Add to the queue for the next level

            distance += 1  # Move to the next level (increase the distance by 1)

        # C. Collect all nodes at the desired distance k
        return [node.val for node in queue]  # Extract values from the remaining nodes in the queue

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
# Building the tree structure
#         3
#       /   \
#      5     1
#     / \   / \
#    6   2 0   8
#       / \
#      7   4
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

solution = Solution()
target = root.left  # Node with value 5
k = 2

# Output: [7, 4, 1]
print(solution.distanceK(root, target, k))

"""
Example 1: Social Network Scenario
Imagine a friendship network where people are connected to friends (like nodes in a tree). The task could be framed 
like this:

Rephrased Problem:
You are given a person in a social network and a list of their connections. Each person in the network has direct 
friendships with other people. Some friends may even be friends of friends.

Your task: Write a function that finds all people exactly k steps away from a given person. In other words, return all 
people who can be reached by exactly k connections (friend-of-friend-of-friend, etc.).

Return the result as a list of person IDs (in any order).

Key Observations:
The friendship network represents an undirected graph.
Finding people exactly k connections away is like BFS (breadth-first search) in a graph.
This scenario maps perfectly to your original problem without explicitly mentioning graphs or trees.
Example 2: File System or Folder Structure
Imagine this problem in the context of a file system, where files are organized in a tree-like structure with folders 
and subfolders.

Rephrased Problem:
Given a root folder, a target folder, and an integer 
𝑘
k, find all folders or files that are exactly k levels away from the target folder.

You can move both down into subfolders and up to parent folders.
Return the list of such folders or files (in any order).

Key Observations:
The file system forms a tree, and you need to traverse it like a graph (both up and down).
This question disguises the original problem as a practical folder traversal task.
Example 3: Communication Network
This scenario could be about a communication network where data packets are sent between nodes.

Rephrased Problem:
In a network, each router is connected to other routers. Given a specific router and a number k, find all routers that 
are exactly k hops away from the given router.

You can move through connected routers in any direction. Return a list of router IDs at exactly k hops.

Key Observations:
Routers and connections form a graph.
Finding routers k hops away is a perfect analogy for distance-k traversal in your original problem.
What Makes These Scenarios More Realistic?
Practical framing: These problems are disguised as real-world challenges (social networks, file systems, networks).
Hidden graph structure: The underlying graph or tree structure isn’t mentioned explicitly, but the logic maps directly 
to a graph traversal problem.
Problem-solving focus: In interviews, companies like Amazon care more about how you approach the problem than whether 
you recognize it as a tree or graph.
How You Could Handle This in an Interview:
Identify the Hidden Structure:

Even if the problem isn’t framed as a tree/graph problem, try to identify whether it involves connections, levels, or 
paths—these are clues that graphs or trees are involved.
Explain Your Approach Thoughtfully:

In the interview, you could say: "This problem seems to involve traversing both up and down the structure, which 
reminds me of a graph traversal. I think I’ll use DFS or BFS to solve it."
Relate It to the Problem You Know:

If you get a disguised version of this problem, you can recognize it and say: "This reminds me of finding nodes at a 
certain distance n a tree."
"""