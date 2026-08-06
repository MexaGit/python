import heapq

# Note: Python's heapq implements a min heap

heap = [67, 341, 234, -67, 12, -976]
heapq.heapify(heap)

heapq.heappush(heap, 7451)
heapq.heappush(heap, -5352)

# The numbers will be printed in sorted order
while heap:
    print(heapq.heappop(heap))