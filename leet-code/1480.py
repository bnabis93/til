from typing import List


class Solution:
    """Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums."""

    def runningSum(self, nums: List[int]) -> List[int]:
        """Time Complexity = O(nums) / Space Complexity = O(nums)"""
        running_sums = [0]
        for idx, num in enumerate(nums):
            sum_of_num = running_sums[idx] + num
            running_sums.append(sum_of_num)
        return running_sums[1:]
