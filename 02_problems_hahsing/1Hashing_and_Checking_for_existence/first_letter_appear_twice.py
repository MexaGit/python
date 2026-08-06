class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)):
            c = s[i]
            for j in range(i):
                if s[j] == c:
                    return c

        return ""

    def repeatedCharacter1(self, s: str) -> str:
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)

        return " "

    def find_numbers(self, nums):
        # Initialize an empty list to store the result
        ans = []

        # Convert the input list to a set to eliminate duplicates and allow fast lookups
        nums = set(nums)

        # Iterate through each unique number in the set
        for num in nums:
            # Check if neither num + 1 nor num - 1 exist in the set
            if (num + 1 not in nums) and (num - 1 not in nums):
                ans.append(num)  # If true, add num to the result list

        # Return the final list of isolated numbers
        return ans

solution = Solution()
print(solution.repeatedCharacter("abccbaacz"))
print(solution.find_numbers([1, 3, 5, 7]))  # Output: [1, 3, 5, 7]
print(solution.find_numbers([1, 2, 3, 5, 7, 8]))  # Output: [5]

"""
The letter 'a' appears on the indexes 0, 5 and 6.
The letter 'b' appears on the indexes 1 and 4.
The letter 'c' appears on the indexes 2, 3 and 7.
The letter 'z' appears on the index 8.
The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second 
occurrence is the smallest.
"""