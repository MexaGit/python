import collections
from typing import List

class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:

        def check(a, b):
            return abs(a - b) < 1e-5

        hs = collections.defaultdict(list)
        seen = {}

        for (a, b), v in zip(equations, values):
            if a == b:
                if check(v, 1):
                    continue
                else:  # understand, if eq a/a not equal 1, edge case
                    return True

            else:
                hs[a].append((b, v))
                hs[b].append((a, 1 / v))

        # print(hs)

        # def dfs():
        def dfs(cur):
            for n, r in hs[cur]:
                if n in seen:
                    if not check(seen[cur] / seen[n], r):
                        return True
                else:
                    seen[n] = seen[cur] / r
                    if dfs(n):
                        return True
            return False

        for cur in hs:
            if cur not in seen:
                seen[cur] = 1
            if dfs(cur):
                return True

        return False

"""
https://leetcode.com/problems/check-for-contradictions-in-equations/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Example 1:

Input: equations = [["a","b"],["b","c"],["a","c"]], values = [3,0.5,1.5]
Output: false
Explanation:
The given equations are: a / b = 3, b / c = 0.5, a / c = 1.5
There are no contradictions in the equations. One possible assignment to satisfy all equations is:
a = 3, b = 1 and c = 2.
"""