from typing import List

class Solution:
    # iterative
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

        return len(seen) == len(rooms)

# Example usage and test cases

# Test case 1
rooms = [[1], [2], [3], []]
# Explanation: You can visit room 0, then use key 1 to enter room 1, use key 2 to enter room 2, and use key 3 to
# enter room 3. Since we were able to visit every room, we return true.
solution = Solution()
print(solution.canVisitAllRooms(rooms))  # Output: True

# Test case 2
rooms = [[1, 3], [3, 0, 1], [2], [0]]
# Explanation: Room 2 cannot be visited because it is not connected to any room that has been unlocked.
print(solution.canVisitAllRooms(rooms))  # Output: False