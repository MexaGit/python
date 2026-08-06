def fibonacci(n):
    # Initialize an array to store Fibonacci numbers up to n.
    # arr[0] = 0 and arr[1] = 1 are the base cases.
    arr = [0] * (n + 1)

    # Base case: the second Fibonacci number is 1
    arr[1] = 1

    # Loop from 2 to n to compute Fibonacci numbers using previous two values.
    for i in range(2, n + 1):
        # Each number is the sum of the two preceding numbers.
        arr[i] = arr[i - 1] + arr[i - 2]

    # Return the nth Fibonacci number.
    return arr[n]


# Test cases
print(fibonacci(5))  # Output: 5 (sequence: 0, 1, 1, 2, 3, 5)
print(fibonacci(7))  # Output: 13 (sequence: 0, 1, 1, 2, 3, 5, 8, 13)

"""
Top-down vs. bottom-up
This method of using recursion and memoization is also known as "top-down" dynamic programming. It is named as such
because we start from the top (the original problem) and move down toward the base cases. For example, we wanted
the n'th Fibonacci number, so we started by calling fibonacci(n). We move down with recursion until we reach the base
cases (F(0) and F(1)).

Another way to approach a dynamic programming problem is with a "bottom-up" algorithm. In bottom-up, we start at the
bottom (base cases) and work our way up to larger problems. This is done iteratively and also known as tabulation.

Top-down and bottom-up refer only to how you decide to implement your algorithm. There is fundamentally nothing 
different between the two approaches. Every top-down implementation can be implemented bottom-up and vice versa. 
The things that define a DP algorithm are the base cases and recurrence relation (which we will talk about more in 
the next article).

There are pros and cons to both, but the main arguments for each are:

Usually, a bottom-up implementation is faster. This is because iteration has less overhead than recursion, although 
this is less impactful if your language implements tail recursion.
However, a top-down approach is usually easier to write. With recursion, the order that we visit states does not matter. 
With iteration, if we have a multidimensional problem, it can sometimes be difficult figuring out the correct 
configuration of your for loops.
"""