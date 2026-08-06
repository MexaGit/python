class Solution(object):
    def largestSumOfAverages(self, A, K):
        # Step 1: Build prefix sum array
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        # Function to calculate average of subarray A[i:j]
        def average(i, j):
            return (P[j] - P[i]) / float(j - i)

        N = len(A)

        # Step 2: Initialize dp array with averages for one partition
        dp = [average(i, N) for i in range(N)]

        # Step 3: Fill dp array for K-1 remaining partitions
        for k in range(K - 1):
            for i in range(N):
                for j in range(i + 1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        # Step 4: Return the maximum sum of averages for K partitions
        return dp[0]


solution = Solution()
print(solution.largestSumOfAverages([3,2,4,1,5], 2))          # Output: 7.5

"""
https://leetcode.com/problems/largest-sum-of-averages/description/
"""