class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store Roman numerals and their corresponding integer values
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
        }

        total = 0  # This will store the total integer value
        ptr = 0  # Pointer to traverse the string 's' character by character

        # Loop through the string 's', processing each Roman numeral or combination
        while ptr < len(s):
            # First, check if there's a two-character Roman numeral (like "IV", "CM", etc.)
            # ptr:ptr+2 means that it takes a two-character substring starting at 'ptr'
            # Example: if ptr = 0 and s = "MCMXCIV", s[ptr:ptr+2] will be "MC"
            # This condition ptr < len(s) - 1 is used to ensure you have at least two characters
            if ptr < len(s) - 1 and s[ptr:ptr+2] in values:
                # If the two-character Roman numeral exists, add its value to 'total'
                # If s[ptr:ptr+2] = "CM", the dictionary lookup values["CM"] returns 900
                total += values[s[ptr:ptr+2]]
                # Move 'ptr' forward by 2 since we processed two characters
                ptr += 2
            else:
                # Otherwise, process a single character Roman numeral
                total += values[s[ptr]]
                # Move 'ptr' forward by 1 since we processed only one character
                ptr += 1

        # Return the total converted integer value after processing the entire string
        return total

# Test cases for understanding how the code works
sol = Solution()

# Example 1: "MCMXCIV" (1994)
# Iterations:
# ptr = 0: s[ptr:ptr+2] = "MC" → not in values, process "M" → total = 1000, ptr = 1
# ptr = 1: s[ptr:ptr+2] = "CM" → in values, add 900 → total = 1900, ptr = 3
# ptr = 3: s[ptr:ptr+2] = "XC" → in values, add 90 → total = 1990, ptr = 5
# ptr = 5: s[ptr:ptr+2] = "IV" → in values, add 4 → total = 1994, ptr = 7
print(sol.romanToInt("MCMXCIV"))  # Expected output: 1994

# Example 2: "LVIII" (58)
# Iterations:
# ptr = 0: s[ptr:ptr+2] = "LV" → not in values, process "L" → total = 50, ptr = 1
# ptr = 1: s[ptr:ptr+2] = "VI" → not in values, process "V" → total = 55, ptr = 2
# ptr = 2: s[ptr:ptr+2] = "II" → not in values, process "I" → total = 56, ptr = 3
# ptr = 3: s[ptr:ptr+2] = "II" → not in values, process "I" → total = 57, ptr = 4
# ptr = 4: s[ptr:ptr+2] = "I"  → process "I" → total = 58, ptr = 5
print(sol.romanToInt("LVIII"))  # Expected output: 58

# Example 3: "IX" (9)
# Iterations:
# ptr = 0: s[ptr:ptr+2] = "IX" → in values, add 9 → total = 9, ptr = 2
print(sol.romanToInt("IX"))  # Expected output: 9


"""
https://leetcode.com/problems/roman-to-integer/description/?envType=problem-list-v2&envId=hash-table
Time Complexity: O(n), where n is the length of the input string.
Space Complexity: O(1), because the algorithm uses constant additional space.
"""