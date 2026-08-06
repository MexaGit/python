from typing import List

class Solution:
    # Hash Set
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        more_losses = set()

        for winner, loser in matches:
            # Add winner
            if (winner not in one_loss) and (winner not in more_losses):
                zero_loss.add(winner)
            # Add or move loser.
            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_losses.add(loser)
            elif loser in more_losses:
                continue
            else:
                one_loss.add(loser)

        return [sorted(list(zero_loss)), sorted(list(one_loss))]

    # Hash Set + Hash Map
    def findWinners1(self, matches: List[List[int]]) -> List[List[int]]:
        seen = set()
        losses_count = {}

        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            losses_count[loser] = losses_count.get(loser, 0) + 1

        # Add players with 0 or 1 loss to the corresponding list.
        zero_lose, one_lose = [], []
        for player in seen:
            count = losses_count.get(player, 0)
            if count == 0:
                zero_lose.append(player)
            elif count == 1:
                one_lose.append(player)

        return [sorted(zero_lose), sorted(one_lose)]

    #Hash Map
    class Solution:
        def findWinners2(self, matches: List[List[int]]) -> List[List[int]]:
            losses_count = {}

            for winner, loser in matches:
                losses_count[winner] = losses_count.get(winner, 0)
                losses_count[loser] = losses_count.get(loser, 0) + 1

            zero_lose, one_lose = [], []
            for player, count in losses_count.items():
                if count == 0:
                    zero_lose.append(player)
                if count == 1:
                    one_lose.append(player)

            return [sorted(zero_lose), sorted(one_lose)]

    #Counting with Array
    def findWinners4(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = [-1] * 100001

        for winner, loser in matches:
            if losses_count[winner] == -1:
                losses_count[winner] = 0
            if losses_count[loser] == -1:
                losses_count[loser] = 1
            else:
                losses_count[loser] += 1

        answer = [[], []]
        for i in range(100001):
            if losses_count[i] == 0:
                answer[0].append(i)
            elif losses_count[i] == 1:
                answer[1].append(i)

        return answer

solution = Solution()
print(solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))

"""
You are given an integer array matches where matches[i] = [winner i, loser i] indicates that the player winner i 
defeated player loser i in a match.

Return a list answer of size 2 where:
answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]

Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Player	Matches                             Played	Losses Count	Classification
1	    Won against 3	                    0	    0               Losses
2	    Won against 3	                    0	    0               Losses
3	    Lost to 1 & 2, won against          6	    2	            2+ Losses
4	    Won against 5, 8, 9; lost to 10	    1	    1               Loss
5	    Won against 6 & 7; lost to 4	    1	    1               Loss
6	    Lost to 3 & 5	                    2	    2+              Losses
7	    Lost to 5	                        1	    1               Loss
8	    Lost to 4	                        1	    1               Loss
9	    Lost to 4 & 10	                    2	    2+              Losses
10	    Won against 4 & 9	                0	    0               Losses

"""