from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort the box types based on the number of units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        unitCount = 0

        # Iterate through the sorted box types
        for boxType in boxTypes:
            # Determine the number of boxes we can take
            boxCount = min(truckSize, boxType[0])
            # Update the total unit count
            unitCount += boxCount * boxType[1]
            # Reduce the available truck size
            truckSize -= boxCount
            # If the truck is full, exit the loop
            if truckSize == 0:
                break

        return unitCount


# Example test case
# Input: boxTypes = [[1, 3], [2, 2], [3, 1]], truckSize = 4
# Output: 8
# Explanation: There are:
# - 1 box of the first type that contains 3 units.
# - 2 boxes of the second type that contain 2 units each.
# - 3 boxes of the third type that contain 1 unit each.
# You can take all the boxes of the first and second types, and one box of the third type.
# The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
solution = Solution()
print(solution.maximumUnits([[1, 3], [2, 2], [3, 1]], 4))  # Expected output: 8

"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] =
[numberOfBoxesi, numberOfUnitsPerBoxi]:
    numberOfBoxesi is the number of boxes of type i.
    numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can
choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

#--------------------------------------------------------------------------------------------#

Approach 2: Using Array Sort
We could simplify the process of finding the maximum units in every iteration. We could arrange the box types in a 
particular order such that we could get the desired box type in constant time without having to iterate over the 
entire array. The simple way to implement this is to sort the array boxTypes in decreasing order of a number of units.

Once all the elements in array boxTypes are sorted in that order, we know that box type at 0th position is the one with
maximum units and the one at 1st position having the second highest number of units and so on.

Algorithm
    Initially, the truck is empty, hence the remaining truck capacity that must be filled would be equal to the 
    truck size. Initialise variable remainingTruckSize to truckSize.
    Sort the array boxTypes in decreasing order of a number of units.
    Start picking up each box type from boxTypes array starting from 0th position. The number of boxes that can be put
    in the truck would be the minimum of remainingTruckSize and the number of boxes available of the given type. 
    Calculate the total number of units and reduce the truck's remaining capacity based on the number of boxes put in 
    the truck.
    The process of filling the truck with box types would continue until the truck is not full i.e remainingTruckSize 
    is greater than 0.

The following figure illustrates the approach in detail for truckSize = 8 and 
boxTypes = [[3, 10], [6, 5], [4, 7], [2, 9]]
"""