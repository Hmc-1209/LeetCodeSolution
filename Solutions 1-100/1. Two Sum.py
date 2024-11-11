from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            desired = target - nums[i]
            if desired in hash:
                return [i, hash[desired]]
            hash[nums[i]] = i
        return []


s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
