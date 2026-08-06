from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0  # Initialize the count of boats
        i = 0  # Pointer for the lightest person
        j = len(people) - 1  # Pointer for the heaviest person
        people.sort()  # Sort the people by their weights

        # While there are still people to rescue
        while i <= j:
            # If the lightest and heaviest person can share a boat
            if people[i] + people[j] <= limit:
                i += 1  # Move the pointer for the lightest person

            j -= 1  # Always move the pointer for the heaviest person
            ans += 1  # Increment the boat count

        return ans  # Return the total number of boats used


# Example test cases
# Example 1:
# Input: people = [1, 2], limit = 3
# Output: 1 (Both can share a boat)
print(Solution().numRescueBoats([1, 2], 3))  # Expected output: 1

# Example 2:
# Input: people = [3, 2, 2, 1], limit = 3
# Output: 3 (We need 3 boats: [1, 2], [2], [3])
print(Solution().numRescueBoats([3, 2, 2, 1], 3))  # Expected output: 3

"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where
each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum
of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

#------------------------------------------------------------------------------------------------#

Let's try to establish why the greedy strategy of attempting to pair the lightest and heaviest person at each step is
optimal.

Let x denote the heaviest person and y denote the lighest person at any given step. There are two possibilities:
    1. x + y > limit. There's no way that x can fit with anyone, since y is already the lightest person.
    Therefore they must sit together.
    2. x + y <= limit. This implies that y could pair with anyone, since x is already the heaviest person.
    To maximize the efficiency of the boats, if we can pair y with anyone, we should pair them with the heaviest person,
    which is x. This makes the most of the boat and also makes it easier to make future pairings since we don't need
    to worry about x anymore.

Again, this is not a formal proof, but an example of how one could explain their thought process in an interview.
From here, the algorithm is easy to implement using a sort and two pointers.

#------------------------------------------------------------------------------------------------#

Approach 1: Greedy (Two Pointer)
Intuition

If the heaviest person can share a boat with the lightest person, then do so. Otherwise, the heaviest person can't 
pair with anyone, so they get their own boat.

The reason this works is because if the lightest person can pair with anyone, they might as well pair with the heaviest
person.

Algorithm

Let people[i] to the currently lightest person, and people[j] to the heaviest.
Then, as described above, if the heaviest person can share a boat with the lightest person 
(if people[j] + people[i] <= limit) then do so; otherwise, the heaviest person sits in their own boat.
"""