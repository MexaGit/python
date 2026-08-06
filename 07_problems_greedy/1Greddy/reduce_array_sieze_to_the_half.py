from typing import List
import collections

def minSetSize(arr: List[int]) -> int:
    # Count the occurrences of each number in the array
    counts = collections.Counter(arr)

    # Extract the counts in reverse-sorted order
    # most_common gives (number, count) pairs, sorted by count in descending order
    counts = [count for number, count in counts.most_common()]

    # Initialize variables to keep track of total removed numbers and set size
    total_removed = 0
    set_size = 0

    # Remove numbers until at least half of the array is removed
    for count in counts:
        total_removed += count  # Increment total removed by the current count
        set_size += 1           # Increment the size of the set used to remove numbers
        if total_removed >= len(arr) // 2:  # Check if we've removed at least half
            break

    return set_size  # Return the size of the set

# Example test case
# Input: arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5
# (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater
# than half of the size of the old array.
print(minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))  # Expected output: 2

"""
https://leetcode.com/problems/reduce-array-size-to-the-half/description/
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers
in the array.
Return the minimum size of the set so that at least half of the integers of the array are removed.

#----------------------------------------------------------------------------------#

Approach 2: Hashing/ Counting
Intuition

A better way of doing the first step is to use a Multiset (also known as a Counter or Bag). A Multiset is, as the name suggests, a type of Set that allows duplicates. It is implemented using a HashMap, where the key is the set items, and the value is an integer stating how many times the item is in the set. In C++, it is called multiset. In Python, it is Counter. In Java and JavaScript, you will have to make your own using a HashMap.

For this problem, the keys will be each unique number in arr, and the values will be how many times each occurred. Building this up using a HashMap is straightforward (Counter and multiset are even easier!).

multiset = new Hash Map
for number in arr:
    if number is not in multiset keys:
       add number to multiset keys with value of 0
    increment value for number by 1
Now we need to determine which counts to take, to minimise the final set size. The simplest way is to extract the values, sort them, and then proceed in the same way as Approach 1.

Algorithm
"""