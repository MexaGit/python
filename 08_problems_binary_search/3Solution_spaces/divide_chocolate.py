from typing import List

class Solution:
    # Binary Search + Greedy
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # Calculate the number of people to split the chocolate between
        number_of_people = k + 1

        # Binary search between the minimum and average sweetness
        left = min(sweetness)  # Minimum possible sweetness
        right = sum(sweetness) // number_of_people  # Maximum possible sweetness (average)

        # Perform binary search
        while left < right:
            mid = (left + right + 1) // 2  # Midpoint of current search range
            cur_sweetness = 0  # Total sweetness assigned to current person
            people_with_chocolate = 0  # Number of people with a valid chunk of chocolate

            # Distribute sweetness chunks
            for s in sweetness:
                cur_sweetness += s

                # If current chunk has reached or exceeded the desired sweetness
                if cur_sweetness >= mid:
                    people_with_chocolate += 1
                    cur_sweetness = 0  # Reset sweetness for the next person

            # If enough people got a piece of chocolate, move to higher sweetness
            if people_with_chocolate >= number_of_people:
                left = mid  # Try for a larger sweetness value
            else:
                right = mid - 1  # Otherwise, try for a smaller sweetness value

        return right

# Example Test Case 1:
# Input: sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 5
# Output: 6
# Explanation: Divide the sweetness array into 6 chunks, each with at least 6 sweetness.
print(Solution().maximizeSweetness([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))  # Expected output: 6

# Example Test Case 2:
# Input: sweetness = [5, 6, 7, 8, 9, 1, 2, 3, 4], k = 8
# Output: 1
# Explanation: Divide the sweetness array into 9 chunks, each with at least 1 sweetness.
print(Solution().maximizeSweetness([5, 6, 7, 8, 9, 1, 2, 3, 4], 8))  # Expected output: 1

# Example Test Case 3:
# Input: sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1], k = 4
# Output: 2
# Explanation: Divide the sweetness array into 5 chunks, each with at least 2 sweetness.
print(Solution().maximizeSweetness([1, 1, 1, 1, 1, 1, 1, 1, 1], 4))  # Expected output: 2

"""
https://leetcode.com/problems/divide-chocolate/description/
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using
k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.
"""