from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[2]
        result = []
        nums.sort()

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if abs(threeSum - target) < abs(closest - target):
                    closest = threeSum
                if threeSum < target:
                    j += 1
                else:
                    k -= 1
        return closest


s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))
print(s.threeSumClosest([0,0,0], 1))
