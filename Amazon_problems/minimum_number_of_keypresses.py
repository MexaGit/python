from collections import Counter


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        cache = Counter(s)
        vals = sorted(cache.items(), key=lambda x: -x[1])
        ans = 0
        r = key = 1
        order = [0] * 26

        for k, v in vals:
            x = ord(k) - 97

            if not order[x]:
                order[x] = r
                key += 1

                if key == 10:
                    key = 1
                    r += 1

            ans += order[x] * v


        return ans

"""
https://leetcode.com/problems/minimum-number-of-keypresses/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Input: s = "apple"
Output: 5
Explanation: One optimal way to setup your keypad is shown above.
Type 'a' by pressing button 1 once.
Type 'p' by pressing button 6 once.
Type 'p' by pressing button 6 once.
Type 'l' by pressing button 5 once.
Type 'e' by pressing button 3 once.
A total of 5 button presses are needed, so return 5.
"""