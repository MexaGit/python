from math import ceil
from typing import List


class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        # Sort both jobs and workers
        jobs.sort()
        workers.sort()

        res = 0
        # Calculate the time each worker needs to find the job
        for i in range(len(jobs)):
            res = max(res, ceil(jobs[i] / workers[i]))

        return res

"""
https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
Example 1:

Input: jobs = [5,2,4], workers = [1,7,5]
Output: 2
Explanation:
- Assign the 2nd worker to the 0th job. It takes them 1 day to finish the job.
- Assign the 0th worker to the 1st job. It takes them 2 days to finish the job.
- Assign the 1st worker to the 2nd job. It takes them 1 day to finish the job.
It takes 2 days for all the jobs to be completed, so return 2.
It can be proven that 2 days is the minimum number of days needed.
"""