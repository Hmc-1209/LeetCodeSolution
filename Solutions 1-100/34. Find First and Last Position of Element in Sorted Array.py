from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        first_find = -1

        if len(nums) == 0:
            return [-1, -1]

        while end >= start:
            mid = (end + start) // 2
            if nums[mid] == target:
                first_find = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        if first_find == -1:
            return [-1, -1]

        start = first_find
        end = len(nums) - 1
        while end >= start:
            mid = (end + start) // 2
            if nums[mid] == target:
                start = mid + 1
            else:
                end = mid - 1

        return [first_find, end]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
print(s.searchRange([], 0))
