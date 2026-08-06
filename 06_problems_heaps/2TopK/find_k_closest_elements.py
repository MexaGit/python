import heapq
from typing import List

class Solution:
    # maxHeap
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        # Iterate through the elements in the array
        for num in arr:
            # Distance from x, and the distance is calculated absolute(abs) value between their difference
            distance = abs(x - num)  # Calculate the distance from x
            # Push a tuple of (-distance, -num) to create a max-heap based on distance
            heapq.heappush(heap, (-distance, -num))
            # Ensure the heap size does not exceed k
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the farthest element if heap size exceeds k

        # Extract the numbers from the heap and return sorted results
        return sorted([-pair[1] for pair in heap])

# Example usage
solution = Solution()

# Test case 1
arr1 = [1, 2, 3, 4, 5]
k1 = 4
x1 = 3
result1 = solution.findClosestElements(arr1, k1, x1)
print(result1)  # Expected output: [1, 2, 3, 4]

# Test case 2
arr2 = [1, 2, 3, 4, 5]
k2 = 4
x2 = 10
result2 = solution.findClosestElements(arr2, k2, x2)
print(result2)  # Expected output: [2, 3, 4, 5]

"""
https://leetcode.com/problems/find-k-closest-elements/description/
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
    
#------------------------------------------------------------------------------------------------#
In the last problem, we wanted the maximum frequencies, so we put the frequencies in a heap. In this problem, we want
the minimum differences, so let's put the differences in a heap. When we wanted the maximums, we used a min heap so 
that pops would remove the smaller elements. In this problem, we want the smallest differences, so if we use a max 
heap, then pops will remove the largest differences.

The problem states that ties should be decided by taking the smaller element. For example, let's say we have x = 5 and 
two numbers 3, 7. Both have an equal distance of 2, but we should consider the 3 as having a "better" score since it is 
less than 7.

How do we handle ties with a heap? This is dependent on the language you are using. In a language like Python or C++, 
you can put an ordered collection (like a tuple or list) in the heap, and it will go through each entry individually 
to determine the value. Using the same example with x = 5 and 3, 7, we could push both (2, 3) and (2, 7) to our max 
heap. The first element 2 in these tuples indicates the difference from x = 5. The second element in these tuples are 
the elements themselves. When determining which tuple has a "larger" value, the heap will compare the first position 
and see that they are equal. It will then move to the second position and see that 7 > 3, and thus 7 would be popped 
first.

In a language like Java, you will need to implement a custom comparator which is a function that explicitly tells your 
heap how to handle the tiebreak case.

"""