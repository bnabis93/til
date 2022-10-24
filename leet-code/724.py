from typing import List


class Solution:
    """Pivot index : 좌우 대칭이 되는 index. 해당 index를 기준으로 좌우의 합이 동일하다.
    e.g. [1,7,3,6,5,6], pivot index = 3"""

    def pivotIndex(self, nums: List[int]) -> int:
        return


def pivotIndex(nums: List[int]) -> int:
    """Time limit solution."""
    left_sum = 0
    right_sum = sum(nums)
    for idx, _ in enumerate(nums):
        right_sum = sum(nums[idx + 1 :])  # List slicing : O(n), sum : O(n)
        left_sum = sum(nums[:idx])
        if left_sum == right_sum:
            return idx
    return -1


def pivotIndex(nums: List[int]) -> int:
    """Time Complexity : O(nums), Space Complexity : O(1."""
    left_sum = 0
    right_sum = sum(nums)
    for idx, num in enumerate(nums):
        right_sum -= num
        if left_sum == right_sum:
            return idx
        left_sum += num
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))
print(pivotIndex([2, 1, -1]))
