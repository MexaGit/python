from typing import List

# Approach 1: Search with Array
def countElements(arr: List[int]) -> int:
    count = 0
    for x in arr:
        if x + 1 in arr:
            count += 1
    return count
# Note that we could also do this as a one-liner generator comprehension.
# return sum(1 for x in arr if x + 1 in arr)

# Approach 2: Search with HashSet
def countElements1(self, arr: List[int]) -> int:
    hash_set = set(arr)
    count = 0
    for x in arr:
        if x + 1 in hash_set:
            count += 1
    return count

# Approach 3: Search with Sorted Array
def countElements2(self, arr: List[int]) -> int:
    arr.sort()
    count = 0
    run_length = 1
    for i in range(len(arr)):
        if arr[i - 1] != arr[i]:
            if arr[i - 1] + 1 == arr[i]:
                count += run_length
            run_length = 0
        run_length += 1
    return count

print(countElements([1,1,3,3,5,5,7,7]))

"""
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
"""