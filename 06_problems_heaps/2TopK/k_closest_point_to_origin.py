import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize a max heap with the first k points
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)  # Create the heap

        # Process the remaining points
        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:  # Compare with the farthest point in the heap
                heapq.heappushpop(heap, (dist, i))

        # Return the k closest points by their indices stored in the heap
        return [points[i] for (_, i) in heap]

    def squared_distance(self, point: List[int]) -> int:
        """Calculate the squared Euclidean distance from the origin."""
        return point[0] ** 2 + point[1] ** 2


# Example usage
solution = Solution()

# Test case 1
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
points1 = [[1,3],[-2,2]]
k1 = 1
result1 = solution.kClosest(points1, k1)
print(result1)  # Expected output: [[-2, 2]]

# Test case 2
points2 = [[3, 3], [5, -1], [-2, 4]]
k2 = 2
result2 = solution.kClosest(points2, k2)
print(result2)  # Expected output: [[-2, 4], [3, 3]]

"""
https://leetcode.com/problems/k-closest-points-to-origin/description/
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

#----------------------------------------------------------------------------------#

Approach 2: Max Heap or Max Priority Queue
Intuition

While we must iterate over all elements in the points array, we only need to keep track of the k closest points 
encountered so far. We could therefore choose to store them in a separate data structure. In order to keep this data 
structure capped at k elements, we will need to keep track of the point that is farthest away from the origin and thus 
the next point to be removed when a closer point is found.

The ideal data structure for this purpose is a max heap or max priority queue. These data structures allow access to 
the max value in constant time and perform replacements in logarithmic time.

Note: We can simulate max heap functionality in a min heap data structure by inserting −dist instead of dist, if 
necessary.

At the start of our iteration through points, we will insert the first k elements into our heap. Once the heap is 
"full", we can then compare each new point to the farthest point stored in the heap. If the new point is closer, then 
we should remove the farthest point from the heap and insert the new point.

After the entire points array has been processed, we can create an array from the points stored in the heap and then 
return the answer.

Algorithm
1. Use a max heap (or max priority queue) to store points by distance.
    Store the first k elements in the heap.
    Then only add new elements that are closer than the top point in the heap while removing the top point to keep the 
    heap at k elements.
2. Return an array of the k points stored in the heap.
 
"""
