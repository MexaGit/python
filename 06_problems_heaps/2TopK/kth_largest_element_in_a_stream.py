import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize a min-heap and store the value of k (for k-th largest element)
        self.min_heap = []
        self.k = k

        # Process each element in the initial list to build the heap
        for num in nums:
            self.add(num)  # Add each number and maintain the heap with k largest elements

    def add(self, val: int) -> int:
        # Add the new element to the min_heap if:
        # 1. The heap has less than k elements, or
        # 2. The new element is greater than the smallest element (heap[0]) in the heap
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)  # Push the new element to the heap
            if len(self.min_heap) > self.k:  # If heap exceeds k elements, pop the smallest one
                heapq.heappop(self.min_heap)

        # Return the k-th largest element (the root of the min-heap)
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Test cases
# Example 1:
# Input: ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output: [null, 4, 5, 5, 8, 8]
# Explanation:
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // return 4
# kthLargest.add(5); // return 5
# kthLargest.add(10); // return 5
# kthLargest.add(9); // return 8
# kthLargest.add(4); // return 8

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # Output: 4 (after adding 3, the 3rd largest element is 4)
print(kthLargest.add(5))  # Output: 5 (after adding 5, the 3rd largest element is 5)
print(kthLargest.add(10))  # Output: 5 (after adding 10, the 3rd largest element is 5)
print(kthLargest.add(9))  # Output: 8 (after adding 9, the 3rd largest element is 8)
print(kthLargest.add(4))  # Output: 8 (after adding 4, the 3rd largest element is still 8)

# Example 2:
# Input: ["KthLargest", "add", "add", "add", "add"]
# [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
# Output: [null, 7, 7, 7, 8]
# Explanation:
# KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
# kthLargest.add(2); // return 7
# kthLargest.add(10); // return 7
# kthLargest.add(9); // return 7
# kthLargest.add(9); // return 8

kthLargest2 = KthLargest(4, [7, 7, 7, 7, 8, 3])
print(kthLargest2.add(2))  # Output: 7 (after adding 2, the 4th largest element is 7)
print(kthLargest2.add(10))  # Output: 7 (after adding 10, the 4th largest element is still 7)
print(kthLargest2.add(9))  # Output: 7 (after adding 9, the 4th largest element is still 7)
print(kthLargest2.add(9))  # Output: 8 (after adding 9, the 4th largest element becomes 8)


"""
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in
real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit
their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously
returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth
highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element
in the pool of test scores so far.

#-------------------------------------------------------------------------------------#

Approach 2: Heap
Intuition
In Approach 1, sorting the entire stream of numbers seems unnecessary because we only need the k-th largest element. Maintaining a sorted list becomes costly as its size increases. To optimize, we can focus on only the necessary elements for retrieving and updating the k-th largest element.

Current

Consider a stream of numbers [0, 4, 6, 9] where k = 3 and incoming val = 2. Before adding 2, the k-th largest element is 4. Adding 2 does not affect 4's position since 2 is smaller. Now, if the incoming value is 7, which is greater than both 4 and 6, 7 would become the 2nd largest number, pushing 6 to be the new k-th largest element, and 4 is no longer in the top k.

Current

From this example, we see that keeping track of just the k largest elements allows us to efficiently maintain the k-th largest element:

If an incoming element val is smaller than or equal to the existing k-th largest element: The k largest elements remain unchanged, and we can return the current k-th largest element.
If val is larger than the current k-th largest element: It replaces the current k-th largest element. After adding val, the new k-th largest element is the next largest element.
To efficiently maintain the k largest elements, we use a min-heap. In a min-heap, elements are organized such that the smallest element is always at the top (root node), providing O(1) access time. Adding elements and removing the top element from the min-heap can be done in O(logn) time.

For our problem, the min-heap will contain the k largest elements, with the k-th largest element at the top. If a new val is greater than the k-th largest element, we add val to the heap and remove the top element, keeping the heap size at k and updating the k-th largest element.

In our optimized approach, we initialize the min-heap with the initial stream nums in the constructor and ensure it contains only the k largest elements. In the add(int val) function, if val is smaller than the current k-th largest element and the heap already contains k elements, we return the top element. Otherwise, we add val, remove the top element if the heap size exceeds k, and return the updated top element.

This approach is more efficient in both time and space complexity compared to maintaining a fully sorted list, as the relaxed ordering of a heap allows quick access and updates to the k largest elements without the overhead of sorting the entire stream.

Algorithm
In the constructor:
Initialize class variable k to the input value k
Initialize a class PriorityQueue minHeap to hold the k largest elements
Iterate through each element num in the initial stream nums:
Call add(num)
In the add(int val) function:
If val is greater than the smallest element in minHeap or the size of minHeap is less than k elements:
Add val to minHeap
If the size of minHeap is greater than k, then remove the top element
Return the top element as the k-th largest element in the stream

"""