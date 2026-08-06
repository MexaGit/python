from collections import deque

class RecentCounter:
    def __init__(self):
        # Initialize an empty deque (a double-ended queue) to store the ping times.
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Remove all pings that are older than 3000 milliseconds (3 seconds) from the current ping time.
        # The condition `t - 3000` ensures that only the pings in the last 3000 ms are kept in the queue.
        while self.queue and self.queue[0] < t - 3000:
            # Remove the oldest ping (at the front of the deque) since it's out of the 3000 ms range.
            self.queue.popleft()

        # Add the current ping `t` to the queue (at the back).
        self.queue.append(t)

        # The length of the queue now represents the number of valid pings in the last 3000 ms.
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Input: 1, 100, 3001, 3002
# Expected output: 1, 2, 3, 3 (only the last three pings are within the 3000 ms window for the last call)

obj = RecentCounter()
print(obj.ping(1))     # Output: 1 (only one ping so far)
print(obj.ping(100))   # Output: 2 (two pings, 1 and 100, both within 3000 ms of each other)
print(obj.ping(3001))  # Output: 3 (three pings: 1, 100, 3001 all within 3000 ms)
print(obj.ping(3002))  # Output: 3 (pings: 1 is removed, only 100, 3001, and 3002 remain)

# Input: 1, 3000, 6000, 9000
# Expected output: 1, 2, 1, 1 (only one or two pings are within the 3000 ms window at each step)
print("#----------------------------------------------------------------#")
obj = RecentCounter()
print(obj.ping(1))     # Output: 1 (only one ping so far)
print(obj.ping(3000))  # Output: 2 (pings at 1 and 3000)
print(obj.ping(6000))  # Output: 2 (pings at 3000 and 6000; ping at 1 is removed)
print(obj.ping(9000))  # Output: 2 (pings at 6000 and 9000; ping at 3000 is removed)

"""
https://docs.python.org/3/library/collections.html#collections.deque
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns }
the number of requests that has happened in the past 3000 milliseconds (including the new request). 
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

Explanation:

ping(1):
Queue: [1]
Output: 1

ping(3000):
Queue: [1, 3000]
Output: 2

ping(6000):
Remove pings older than 6000 - 3000 = 3000
Ping at 1 is removed.
Queue: [3000, 6000]
Output: 2

ping(9000):
Remove pings older than 9000 - 3000 = 6000
Ping at 3000 is removed.
Queue: [6000, 9000]
Output: 2
"""