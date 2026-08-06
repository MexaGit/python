from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        # Variable to keep track of the highest altitude encountered
        highest_point = 0
        # Iterate over each altitude change in the gain list
        for altitude_gain in gain:
            # Add the current altitude gain to the previous altitude to get the new altitude
            current_altitude += altitude_gain
            print(current_altitude, end=" ")
            # Update highest_point if the new current altitude is higher
            highest_point = max(highest_point, current_altitude)
        print()
        return highest_point

solution = Solution()
print(solution.largestAltitude([-5,1,5,0,-7]))
"""
Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [-5,-4,1,1,-6]. The highest is 1.

Time Complexity:

Loop through the gain list:
The code iterates through the gain list once, performing constant time operations (addition and comparison) for each 
element. If the list has n elements, the time complexity is O(n), where n is the length of the gain list.

Thus, the time complexity is O(n).

Space Complexity:

Space used by variables:
The code uses a constant amount of extra space:
current_altitude and highest_point are single integer variables.
The input list gain is provided as input and not modified, so no additional space is required beyond the input list.

Since we don't use any additional data structures that scale with the input size, the space complexity is O(1) 
(constant space).
"""