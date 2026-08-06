from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        # Store the maximum size of the moving window
        self.size = size
        # Initialize an empty deque to store the window values
        self.queue = deque()

    def next(self, val: int) -> float:
        # If the queue has reached the maximum size, remove the oldest element
        if len(self.queue) >= self.size:
            self.queue.popleft()  # Remove the oldest value from the left end

        # Add the new value to the deque (to the right end)
        self.queue.append(val)

        # Return the average of the current window (sum of the elements divided by their count)
        return sum(self.queue) / len(self.queue)

    """
    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)
    """

# Test case where the number of values exceeds the window size
# Input: size=3, next values: 1, 10, 3, 5
# Expected output: 1.0, 5.5, 4.6667, 6.0

obj = MovingAverage(3)
print(obj.next(1))   # Output: 1.0 (queue: [1], average: 1.0)
print(obj.next(10))  # Output: 5.5 (queue: [1, 10], average: (1 + 10) / 2 = 5.5)
print(obj.next(3))   # Output: 4.6667 (queue: [1, 10, 3], average: (1 + 10 + 3) / 3 = 4.6667)
print(obj.next(5))   # Output: 6.0 (queue: [10, 3, 5], average: (10 + 3 + 5) / 3 = 6.0)

