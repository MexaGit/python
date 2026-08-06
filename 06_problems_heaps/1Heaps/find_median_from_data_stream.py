import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap for the lower half of numbers
        self.max_heap = []
        # Min-heap for the upper half of numbers
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Add to max-heap (inverted to use as a max-heap)
        heapq.heappush(self.max_heap, -num)
        # Balance the heaps by moving the largest of max-heap to min-heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        # Ensure min-heap does not have more elements than max-heap
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # If max-heap has more elements, the median is the root of max-heap
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # If both heaps are of equal size, the median is the average of both roots
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0

# Test case from the example
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
actions = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
values = [[], [1], [2], [], [3], []]

medianFinder = None
results = []

for action, value in zip(actions, values):
    if action == "MedianFinder":
        medianFinder = MedianFinder()
        results.append(None)
    elif action == "addNum":
        medianFinder.addNum(value[0])
        results.append(None)
    elif action == "findMedian":
        median = medianFinder.findMedian()
        results.append(median)

# Expected output: [null, null, null, 1.5, null, 2.0]
print(results)  # Output: [None, None, None, 1.5, None, 2.0]

# # Example test cases
# medianFinder = MedianFinder()
# medianFinder.addNum(1)
# medianFinder.addNum(2)
# print(medianFinder.findMedian())  # Expected output: 1.5
# medianFinder.addNum(3)
# print(medianFinder.findMedian())  # Expected output: 2.0
# medianFinder.addNum(4)
# print(medianFinder.findMedian())  # Expected output: 2.5

"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""