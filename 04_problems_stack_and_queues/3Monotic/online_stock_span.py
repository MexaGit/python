class StockSpanner:
    def __init__(self):
        self.stack = []  # Stack to keep track of prices and their spans

    def next(self, price: int) -> int:
        ans = 1  # The span starts at 1 for the current price
        # While there are elements in the stack and the current price is greater than or equal to
        # the price at the top of the stack
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the popped price to the current span
            ans += self.stack.pop()[1]

        # Append the current price and its span to the stack
        self.stack.append([price, ans])
        return ans

# Test case with increasing prices
# Input: prices = [100, 80, 60, 70, 60, 75, 85]
# Expected Output: [1, 1, 1, 2, 1, 4, 6]
# Explanation:
# - Price 100: span = 1 (no previous prices)
# - Price 80: span = 1 (80 is less than 100)
# - Price 60: span = 1 (60 is less than 80)
# - Price 70: span = 2 (70 is greater than 60 but less than 80)
# - Price 60: span = 1 (60 is less than 70)
# - Price 75: span = 4 (75 is not greater than 80 and spans over the last 60, 60, and 70)
# - Price 85: span = 6 (85 is greater than 75, 70, 80, and two 60s but stops at 100)

spanner = StockSpanner()
prices = [100, 80, 60, 70, 60, 75, 85]
output = [spanner.next(price) for price in prices]
print(output)  # Output: [1, 1, 1, 2, 1, 4, 6]

# Test case with fluctuating prices
# Input: prices = [30, 20, 25, 10, 15, 20, 30]
# Expected Output: [1, 1, 2, 1, 2, 3, 7]
# Explanation:
# - Price 30: span = 1 (no previous prices)
# - Price 20: span = 1 (20 is less than 30)
# - Price 25: span = 2 (25 is greater than 20 but less than 30)
# - Price 10: span = 1 (10 is less than 25)
# - Price 15: span = 2 (15 is greater than 10 but less than 25)
# - Price 20: span = 3 (20 is greater than 15 but less than 25)
# - Price 30: span = 7 (30 is greater than all previous prices)

spanner = StockSpanner()
prices = [30, 20, 25, 10, 15, 20, 30]
output = [spanner.next(price) for price in prices]
print(output)  # Output: [1, 1, 2, 1, 2, 3, 7]

"""
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price
for the current day.
The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and
going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2,
then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4
consecutive days.

Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8,
then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3
consecutive days.

Implement the StockSpanner class:
StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.


Example 1:
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
"""