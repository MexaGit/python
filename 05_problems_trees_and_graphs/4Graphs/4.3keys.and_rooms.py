from typing import List

class Solution:
    # 🗝️ The detective's mission: Can you visit all rooms?
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}  # 📝 Start with room 0 unlocked (you’ve already visited it).
        stack = [0]  # 🎒 Start exploring from room 0. LIFO

        # 🔄 Keep exploring rooms until you have no more keys left in your stack.
        while stack:
            node = stack.pop()  # 🚪 Open the room you’re currently holding the key for.

            # 🗝️ Look at all the keys inside the current room.
            for neighbor in rooms[node]:
                # ❓ If you find a key to a room you haven’t visited yet...
                if neighbor not in seen:
                    seen.add(neighbor)  # 📝 Mark that room as visited.
                    stack.append(neighbor)  # 🎒 Add the key to your stack to explore it later.

        # ✅ If you’ve visited every room, return True.
        # ❌ If not, return False.
        return len(seen) == len(rooms)  # Compare visited rooms with the total number of rooms.

# Example usage and test cases
# For example:
# rooms = [[1], [2], [3], []]
# Here’s how it maps:
# Room 0 (index 0) contains key to Room 1.
# Room 1 (index 1) contains key to Room 2.
# Room 2 (index 2) contains key to Room 3.
# Room 3 (index 3) contains no keys (empty list).

# Test case 1
rooms = [[1], [2], [3], []]
# Explanation: You can visit room 0, then use key 1 to enter room 1, use key 2 to enter room 2, and use key 3 to
# enter room 3. Since we were able to visit every room, we return true.
solution = Solution()
print(solution.canVisitAllRooms(rooms))  # Output: True

# Input:
# rooms = [[1, 3], [3, 0, 1], [2], [0]]
# rooms = [
#     [1, 3],  # Room 0 has keys to room 1 and room 3
#     [3, 0, 1],  # Room 1 has keys to room 3, room 0, and itself
#     [2],  # Room 2 has a key to itself
#     [0]   # Room 3 has a key to room 0
# ]

# Test case 2
rooms = [[1, 3], [3, 0, 1], [2], [0]]
# Explanation: Room 2 cannot be visited because it is not connected to any room that has been unlocked.
print(solution.canVisitAllRooms(rooms))  # Output: False

"""
Scenario: Delivery Driver in a Warehouse System 🚚
You are a delivery driver who needs to collect packages from multiple warehouses (rooms).

However, only Warehouse 0 is unlocked at the start.
Inside each warehouse, you may find keys to unlock other warehouses.
Your job is to visit every warehouse to pick up the packages.
If you can access every warehouse, you complete your route successfully. Otherwise, some packages are missed.
In this delivery system analogy, each warehouse is a node (room), and each key to another warehouse is a connection 
(edge).
"""