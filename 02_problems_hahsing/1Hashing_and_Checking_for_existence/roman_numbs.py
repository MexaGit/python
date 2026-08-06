class Solution:
    def intToRoman(self, num: int) -> str:
        # A list of tuples where each tuple contains a number and its corresponding Roman numeral.
        # The list is ordered from the largest to the smallest value for easy conversion.
        # the key operation is iterating over the values in a specific order (largest to smallest).
        # A list of tuples is perfect for this because we can simply loop over it in order.
        digits = [
            (1000, "M"),   # 1000 -> M
            (900, "CM"),   # 900 -> CM
            (500, "D"),    # 500 -> D
            (400, "CD"),   # 400 -> CD
            (100, "C"),    # 100 -> C
            (90, "XC"),    # 90 -> XC
            (50, "L"),     # 50 -> L
            (40, "XL"),    # 40 -> XL
            (10, "X"),     # 10 -> X
            (9, "IX"),     # 9 -> IX
            (5, "V"),      # 5 -> V
            (4, "IV"),     # 4 -> IV
            (1, "I")       # 1 -> I
        ]

        # Initialize an empty list to store the resulting Roman numerals
        roman_digits = []

        # Loop through the list of digits, starting from the largest value to the smallest
        for value, symbol in digits:
            #print(value, symbol)
            # If num becomes 0, we stop because we don't need to convert anything further.
            if num == 0:
                break

            # divmod(num, value) returns a tuple (count, remainder):
            # - count is how many times 'value' fits into 'num'
            # - remainder is the new value of 'num' after subtracting the 'value * count'.
            # Example of how divmod() will be called at each step for num = 58:
            # count, num = divmod(58, 50) -> count = 1, num = 8 (append "L")
            # count, num = divmod(8, 10)  -> count = 0, num = 8 (skip "X")
            # count, num = divmod(8, 5)   -> count = 1, num = 3 (append "V")
            # count, num = divmod(3, 1)   -> count = 3, num = 0 (append "III")
            count, num = divmod(num, value)
            # The loop starts by checking each value in digits, beginning from the largest (1000).
            # Even if num is too small for the current value, it will try dividing num by that value.
            # If the value doesn't fit into num, count will be 0, and num stays the same.

            # Example of how divmod() will be called at each step for num = 58:
            # - count, num = divmod(58, 1000) -> count = 0, num = 58 (skip "M")
            # - count, num = divmod(58, 500)  -> count = 0, num = 58 (skip "D")
            # - count, num = divmod(58, 50)   -> count = 1, num = 8 (append "L")
            # - count, num = divmod(8, 10)    -> count = 0, num = 8 (skip "X")
            # - count, num = divmod(8, 5)     -> count = 1, num = 3 (append "V")
            # - count, num = divmod(3, 1)     -> count = 3, num = 0 (append "III")
            # Each iteration of the loop handles one value from the digits list, performs a divmod(), and either
            # appends the corresponding Roman numeral symbol (if count > 0) or skips the symbol (if count = 0).

            # If 'count' is greater than 0, it means we can use 'count' copies of 'symbol'
            # Append 'count' copies of 'symbol' to the roman_digits list
            # roman_digits.append("I" * 3)  # Appends "III"
            roman_digits.append(symbol * count)
            #print(symbol, count)

        # Join the list of Roman numerals into a single string and return it as the result.
        return "".join(roman_digits)

# Example test cases
sol = Solution()
print(sol.intToRoman(58))  # Output: "LVIII" (50 + 5 + 3)
print(sol.intToRoman(1994))  # Output: "MCMXCIV" (1000 + 900 + 90 + 4)

"""
https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=hash-table
Time complexity: O(1) (constant time), because the loop always runs for a fixed number of iterations (13) and the 
operations inside the loop are constant-time operations.
Space complexity: O(1) (constant space), because the space usage is independent of the size of num.
"""
