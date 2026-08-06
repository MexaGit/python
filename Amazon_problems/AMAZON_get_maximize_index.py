def getMaximizeIndex(importance):
    # Step 1: Sort the array in descending order to maximize prefix sum
    # This ensures we start with the largest values, giving us the best chance
    # of keeping the prefix sum positive for as long as possible.
    importance.sort(reverse=True)

    # Step 2: Initialize prefix sum
    prefix_sum = 0

    # Step 3: Compute the prefix sum in one pass
    # This loop processes each element exactly once (O(n) time).
    for i, value in enumerate(importance):
        prefix_sum += value  # Add the current value to the prefix sum

        # EARLY TERMINATION: If prefix sum becomes negative, return the index.
        if prefix_sum < 0:
            return i  # Return the first index where the prefix sum turns negative

    # Step 4: If no negative prefix sum found, return -1
    # This happens if all prefix sums remain non-negative.
    return -1


# Example Usage:
importance = [2, -4, 1]
print(getMaximizeIndex(importance))  # Output: 2

importance = [-1, -2, -3]
print(getMaximizeIndex(importance))  # Output: 0 (First element makes sum negative)

importance = [10, 5, 7]
print(getMaximizeIndex(importance))  # Output: -1 (Sum never turns negative)


"""
given n products and an array, determine the positive prefix sum of importance
example: given n = 3 importance = [2, 1, 4]
there's no way to get a -1

prefix sum if we find the prefix sum of importnsce in this manner only it, will be [2,3,-1] 
first index where the prefix sum array turn negative is 2

we can apply prefix sum on the array[2, -4, 1] it will be [2, -2, -1]
the first index where the prefix sum array turns negative is 1

we can apply prefix sum on the array [-4, 1, 2]. It will be [-4, -3 -1]
the first index where the prefixsum array turns negative is 1

so the answer is 2. it can be proved that this is one of the most optimal arrangements by taking every possible 
premutation

complete the function getmaximizeIndex parameter int[]: importance: the importance of package index, retyrb -1

example:
stdin       function
-----           --------
2                importance[] size n = 2
1                importance = [1,2]
2
"""