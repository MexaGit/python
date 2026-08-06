from collections import defaultdict
from typing import List

class Solution:
    # iterative version of this algorithm:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x, y))

        ans = 0
        stack = [0]
        seen = {0}
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if (node, neighbor) in roads:
                        ans += 1
                    seen.add(neighbor)
                    stack.append(neighbor)

        return ans

# Example usage and test cases

# Test case 1
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Explanation: We need to reorder roads [1 -> 3] and [4 -> 0].
solution = Solution()
print(solution.minReorder(n, connections))  # Output: 3

# Test case 2
n = 5
connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
# Explanation: We need to reorder road [1 -> 2].
print(solution.minReorder(n, connections))  # Output: 1