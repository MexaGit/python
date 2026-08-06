def answer_queries(nums, queries, limit):
    prefix = [nums[0]]

    # Build the prefix sum array
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])  # Add the current element to the running sum
        # For example, if nums = [1, 2, 3, 4], the prefix array will be [1, 3, 6, 10]

    ans = [] # List to store the results of each query
    for x, y in queries:
        # Calculate the sum of the subarray nums[x:y] using the prefix sum array
        if x > 0:
            # When x > 0, subtract prefix[x - 1] from prefix[y] to get the sum of the subarray
            curr = prefix[y] - prefix[x - 1]
            # Example for query (1, 3):
            # prefix[y] = prefix[3] = 10 (sum of nums[0:3])
            # prefix[x - 1] = prefix[0] = 1 (sum of nums[0])
            # So, curr = 10 - 1 = 9, which is the sum of nums[1:3] (i.e., [2, 3, 4])
        else:
            curr = prefix[y]
            # When x == 0, the subarray starts from the beginning (index 0)
            # So, curr is just prefix[y], which represents the sum of nums[0:y+1]
            # Example:
            # For query (0, 2): The subarray is [nums[0], nums[1], nums[2]] -> prefix[2] = 6
            # For query (0, 4): The subarray is [nums[0], nums[1], nums[2], nums[3], nums[4]] -> prefix[4] = 15
        ans.append(curr < limit)

    return ans

# Example usage
nums = [1, 2, 3, 4, 5]
queries = [(0, 2), (1, 3), (0, 4)]
limit = 10
print(answer_queries(nums, queries, limit))  # Output: [True [1,2,3] = 6, True [2,3,4] = 9, False [1,2,3,4,5] = 15]

"""
Building a prefix sum is a form of pre-processing. Pre-processing is a useful strategy in a variety of problems 
where we store pre-computed data in a data structure before running the main logic of our algorithm. 
While it takes some time to pre-process, it's an investment that will save us a huge amount of time during 
the main parts of the algorithm.

Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, 
return a boolean array that represents the answer to each query. A query is true if the sum of the subarray 
from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is 
[true, false, true]. For each query, the subarray sums are [12, 14, 12].

#--------------------------------------------------------------------------------#

Time Complexity: O(n + m), where n is the length of nums (for creating the prefix sum) and m is the number of queries 
(for processing them).

Space Complexity: O(n) for the prefix sum array.
"""