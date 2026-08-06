# Memoized Fibonacci implementation to optimize repeated calculations.
def fibonacci(n):
    # Base case: return 0 for n = 0
    if n == 0:
        return 0
    # Base case: return 1 for n = 1
    if n == 1:
        return 1

    # If the value is already calculated (memoized), return it directly.
    if n in memo:
        return memo[n]

    # If not, compute the value by summing the previous two Fibonacci numbers
    # and store the result in the memo dictionary for future use.
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


# Dictionary to store previously computed Fibonacci numbers.
memo = {}

# Test cases
print(fibonacci(5))  # Output: 5 (sequence: 0, 1, 1, 2, 3, 5)
print(fibonacci(7))  # Output: 13 (sequence: 0, 1, 1, 2, 3, 5, 8, 13)

