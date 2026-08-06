from collections import Counter
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Count the frequency of each integer in the array
        counts = Counter(arr)
        # Sort the frequencies in descending order
        ordered = sorted(counts.values(), reverse=True)

        # Remove integers from the least frequent to the most frequent until k is exhausted
        while k:
            val = ordered[-1]  # Get the least frequent count
            if val <= k:  # If we can remove all occurrences of this integer
                k -= val  # Reduce k by the count of the integer
                ordered.pop()  # Remove this integer's frequency from the list
            else:
                break  # If k is less than the count, stop removing

        # Return the number of unique integers left
        return len(ordered)

# Example test cases
# Example 1:
# Input: arr = [5, 5, 4, 4, 3, 3, 1, 1], k = 4
# Output: 2 (We can remove 4 of the integers to leave 2 unique integers, e.g., [5, 4])
# The counts are: 5 = 2, 4 = 2, 3 = 2, 1 = 2
# We can remove 4 (we have only k = 4) occurrences of 1 and 3 (both appear 2 times) to leave 5 and 4
print(Solution().findLeastNumOfUniqueInts([5, 5, 4, 4, 3, 3, 1, 1], 4))  # Expected output: 2

# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
print(Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))  # Expected output: 2

"""
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/editorial/
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k
elements.

We need to perform k removals - what element is the best to remove? We can improve our answer only if we remove all of 
an element, so we should greedily remove the element with the lowest frequency at each step.

We can use a hash map to find the frequency of each element. Then we can sort the keys according to their frequencies, 
and iterate through the keys starting with the least frequent element. At each key, if the frequency is less than or 
equal to k, we can remove that key and decrease k by the count. We continue this until we run out of removals. 
The number of keys remaining at the end is the answer.
 
"""