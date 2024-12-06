from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = pivot = 0
        end = len(nums) - 1

        while end > start:
            mid = (end + start) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid

        pivot = start
        if nums[pivot] == target:
            return pivot

        if nums[pivot] <= target <= nums[-1]:
            start = pivot + 1
            end = len(nums) - 1
        else:
            start = 0
            end = pivot - 1

        while end >= start:
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search([1], 0))
print(s.search([1, 3, 5], 1))
print(s.search([3, 5, 1], 3))
print(s.search([4, 5, 6, 7, 8, 9, 1, 2, 3], 1))
print(s.search([8, 9, 2, 3, 4], 9))
