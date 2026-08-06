from collections import defaultdict
from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(cards)):
            dic[cards[i]].append(i)

        ans = float("inf")
        for key in dic:
            arr = dic[key]
            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)

        return ans if ans < float("inf") else -1

    # We can actually improve this algorithm slightly by observing that we don't need to store all the indices,
    # but only the most recent one that we saw for each number.
    def minimumCardPickup1(self, cards: List[int]) -> int:
        dic = defaultdict(int)
        ans = float("inf")
        for i in range(len(cards)):
            if cards[i] in dic:
                ans = min(ans, i - dic[cards[i]] + 1)

            dic[cards[i]] = i

        return ans if ans < float("inf") else -1

solution = Solution()
print(solution.minimumCardPickup([3,4,2,3,4,7]))

"""
The question is equivalent to: what is the shortest distance between any two of the same element?
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards
are matching if the cards have the same value.
Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among
the picked cards. If it is impossible to have matching cards, return -1.

Example 1:
Input: cards = [3,4,2,3,4,7]
Output: 4

Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3.
Note that picking up the cards [4,2,3,4] is also optimal.

Example 2:
Input: cards = [1,0,5,3]
Output: -1

Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
"""