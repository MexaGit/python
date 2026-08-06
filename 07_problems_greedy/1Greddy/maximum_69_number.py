class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert the input 'num' to a list of characters 'num_char_list'.
        num_char_list = list(str(num))

        # Iterate over the list (from high to low).
        for i, cur_char in enumerate(num_char_list):
            # If we find the first '6', replace it with '9' and break the loop.
            if cur_char == '6':
                num_char_list[i] = '9'
                break

        # Convert the modified char list to an integer and return it.
        return int("".join(num_char_list))


# Example test cases
# Example 1:
# Input: num = 9669
# Output: 9969 (Changing the first 6 to 9 gives the maximum number)
print(Solution().maximum69Number(9669))  # Expected output: 9969

# Example 2:
# Input: num = 9996
# Output: 9999 (Changing the last 6 to 9)
print(Solution().maximum69Number(9996))  # Expected output: 9999

# Example 3:
# Input: num = 9999
# Output: 9999 (No 6 to change)
print(Solution().maximum69Number(9999))  # Expected output: 9999

"""
You are given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

#---------------------------------------------------------------------------------------#

In this problem, we are given an integer num where every digit is either 6 or 9, we can change up to 1 digit
(from 6 to 9 or vice versa).

The task is to return the largest integer we can get.
After observation, we can get these conclusions as follows:
    We can only increment num by converting a digit 6 to 9.
    We should always convert the highest digit 6. Suppose num = 669, it has multiple digits 6, we must convert the
    first one to make it 969 rather than 699.
    If every digit of num is 9, we only need to return num since it already stands for the largest integer.

More examples:
669 9669 9999 96
 |    |   |   |
969 9969 9999 99
Hence, the task equals finding the highest digit 6 (if it exists) and replacing it with 9.

Approach 1: Convert the integer to an iterable object
Intuition

The most intuitive method to find the first digit 6 is to traverse through each digit of num from high to low, 
as we discussed in the overview section.

However, we can't traverse over an integer in C++, Java, or Python, nor can we modify it. Hence, we can first convert 
it to an iterable and mutable object, such as a string in C++, a string builder in Java, or a list in Python, 
and traverse over the object to locate the first occurrence of 6.

Algorithm
1. Convert the input integer num to an iterable and mutable object num_obj.
2. Iterate over num_obj, if we find a digit 6, replace it with 9 and stop the iteration.
3. Return the integer converted from the modified num_obj.
"""