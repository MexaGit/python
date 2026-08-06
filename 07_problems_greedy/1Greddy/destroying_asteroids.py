from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Sort the asteroids array in increasing order
        asteroids.sort()

        # Iterate through each asteroid
        for asteroid in asteroids:
            # If the current asteroid is larger than the current mass, return False
            if asteroid > mass:
                return False

            # Otherwise, the planet absorbs the asteroid, increasing its mass
            mass += asteroid

        # If all asteroids can be destroyed, return True
        return True


# Test cases

# Example 1:
# Input: mass = 10, asteroids = [3, 9, 19, 5, 21]
# Output: True
# Explanation:
# The planet's mass starts at 10.
# After absorbing asteroid 3, the mass becomes 13.
# After absorbing asteroid 5, the mass becomes 18.
# After absorbing asteroid 9, the mass becomes 27.
# After absorbing asteroid 19, the mass becomes 46.
# Finally, the planet absorbs the last asteroid 21 and its mass becomes 67.
# Therefore, the planet can destroy all asteroids.
solution = Solution()
mass1 = 10
asteroids1 = [3, 9, 19, 5, 21]
print(solution.asteroidsDestroyed(mass1, asteroids1))  # Output: True

# Example 2:
# Input: mass = 5, asteroids = [4, 9, 10]
# Output: False
# Explanation:
# The planet's mass starts at 5.
# It can absorb the first asteroid 4, but when it encounters the second asteroid 9,
# its mass (9) is larger than the planet's mass (5), so the planet can't destroy all asteroids.
mass2 = 5
asteroids2 = [4, 9, 10]
print(solution.asteroidsDestroyed(mass2, asteroids2))  # Output: False

"""
https://leetcode.com/problems/destroying-asteroids/description/
You are given an integer mass, which represents the original mass of a planet. You are further given an integer array
asteroids, where asteroids[i] is the mass of the ith asteroid.

You can arrange for the planet to collide with the asteroids in any arbitrary order. If the mass of the planet is
greater than or equal to the mass of the asteroid, the asteroid is destroyed and the planet gains the mass of the
asteroid. Otherwise, the planet is destroyed.

Return true if all asteroids can be destroyed. Otherwise, return false.
"""