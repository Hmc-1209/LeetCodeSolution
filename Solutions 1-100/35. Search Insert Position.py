from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        left, right = 0, len(nums) - 1

        while left <= right:
            pos = (left + right) // 2
            if nums[pos] == target:
                return pos
            elif nums[pos] > target:
                right = pos - 1
            else:
                left = pos + 1

        return left


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
