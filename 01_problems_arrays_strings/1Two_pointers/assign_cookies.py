from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        children = cookie = 0

        while children < len(g) and cookie < len(s):
            if g[children] <= s[cookie]:
                children += 1
            cookie += 1
        return children

solution = Solution()
print(solution.findContentChildren( [1,2,3], [1,1]))
"""
Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1
content. You need to output 1.

Example 2:
Input: g = [1,2], s = [1,2,3]
Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
 
"""