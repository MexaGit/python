class Solution:
    # Approach #1 Sorting
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num

    # Approach #2 HashSet [Accepted]
    def missingNumber1(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

    # Approach #3 Bit Manipulation
    def missingNumber2(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    # Approach #4 Gauss' Formula [Accepted]
    def missingNumber3(self, nums):
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

solution = Solution()
print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))

