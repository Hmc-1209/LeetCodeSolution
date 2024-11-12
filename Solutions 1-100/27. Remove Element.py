from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i, e in enumerate(nums):
            if e == val:
                count += 1
            else:
                nums[i-count] = nums[i]

        return len(nums) - count


s = Solution()
print(s.removeElement([3,2,2,3], 3))
print(s.removeElement([0,1,2,2,3,0,4,2], 2))
